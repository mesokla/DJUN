const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 6480, height: 1350 } });
  await p.goto('file://' + __dirname + '/panorama.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForSelector('body[data-ready]'); await p.waitForTimeout(200);
  require('fs').mkdirSync(__dirname + '/out', { recursive: true });
  await p.screenshot({ path: __dirname + '/out/panorama.png' });
  for (let i = 0; i < 6; i++)
    await p.screenshot({ path: `${__dirname}/out/slide_${i+1}.png`, clip: { x: i*1080, y: 0, width: 1080, height: 1350 } });
  await b.close();
})();
