const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const n of [1,2]){await p.goto('file://'+process.cwd()+`/slide_${n}.html`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:`slide_${n}.png`});}await b.close();})();
