const {chromium}=require('playwright');(async()=>{const [html,out,dur,only]=process.argv.slice(2);const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('console',m=>console.log('C:',m.text()));p.on('pageerror',e=>console.log('E:',e.message));
await p.goto('http://127.0.0.1:8765/'+html);await p.waitForFunction(()=>document.title==='ready',null,{timeout:60000});
const fps=30;const frames=only?only.split(',').map(Number):[...Array(Math.round(fps*parseFloat(dur))).keys()];
for(const i of frames){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`${out}/f${String(i).padStart(4,'0')}.png`});}await b.close();})();
