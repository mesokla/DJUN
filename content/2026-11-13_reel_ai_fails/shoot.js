const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  fs.mkdirSync(__dirname + '/frames', { recursive: true });
  for (const f of fs.readdirSync(__dirname + '/html').sort()) {
    await p.goto('file://' + __dirname + '/html/' + f); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150); await p.evaluate(() => window.setT && window.setT(20));
    await p.screenshot({ path: __dirname + '/frames/' + f.replace('.html', '.png') });
  }
  await b.close();
})();
