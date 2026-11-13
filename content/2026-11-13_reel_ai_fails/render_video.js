// Renders the animated reel: each scene HTML is stepped frame by frame via window.setT(t).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
// Scene cut points (seconds) taken from the pauses in audio/voiceover.mp3
const CUTS = [0, 7.6, 10.5, 18.8, 28.55, 34.5, 41.5, 48.0];
const NAMES = ["00_hook","00_list","01_clients","02_reports","03_publish","04_access","05_end"];
const FPS = 30, out = process.argv[2];
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  let n = 0;
  for (let k = 0; k < NAMES.length; k++) {
    const name = NAMES[k], nf = Math.round(CUTS[k+1]*FPS) - Math.round(CUTS[k]*FPS);
    await p.goto('file://' + path.join(__dirname, 'html', name + '.html'));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    for (let f = 0; f < nf; f++) {
      await p.evaluate(t => window.setT(t), f / FPS);
      await p.screenshot({ path: `${out}/f${String(n++).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    }
  }
  await b.close(); console.log('frames', n);
})();
