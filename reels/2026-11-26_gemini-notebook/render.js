// Render index.html to MP4 (1080x1920, 30 fps) with headless Chromium + ffmpeg.
// usage: node render.js [out.mp4]            full render (muxes voice.mp3 if present)
//        node render.js --stills 0.5,3,7.2    PNG stills to out/still_<t>.png
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path'), fs = require('fs');
(async () => {
  const args = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(__dirname, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))));
  await page.waitForTimeout(300);
  const total = await page.evaluate(() => window.TOTAL);
  fs.mkdirSync(path.join(__dirname, 'out'), { recursive: true });
  if (args[0] === '--stills') {
    for (const t of args[1].split(',').map(Number)) {
      await page.evaluate(t => seek(t), t);
      await page.waitForTimeout(60);
      await page.screenshot({ path: path.join(__dirname, 'out', `still_${t.toFixed(2)}.png`) });
    }
    console.log('total', total.toFixed(2)); await browser.close(); return;
  }
  const out = path.resolve(args[0] || path.join(__dirname, 'out', 'gemini_notebook_reel.mp4'));
  const voice = fs.existsSync(path.join(__dirname, 'soundtrack.wav')) ? path.join(__dirname, 'soundtrack.wav') : path.join(__dirname, 'voice.mp3');
  const ff = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '30', '-i', '-'];
  if (fs.existsSync(voice)) ff.push('-i', voice, '-af', 'apad', '-c:a', 'aac', '-b:a', '192k', '-t', total.toFixed(3));
  ff.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart', out);
  const proc = spawn('ffmpeg', ff, { stdio: ['pipe', 'inherit', 'inherit'] });
  const n = Math.ceil(total * 30);
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => seek(t), i / 30);
    const buf = await page.screenshot({ type: 'jpeg', quality: 93 });
    if (!proc.stdin.write(buf)) await new Promise(r => proc.stdin.once('drain', r));
    if (i % 150 === 0) console.log(`frame ${i}/${n}`);
  }
  proc.stdin.end();
  await new Promise(r => proc.on('close', r));
  console.log('wrote', out, total.toFixed(2) + 's');
  await browser.close();
})();
