const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/story_4.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const fps=30,n=fps*7;for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`s4_frames/f${String(i).padStart(4,'0')}.png`});}await b.close();})();
