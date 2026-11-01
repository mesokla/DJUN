const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=6;i++){await p.goto('file://'+process.cwd()+`/slide_${i}.html`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:`v8_${i}.png`});}await b.close();})();
