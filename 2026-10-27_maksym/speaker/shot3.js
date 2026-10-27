const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();let p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+process.cwd()+'/s2.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:'s2_bg.png'});
p=await b.newPage({viewport:{width:952,height:714}});await p.goto('file://'+process.cwd()+'/mask.html');await p.screenshot({path:'mask.png'});await b.close();})();
