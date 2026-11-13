// Renders the animated reel: each scene HTML is stepped frame by frame via window.setT(t).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const SCENES = [["00_hook",4],["00_list",3],["01_clients",7],["02_reports",9],["03_publish",6],["04_access",7],["05_end",7]];
const FPS = 30, out = process.argv[2];
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  let n = 0;
  for (const [name, dur] of SCENES) {
    await p.goto('file://' + path.join(__dirname, 'html', name + '.html'));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    for (let f = 0; f < dur * FPS; f++) {
      await p.evaluate(t => window.setT(t), f / FPS);
      await p.screenshot({ path: `${out}/f${String(n++).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    }
  }
  await b.close(); console.log('frames', n);
})();
