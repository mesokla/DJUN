const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:7560,height:1350}});await p.goto('file://'+process.cwd()+'/pano.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);await p.screenshot({path:process.argv[2],omitBackground:true});
const q=await b.newPage({viewport:{width:156,height:73},deviceScaleFactor:4});const car=await p.evaluate(()=>{const e=document.querySelector('.car');return e?e.outerHTML:''});
if(car){await q.setContent('<body style="margin:0;background:transparent">'+car.replace(/class="car" style="[^"]*"/,'')+'</body>');await q.screenshot({path:'car4x.png',omitBackground:true});}
await b.close();})()
