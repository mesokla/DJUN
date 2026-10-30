const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});
for(const n of ['avatar_crest','avatar_crest_word']){await p.goto('file://'+process.cwd()+`/${n}.html`);await p.waitForTimeout(300);await p.screenshot({path:`${n}.png`});}await b.close();})();
