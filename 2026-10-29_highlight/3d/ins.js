const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage();p.on('console',m=>console.log(m.text()));
await p.goto('http://127.0.0.1:8765/inspect.html');await p.waitForFunction(()=>document.title==='done',null,{timeout:20000});console.log(JSON.stringify(await p.evaluate(()=>window.R)));await b.close();})();
