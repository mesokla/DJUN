const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=7;i++){await p.goto('file://'+process.cwd()+'/slide_'+i+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForFunction(()=>document.body.dataset.done);await p.waitForTimeout(200);
// rerun drawing after fonts load
await p.screenshot({path:'slide_'+i+'.png'});}await b.close();})()
