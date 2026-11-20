import random
HEAD='''<!doctype html><meta charset="utf-8"><style>
@font-face{font-family:Cav;src:url(caveat-cyrillic-700-normal.woff2);unicode-range:U+0400-04FF}@font-face{font-family:Cav;src:url(caveat-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+2190-21FF}
@font-face{font-family:Neu;src:url(neucha-cyrillic-400-normal.woff2);unicode-range:U+0400-04FF}@font-face{font-family:Neu;src:url(neucha-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+2190-21FF}
@font-face{font-family:Bad;src:url(bad-script-cyrillic-400-normal.woff2);unicode-range:U+0400-04FF}@font-face{font-family:Bad;src:url(bad-script-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+2190-21FF}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;position:relative;overflow:hidden;color:#231c17}
body.K{background:url(bg_kraft.jpg)} body.P{background:url(bg_clip.jpg)}
.a{position:absolute}
.cav{font-family:Cav;line-height:.95}.neu{font-family:Neu;line-height:1.25}.bad{font-family:Bad;line-height:1.3}
.br{color:#8C5A2B}.rd{color:#A8432C}
.scrap{position:absolute;background:#F7F2E8;padding:26px 34px;box-shadow:0 8px 18px rgba(60,40,20,.18)}
.tape{position:absolute;width:120px;height:38px;background:rgba(235,225,200,.75);box-shadow:0 1px 3px rgba(0,0,0,.08)}
svg#rough{position:absolute;left:0;top:0;pointer-events:none}
.ink{mix-blend-mode:multiply}
</style><script src="rough.js"></script><body class="%s">'''
TAIL='''<svg id="rough" width="1080" height="1350"></svg><script>
document.fonts.ready.then(()=>{const svg=document.getElementById('rough');const rc=rough.svg(svg);
const O=(o)=>Object.assign({roughness:1.4,bowing:1.2,stroke:'#231c17',strokeWidth:3},o||{});
function R(el){return el.getBoundingClientRect()}
document.querySelectorAll('[data-u]').forEach(el=>{const r=R(el);const c=el.dataset.u||'#8C5A2B';svg.appendChild(rc.line(r.left,r.bottom+4,r.right,r.bottom+2,O({stroke:c,strokeWidth:4})));svg.appendChild(rc.line(r.left+20,r.bottom+12,r.right-30,r.bottom+10,O({stroke:c,strokeWidth:3})))});
document.querySelectorAll('[data-c]').forEach(el=>{const r=R(el);svg.appendChild(rc.ellipse((r.left+r.right)/2,(r.top+r.bottom)/2,r.width+40,r.height+26,O({stroke:el.dataset.c||'#8C5A2B',strokeWidth:3})))});
document.querySelectorAll('[data-x]').forEach(el=>{const r=R(el);svg.appendChild(rc.line(r.left-6,(r.top+r.bottom)/2+3,r.right+6,(r.top+r.bottom)/2-2,O({stroke:'#A8432C',strokeWidth:4})))});
document.querySelectorAll('[data-box]').forEach(el=>{const r=R(el);const x=r.left-58,y=r.top+(r.height-34)/2;svg.appendChild(rc.rectangle(x,y,34,34,O({strokeWidth:3})));svg.appendChild(rc.linearPath([[x+6,y+16],[x+15,y+28],[x+40,y-8]],O({stroke:'#8C5A2B',strokeWidth:4})))});
document.querySelectorAll('[data-ar]').forEach(el=>{const p=el.dataset.ar.split(',').map(Number);const [x1,y1,x2,y2]=p;svg.appendChild(rc.curve([[x1,y1],[(x1+x2)/2+(p[4]||0),(y1+y2)/2+(p[5]||0)],[x2,y2]],O({stroke:'#8C5A2B',strokeWidth:3.5})));const a=Math.atan2(y2-((y1+y2)/2+(p[5]||0)),x2-((x1+x2)/2+(p[4]||0)));for(const d of [2.6,-2.6]){svg.appendChild(rc.line(x2,y2,x2+22*Math.cos(a+d),y2+22*Math.sin(a+d),O({stroke:'#8C5A2B',strokeWidth:3.5})))}});
document.querySelectorAll('.scrap').forEach(el=>{let pts=[];const n=18;for(let i=0;i<=n;i++)pts.push(`${i/n*100}% ${Math.random()*4}%`);for(let i=0;i<=n;i++)pts.push(`${100-Math.random()*1.5}% ${i/n*100}%`);for(let i=n;i>=0;i--)pts.push(`${i/n*100}% ${100-Math.random()*4}%`);for(let i=n;i>=0;i--)pts.push(`${Math.random()*1.5}% ${i/n*100}%`);el.style.clipPath=`polygon(${pts.join(',')})`});document.body.dataset.done=1});
</script>'''
def page(cls,body): return HEAD%cls+body+TAIL
def scrap(x,y,w,txt,rot,size=50,tape=True,cls='neu'):
    t=f'<div class="tape" style="left:{x+w/2-60}px;top:{y-16}px;transform:rotate({rot*-3:.0f}deg)"></div>' if tape else ''
    return f'<div class="scrap {cls}" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);font-size:{size}px">{txt}</div>'+t
def ce(sub,note):  # bad-slide frame
    return f'''<div class="a cav" style="left:80px;top:90px;font-size:300px">Це</div>
<div class="a bad br" style="left:560px;top:230px;font-size:64px;transform:rotate(-8deg)">{note}</div>
<div class="a cav" style="left:300px;top:1060px;font-size:230px">нудно…</div>'''
S=[]
# 1
S.append(page('K',ce('','zzz…')+
 scrap(90,470,760,'Напиши комерційну пропозицію',-3)+scrap(230,650,760,'Напиши комерційну пропозицію',2)+scrap(120,830,760,'Напиши комерційну пропозицію',-1.5)+
 '<div class="a bad rd" style="left:720px;top:990px;font-size:40px;transform:rotate(-6deg)">і знову вода<br>у відповідь</div>'))
# 2
items=[('роль','«ти B2B-маркетолог з 10 роками досвіду»'),('аудиторія','«фінансові директори виробничих компаній»'),('формат','«1 сторінка, три пакети з цінами»'),('тон','«діловий, без пафосу»'),('приклад','«ось КП, яке закрило угоду в жовтні»'),('чого не писати','«жодних “інноваційних рішень”»')]
li=''.join(f'<div style="margin:0 0 22px 60px"><span class="neu" data-box style="font-size:44px">{a}</span><div class="bad br" style="font-size:31px;margin-top:2px">{b}</div></div>' for a,b in items)
S.append(page('P','''<div class="a cav" style="left:190px;top:255px;font-size:94px;transform:rotate(-2deg)"><span data-u>Додайте в промпт:</span></div>
<div class="a" style="left:190px;top:420px;width:720px">'''+li+'''</div>
<div class="a bad" style="left:420px;top:1150px;font-size:34px;transform:rotate(-3deg)">і отримаєте КП, яке<br>не соромно надіслати</div><i data-ar="350,1110,410,1180,-40,20"></i>'''))
# 3
S.append(page('K',ce('','знову…')+
 scrap(90,520,260,'CRM',-4,54)+scrap(400,560,280,'таблиця',3,54)+scrap(720,520,280,'звіт у пошту',-2,46)+
 '<div class="a bad rd" style="left:250px;top:720px;font-size:34px;transform:rotate(4deg)">Ctrl+C<br>Ctrl+V</div><div class="a bad rd" style="left:600px;top:730px;font-size:34px;transform:rotate(-3deg)">Ctrl+C<br>Ctrl+V</div>'
 '<div class="a neu" style="left:150px;top:880px;font-size:46px;transform:rotate(-1.5deg)">щоп\'ятниці, <span data-c="#A8432C">2 години</span> вручну</div>'))
# 4
svc=['Google Drive','Gmail','Календар','Notion','Slack','CRM']
sv=''.join(f'<span class="neu" style="display:inline-block;font-size:52px;margin:0 44px 30px 0;transform:rotate({random.Random(i).uniform(-3,3):.1f}deg)" {"data-c" if i in (1,5) else ""}>{s}</span>' for i,s in enumerate(svc))
ex=['збирає звіт з продажів прямо з таблиці','пише чернетки відповідей клієнтам','перед зустріччю нагадує, з ким і про що домовлялись']
exl=''.join(f'<div class="neu" data-box style="font-size:42px;margin:0 0 26px 60px">{e}</div>' for e in ex)
S.append(page('P','''<div class="a cav" style="left:190px;top:250px;font-size:110px;transform:rotate(-2deg)"><span data-u>Підключіть:</span></div>
<div class="a" style="left:200px;top:420px;width:700px">'''+sv+'''</div>
<div class="a bad br" style="left:200px;top:690px;font-size:46px;transform:rotate(-2deg)">і AI сам:</div>
<div class="a" style="left:200px;top:790px;width:700px">'''+exl+'</div>'))
# 5
intro='Ми B2B-логістика, клієнти з e-commerce, тон діловий, без англіцизмів…'
S.append(page('K',ce('','вдесяте…')+
 scrap(80,450,760,intro,-2.5,40)+scrap(230,640,760,intro,2,40)+scrap(110,830,760,intro,-1,40)+
 '<div class="a bad rd" style="left:770px;top:1000px;font-size:40px;transform:rotate(-7deg)">і так у кожному<br>новому чаті</div>'))
# 6
sv2=[('власні інструкції','хто ви і як із вами працювати'),('Проєкти','документи й контекст однієї задачі'),('скіли','інструкції для задач, які повторюються'),('пам\'ять','AI пам\'ятає попередні розмови')]
l2=''.join(f'<div style="margin:0 0 18px 60px"><span class="neu" data-box style="font-size:44px">{a}</span><div class="bad br" style="font-size:30px">{b}</div></div>' for a,b in sv2)
S.append(page('P','''<div class="a cav" style="left:190px;top:250px;font-size:110px;transform:rotate(-2deg)"><span data-u>Збережіть:</span></div>
<div class="a" style="left:190px;top:420px;width:740px">'''+l2+'''</div>
<div class="a neu" style="left:200px;top:905px;font-size:38px;transform:rotate(1deg)"><span class="br">Ви:</span> «Підготуй апдейт для клієнта»</div>
<div class="a neu" style="left:200px;top:975px;width:700px;font-size:38px;transform:rotate(-1deg)"><span class="br">AI:</span> Готово. Діловим тоном, з цифрами за тиждень і наступними кроками.</div>
<div class="a bad" style="left:220px;top:1140px;font-size:34px;transform:rotate(-2deg)">і пояснювати нічого не треба</div>'''))
# 7
S.append(page('P','''<div class="a cav" style="left:190px;top:310px;font-size:118px;line-height:.95;transform:rotate(-2deg)">AI нудний,<br><span class="br">поки ви його<br>не налаштуєте</span></div>
<div class="a neu" style="left:200px;top:760px;width:680px;font-size:40px">Контекст у промпті, підключені сервіси, збережені налаштування. І AI працює на вас.</div>
<div class="a bad br" style="left:200px;top:1010px;font-size:36px;transform:rotate(-3deg)"><span data-u="#8C5A2B">збережіть, щоб спробувати</span></div>
<div class="a ink" style="left:700px;top:1110px;display:flex;align-items:center;gap:10px;opacity:.85;transform:rotate(-6deg)"><img src="crest.svg" style="height:56px"><img src="letters.svg" style="height:22px"></div>'''))
for i,h in enumerate(S,1): open(f'slide_{i}.html','w').write(h)
