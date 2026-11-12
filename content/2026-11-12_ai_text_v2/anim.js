const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const dir = process.argv[2]; fs.mkdirSync(dir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 6480, height: 1350 } });
  await p.goto('file://' + __dirname + '/panorama.html');
  await p.waitForSelector('body[data-ready]');
  await p.evaluate(() => document.querySelectorAll('.strike').forEach(el => {
    const L = el.getTotalLength() + 20; el.style.strokeDasharray = L; el.style.strokeDashoffset = L; el.dataset.len = L; }));
  const fps = 30, total = 6000, starts = [600, 1500, 2400], dur = 650;
  const ease = t => t < .5 ? 2*t*t : 1 - Math.pow(-2*t + 2, 2) / 2;
  for (let f = 0; f < total * fps / 1000; f++) {
    const t = f * 1000 / fps;
    const prog = starts.map(s => ease(Math.min(1, Math.max(0, (t - s) / dur))));
    await p.evaluate(prog => document.querySelectorAll('.strike').forEach((el, i) => {
      el.style.strokeDashoffset = el.dataset.len * (1 - prog[i]);
      el.closest('svg').parentElement; }), prog);
    await p.evaluate(prog => document.querySelectorAll('.phrase').forEach((el, i) => {
      el.style.color = prog[i] > .9 ? '#8C7B6B' : '#190F09'; el.style.transition = 'none'; }), prog);
    await p.screenshot({ path: `${dir}/f${String(f).padStart(4,'0')}.png`, clip: { x: 1080, y: 0, width: 1080, height: 1350 } });
  }
  await b.close();
})();
