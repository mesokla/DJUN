import math,os
NOCAR=os.environ.get('NOCAR')=='1'
FG=os.environ.get('FG')=='1'
W,H,N=1080,1350,7
def yat(x): return 1060+38*math.sin(x/520+.6)+18*math.sin(x/210)+95*math.exp(-((x-(3*W+330))/330)**2)
LX=2*W+820; R=130
pts=[(x,yat(x)) for x in range(-1200,LX,8)]
y0=yat(LX); cy=y0-R
pts+=[(LX+R*math.sin(t/60*2*math.pi), cy+R*math.cos(t/60*2*math.pi)) for t in range(61)]
pts+=[(x,yat(x)) for x in range(LX+8,6*W+700,8)]
END=pts[-1]
d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)
CX=300; a=math.degrees(math.atan((yat(CX+5)-yat(CX-5))/10))
CAR=f'''<svg class="car" style="left:{CX-78}px;top:{yat(CX)-70}px;transform:rotate({a:.1f}deg)" width="156" height="73" viewBox="0 0 120 56">
<path d="M6,38 Q6,28 18,27 L34,25 Q44,10 60,9 L78,9 Q92,10 100,25 L110,28 Q116,30 116,38 L116,42 Q116,45 112,45 L10,45 Q6,45 6,42Z" fill="#190F09"/>
<path d="M40,25 Q48,14 60,14 L68,14 L68,25Z M73,14 L78,14 Q88,15 94,25 L73,25Z" fill="#F3EDE6"/>
<circle cx="32" cy="45" r="9" fill="#190F09" stroke="#F3EDE6" stroke-width="3"/><circle cx="92" cy="45" r="9" fill="#190F09" stroke="#F3EDE6" stroke-width="3"/></svg>'''
def note(x,y,t,rot=-4,size=52,w=None): return f'<div class="cv" style="left:{x}px;top:{y}px;transform:rotate({rot}deg);font-size:{size}px;{"width:%dpx"%w if w else ""}">{t}</div>'
def arrow(x,y,dpath,w=200,h=160): return f'<svg class="ar" style="left:{x}px;top:{y}px" width="{w}" height="{h}"><path d="{dpath}"/></svg>'
LOGO='<div class="logo"><img src="crest.svg" style="height:46px"><div class="w"><img src="letters.svg" style="height:19px"><small>AI академія</small></div></div>'
S=[]
S.append(LOGO)
S.append('''<div class="h" style="top:230px;font-size:84px">Скіл це<br>навик <span class="itx">для AI</span></div>
<div class="p" style="top:460px;width:480px">Ви один раз описуєте, як робити задачу. AI зберігає це й сам відкриває, щойно бачить схожу.</div>
<div class="card" style="left:600px;top:450px;transform:rotate(3deg)"><div class="mono" style="color:#A16E3B">skill.md</div><div style="font:800 32px/1.1 M;margin:14px 0 16px">Стиль презентацій</div><div class="mono" style="line-height:1.7;color:#5d5248">одна думка на слайд<br>до 6 рядків тексту<br>фірмові кольори</div></div>'''+note(640,790,'один файл, і AI<br>знає, як треба',-5,52))
S.append('''<div class="h" style="top:230px;font-size:84px">Більше не треба<br><span class="itx">повторювати</span></div>
<div style="position:absolute;left:72px;top:470px;display:flex;flex-direction:column;gap:12px">'''+''.join(f'<div class="old" style="opacity:{o}">Одна думка на слайд, до 6 рядків…</div>' for o in (1,.65,.4))+'''</div>'''+note(640,560,'і так у кожному<br>новому чаті',6,52)+'''<div class="new" style="left:72px;top:790px">Зроби презентацію ✓</div>''')
S.append('''<div class="h" style="top:230px;font-size:84px">Каталог прямо<br><span class="itx">в Claude</span></div>
<div class="p" style="top:450px;width:930px;font-size:33px">Плюсик у чаті → Skills → Переглянути. Там тисячі скілів за темами, серед них офіційні від Anthropic для Word, Excel, PowerPoint і PDF.</div>
<img class="ui" src="ui_menu.png" style="left:72px;top:620px;width:460px;transform:rotate(-2deg)">
<img class="ui" src="ui_catalog.png" style="left:590px;top:600px;width:400px;transform:rotate(2deg)">
<div class="ring" style="left:96px;top:790px;width:270px;height:62px"></div>'''+note(600,975,'ось тут',-4,56)+arrow(420,860,'M170,130 C120,120 60,80 20,20 M14,46 L20,20 L44,28',190,150))
S.append('''<div class="h" style="top:230px;font-size:84px">Маркетплейс<br><span class="itx">скілів</span></div>
<div class="p" style="top:460px;width:470px">На сайті skillsmp.com зібрали понад 4 мільйони скілів. Шукаєте за задачею, читаєте опис, завантажуєте.</div>
<img class="ui" src="ui_mp.png" style="left:590px;top:420px;width:420px;transform:rotate(3deg)">
<div class="ring" style="left:600px;top:810px;width:250px;height:80px;transform:rotate(1deg)"></div>'''+note(330,830,'4 мільйони!',-6,56)+arrow(470,840,'M10,40 C60,20 100,20 130,30 M112,16 L132,30 L112,44',150,70))
S.append('''<div class="h" style="top:230px;font-size:84px">GitHub.<br><span class="itx">Але обережно</span></div>
<div class="p" style="top:460px;width:500px">Більшість цих мільйонів зібрали саме звідти, а викласти на GitHub може будь-хто. Разом зі скілом легко завантажити шкідливий код.</div>
<div class="sticky" style="left:620px;top:450px"><div class="cv" style="position:static;font-size:48px;line-height:1.25">перед тим як<br>встановити:<br><br>✓ хто автор?<br>✓ що всередині?<br>✗ просить паролі?<br>&nbsp;&nbsp;&nbsp;не беремо</div></div>''')
S.append('''<div class="h" style="top:230px;font-size:84px">Скіл під<br><span class="itx">ваш процес</span></div>
<div class="p" style="top:460px;width:470px">Створіть його самі, без коду: Skills → Додати → Створити з Claude. Опишіть задачу, а Claude сам складе файл скіла.</div>
<img class="ui" src="ui_add.png" style="left:600px;top:470px;width:400px;transform:rotate(-2deg)">
<div class="ring" style="left:618px;top:665px;width:330px;height:66px;transform:rotate(-3deg)"></div>
<div class="h" style="top:1180px;font-size:40px;line-height:1">Збережіть, <span class="itx" style="font-size:44px">щоб не загубити</span></div>''')
body=''.join(f'<section style="left:{i*W}px'+(';background:url(cover_bg.png) center/cover' if i==0 else '')+f'">{s}</section>' for i,s in enumerate(S))
html=f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:M;src:url(Montserrat.ttf)}}@font-face{{font-family:J;src:url(JetBrainsMono.ttf)}}
@font-face{{font-family:C;src:url(cav-cyrillic.woff2);unicode-range:U+0400-04FF}}@font-face{{font-family:C;src:url(cav-latin.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+2190-21FF,U+2713-2717}}
@font-face{{font-family:Li;src:url(lora-cyrillic.woff2);unicode-range:U+0400-04FF}}@font-face{{font-family:Li;src:url(lora-latin.woff2);unicode-range:U+0000-00FF,U+2000-206F}}
*{{margin:0;box-sizing:border-box}}body{{width:{W*N}px;height:{H}px;position:relative;overflow:hidden;font-family:M;color:#190F09;background:#F3EDE6 url(grain.png)}}
section{{position:absolute;top:0;width:{W}px;height:{H}px}}
.logo{{position:absolute;top:70px;left:72px;display:flex;align-items:center;gap:12px}}.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}.logo small{{font:700 11px/1 M;letter-spacing:.2em;margin-top:6px;margin-right:-.2em;color:#A16E3B}}
.h{{position:absolute;left:72px;font-weight:800;letter-spacing:-.045em;line-height:1}}
.it{{position:absolute;left:72px;font-family:Li;font-style:italic;font-weight:500;color:#A16E3B;letter-spacing:-.02em;line-height:1}}
.itx{{font-family:Li;font-style:italic;font-weight:500;color:#A16E3B;letter-spacing:-.02em}}
.p{{position:absolute;left:72px;font:500 34px/1.42 M;color:#3b2e24}}
.cv{{position:absolute;font-family:C;font-weight:600;color:#A16E3B;line-height:1.05}}
.ar{{position:absolute;overflow:visible}}.ar path{{fill:none;stroke:#A16E3B;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}}
.card{{position:absolute;width:390px;background:#fff;border-radius:18px;box-shadow:0 18px 40px rgba(25,15,9,.08);padding:30px 32px}}.mono{{font:500 23px/1.3 J}}
.old{{background:#fff;color:#9c8f82;border-radius:18px;padding:18px 24px;font:600 27px/1.2 M;text-decoration:line-through;text-decoration-color:#A16E3B;text-decoration-thickness:3px;width:560px}}
.new{{position:absolute;background:#190F09;color:#F3EDE6;border-radius:18px;padding:22px 30px;font:800 42px/1 M}}
.ui{{position:absolute;border-radius:18px;box-shadow:0 22px 50px rgba(25,15,9,.22)}}
.ring{{position:absolute;border:4px solid #A16E3B;border-radius:50%;transform:rotate(-2deg)}}
.sticky{{position:absolute;width:380px;background:#FBF6EF;border-radius:6px;padding:34px 34px;box-shadow:0 14px 34px rgba(25,15,9,.12);transform:rotate(3deg)}}
.car{{position:absolute;z-index:5;transform-origin:78px 70px}}
</style>

{body}<svg style="position:absolute;z-index:2;left:0;top:0" width="{W*N}" height="{H}"><path d="{d}" fill="none" stroke="#A16E3B" stroke-width="6" stroke-dasharray="0 17" stroke-linecap="round" opacity=".75"/><clipPath id="c0"><rect x="0" y="0" width="1080" height="1350"/></clipPath><path d="{d}" clip-path="url(#c0)" fill="none" stroke="#F3EDE6" stroke-width="6" stroke-dasharray="0 17" stroke-linecap="round"/><circle cx="{END[0]}" cy="{END[1]}" r="11" fill="#A16E3B"/></svg>'''+('' if NOCAR else CAR)
if FG:
    html=html.replace('</style>','body{background:none!important}body *{visibility:hidden}section:first-child .ui,section:first-child .ring,section:nth-child(4) .ui,section:nth-child(4) .ring,section:nth-child(4) .ar,section:nth-child(4) .cv{visibility:visible}</style>')
open('pano.html','w').write(html)
