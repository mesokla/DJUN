const {chromium}=require('playwright');(async()=>{const [only]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/reel.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const fps=30;const fr=only?only.split(',').map(Number):[...Array(Math.round(fps*35.3)).keys()];
for(const i of fr){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`frames/f${String(i).padStart(4,'0')}.png`});}await b.close();})();
