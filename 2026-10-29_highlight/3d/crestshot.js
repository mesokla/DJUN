const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('E:',e.message));
await p.goto('http://127.0.0.1:8765/glyph.html');await p.waitForFunction(()=>document.title==='ready',null,{timeout:60000});
await p.evaluate(()=>showCrest(-0.28,0.1));await p.screenshot({path:'../crest3d.png',omitBackground:true});await b.close();})();
