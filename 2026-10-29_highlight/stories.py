CSS='''@font-face{font-family:M;src:url(Montserrat.ttf)}@font-face{font-family:J;src:url(JetBrainsMono.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:M;color:#EFE7DF}
.bg{position:absolute;inset:0;background:radial-gradient(70% 40% at 30% 40%,#3d2c1a 0%,#24190f 45%,#140e08 80%,#0e0905 100%)}
.dots{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(217,180,140,.7) 1.8px,transparent 2.4px);background-size:48px 48px;-webkit-mask:radial-gradient(70% 45% at 35% 42%,#000 0%,rgba(0,0,0,.5) 55%,rgba(0,0,0,.18) 100%)}
.logo{position:absolute;top:250px;left:80px;display:flex;align-items:center;gap:16px}
.logo .w{display:flex;flex-direction:column;align-items:flex-end}.logo small{font:700 14px/1 M;letter-spacing:.2em;color:#D2A26C;margin-top:7px;margin-right:-.2em}
.k{font:500 30px/1 J;color:#D2A26C;margin-bottom:28px}
h1{font-weight:800;font-size:96px;line-height:1;letter-spacing:-.035em}
h1 em,h2 em,b em{font-style:normal;color:#D2A26C}
.c{position:absolute;left:80px;right:80px;top:430px}
p{font:500 38px/1.38 M;color:#E4D8CB;margin-top:34px}
p.m{color:#B9A897;font-size:34px}
.glyph{position:absolute;filter:drop-shadow(0 30px 50px rgba(0,0,0,.55))}
.blk{margin-top:44px;padding-top:30px;border-top:2px solid rgba(210,162,108,.55)}
.blk h2{font-weight:800;font-size:56px;line-height:1.05;letter-spacing:-.02em}
.blk p{margin-top:14px}
.it{display:flex;gap:26px;padding:30px 0;border-bottom:1px solid rgba(239,231,223,.14)}
.it i{font:500 30px/1.3 J;font-style:normal;color:#D2A26C;min-width:56px;padding-top:6px}
.it b{display:block;font-weight:800;font-size:44px;line-height:1.1;letter-spacing:-.02em}
.it span{display:block;font:500 31px/1.35 M;color:#C9B8A6;margin-top:8px}
.list{margin-top:40px;border-top:2px solid rgba(210,162,108,.55)}
.foot{position:absolute;left:80px;right:80px;font:500 28px/1.3 J;color:#D2A26C}
'''
LOGO='<div class="logo"><img src="crest_light.svg" style="height:70px"><div class="w"><img src="letters_light.svg" style="height:29px"><small>AI академія</small></div></div>'
def page(body,glyph,gs,script=''):
    return f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div class="bg"></div><div class="dots"></div><img class="glyph" src="glyph_{glyph}.png" style="{gs}">{LOGO}{body}{script}'
S={}
S['story_2']=page('''<div class="c"><div class="k">// хто ми</div><h1>Джун.<br><em>AI академія</em></h1>
<p>Вчимо працювати з AI так, щоб він вирішував реальні задачі: у роботі, у власній справі, у творчості.</p>
<p class="m">Поєднуємо освіту й експертний досвід. Вчать практики, які самі щодня працюють з AI.</p></div>
<div class="foot" style="top:1440px">8+ років в освіті · сотні випускників</div>''','brace','right:-90px;bottom:-60px;height:700px;opacity:.95')
S['story_3']=page('''<div class="c"><div class="k">// для кого</div><h1>Кому<br><em>до нас</em></h1>
<div class="blk"><h2>Спеціалістам</h2><p>Від першого промпту до власного стилю, портфоліо й навички, яка допомагає заробляти.</p></div>
<div class="blk"><h2>Бізнесу</h2><p>Знаходимо, де AI створить цінність у маркетингу, продажах і процесах, і робимо план дій.</p></div></div>
<div class="foot" style="top:1500px">// програмувати вміти не потрібно</div>''','O','right:-170px;bottom:-40px;height:560px;opacity:.95')
S['story_5']=page('''<div class="c"><div class="k">// що в нас є</div><h1>Тут<br><em>буде цікаво</em></h1>
<div class="list">
<div class="it"><i>01</i><div><b>Курси й інтенсиви</b><span>з різних напрямів AI</span></div></div>
<div class="it"><i>02</i><div><b>Кейси</b><span>AI у маркетингу, продажах і процесах</span></div></div>
<div class="it"><i>03</i><div><b>Розбори</b><span>інструменти й промпти, які працюють</span></div></div>
<div class="it"><i>04</i><div><b>Анонси</b><span>нові курси й зустрічі наживо</span></div></div></div></div>
''','chev','right:-120px;bottom:-30px;height:520px;opacity:.95')
S4='''<div class="c"><div class="k">// наш підхід</div><h1>Як ми<br><em>навчаємо</em></h1>
<div class="list">
<div class="it a" id="a0"><i>01</i><div><b>Практика, а не теорія</b><span>Кожен курс закінчується реальним результатом</span></div></div>
<div class="it a" id="a1"><i>02</i><div><b>Наживо + записи</b><span>Зустрічі з ментором і уроки у своєму темпі</span></div></div>
<div class="it a" id="a2"><i>03</i><div><b>Ментори-практики</b><span>Ті, хто вже використовує AI у своїй роботі</span></div></div>
<div class="it a" id="a3"><i>04</i><div><b>Чесно про AI</b><span>Він не зробить усе за вас, але зробить те, що ви чітко пояснили</span></div></div></div></div>'''
SCR='''<script>const cl=x=>Math.max(0,Math.min(1,x)),eo=x=>1-Math.pow(1-cl(x),3);
window.render=function(t){const h=document.querySelector('.c h1'),k=document.querySelector('.k'),L=document.querySelector('.list'),g=document.querySelector('.glyph');
 const a=eo(t/0.6);k.style.opacity=a;h.style.opacity=eo((t-0.15)/0.6);h.style.transform=`translateY(${40*(1-eo((t-0.15)/0.6))}px)`;
 L.style.borderTopColor=`rgba(210,162,108,${.55*eo((t-0.6)/0.5)})`;
 for(let i=0;i<4;i++){const e=document.getElementById('a'+i);const p=eo((t-1.0-i*0.9)/0.6);e.style.opacity=p;e.style.transform=`translateX(${-60*(1-p)}px)`;
  e.querySelector('i').style.color=(t>1.0+i*0.9&&t<1.0+i*0.9+0.9)?'#F2C48D':'#D2A26C';}
 const gp=eo((t-0.2)/1.2);g.style.opacity=.95*gp;g.style.transform=`translateY(${120*(1-gp)}px) rotate(${-8*(1-gp)+Math.sin(t*1.2)*2}deg)`;};
render(0);document.title='ready';</script>'''
S['story_4']=page(S4,'hash','right:-140px;bottom:-60px;height:560px;opacity:.95',SCR)
for k,v in S.items(): open(k+'.html','w').write(v)
