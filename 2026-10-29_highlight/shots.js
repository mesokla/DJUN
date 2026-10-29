const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of ['story_2','story_3','story_5']){await p.goto('http://127.0.0.1:8765/../'+n+'.html').catch(()=>{});await p.goto('file://'+process.cwd()+`/${n}.html`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);await p.screenshot({path:`${n}.png`});}
await p.goto('file://'+process.cwd()+'/story_4.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);await p.evaluate(()=>render(9));await p.screenshot({path:'story_4_final.png'});
await b.close();})();
