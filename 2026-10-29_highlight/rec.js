const {chromium}=require('playwright');(async()=>{const [html,out,dur]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/'+html);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const fps=30,n=Math.round(fps*parseFloat(dur));for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`${out}/f${String(i).padStart(4,'0')}.png`});}await b.close();})();
