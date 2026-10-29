const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('E:',e.message));
await p.goto('http://127.0.0.1:8765/glyph.html');await p.waitForFunction(()=>document.title==='ready',null,{timeout:60000});
const G=[['brace',-0.5,0.2,0.15,30],['O',0.55,-0.25,0,26],['hash',-0.45,0.3,-0.12,24],['chev',0.5,-0.2,0.1,30]];
for(const [n,ry,rx,rz,s] of G){await p.evaluate(a=>show(...a),[n,ry,rx,rz,s]);await p.screenshot({path:`../glyph_${n}.png`,omitBackground:true});}
await b.close();})();
