import math
W,H,N=1080,1350,7
# path points: wavy line across the panorama
pts=[]
for x in range(-40,W*N+41,20):
    y=1110+95*math.sin(x/430)+40*math.sin(x/170+1)
    pts.append((x,y))
d='M'+' L'.join(f'{x:.0f},{y:.0f}' for x,y in pts)
def yat(x): return 1110+95*math.sin(x/430)+40*math.sin(x/170+1)
def slope(x): return (yat(x+5)-yat(x-5))/10
CH=[(i*W+[820,300,820,880,300,870,560][i]) for i in range(N)]
chev=''.join(f'<img src="glyph_chev.png" style="position:absolute;left:{x-90:.0f}px;top:{yat(x)-120:.0f}px;height:240px;transform:rotate({math.degrees(math.atan(slope(x))):.0f}deg);filter:drop-shadow(0 20px 30px rgba(25,15,9,.3))">' for x in CH)
logo='<div class="logo" style="left:{x}px"><img src="crest.svg" style="height:48px"><div class="w"><img src="letters.svg" style="height:20px"><small>AI академія</small></div></div><div class="pg" style="left:{px}px">{n}/7</div>'
L=''.join(logo.format(x=i*W+72,px=i*W+960,n=i+1) for i in range(N))
def at(i,s): return s.replace('LEFT',str(i*W+72)).replace('RIGHTW',str(W-144))
C=[]
C.append(at(0,'''<div class="h" style="left:LEFTpx;top:300px;font-size:120px">AI-скіли:</div>
<div class="h br" style="left:LEFTpx;top:430px;font-size:96px">що це і де<br>їх брати</div>
<div class="p" style="left:LEFTpx;top:700px;width:760px">І чому з ними AI нарешті робить так, як треба саме вам.</div>
<div class="sw" style="left:LEFTpx">гортайте →</div>'''))
C.append(at(1,'''<div class="k" style="left:LEFTpx;top:250px">ЩО ЦЕ</div><div class="h" style="left:LEFTpx;top:290px;font-size:96px">Скіл це <span class="br">навик</span><br>для AI</div>
<div class="p" style="left:LEFTpx;top:540px;width:470px">Ви один раз описуєте, як робити задачу. AI зберігає це й сам відкриває, щойно бачить схожу.</div>
<div class="card" style="left:''' + str(1*W+600) + '''px;top:520px;transform:rotate(3deg)"><div style="display:flex;align-items:center;gap:14px"><div class="md">.md</div><div><b style="font:800 30px/1 M">Стиль постів</b><div style="font:500 20px/1.3 J;color:#8a7f73;margin-top:6px">skill.md</div></div></div><div style="font:500 22px/1.6 J;color:#5d5248;margin-top:18px">коротко, на «ви»<br>без емодзі<br>теплий тон</div></div>'''))
C.append(at(2,'''<div class="k" style="left:LEFTpx;top:250px">НАВІЩО</div><div class="h" style="left:LEFTpx;top:290px;font-size:88px">Більше не треба<br><span class="br">повторювати</span></div>
<div style="position:absolute;left:LEFTpx;top:540px;width:560px;display:flex;flex-direction:column;gap:12px">''' + ''.join(f'<div class="old" style="opacity:{o}">Пиши коротко, на «ви», без емодзі…</div>' for o in (1,.7,.45)) + '''</div>
<div class="new" style="left:LEFTpx;top:820px">Зроби пост ✓</div>'''))
C.append(at(3,'''<div class="k" style="left:LEFTpx;top:250px">ДЕ БРАТИ · 01</div><div class="h" style="left:LEFTpx;top:290px;font-size:92px">Готові скіли<br><span class="br">від Anthropic</span></div>
<div class="p" style="left:LEFTpx;top:540px;width:700px">Компанія, яка робить Claude, має офіційні скіли для документів, презентацій, таблиць і PDF. Вмикаються в налаштуваннях.</div>
<div style="position:absolute;left:LEFTpx;top:800px;display:flex;gap:14px">''' + ''.join(f'<div class="chip">{x}</div>' for x in ('DOCX','PPTX','XLSX','PDF')) + '</div>'))
C.append(at(4,'''<div class="k" style="left:LEFTpx;top:250px">ДЕ БРАТИ · 02</div><div class="h" style="left:LEFTpx;top:290px;font-size:92px">Каталоги,<br>де <span class="br">діляться</span></div>
<div class="p" style="left:LEFTpx;top:540px;width:820px">Люди викладають скіли під різні задачі. Знайшли потрібний, завантажили, додали собі.</div>
<div style="position:absolute;left:LEFTpx;width:900px;top:720px;display:flex;flex-wrap:wrap;gap:14px">''' + ''.join(f'<span class="tag" style="{s}">{x}</span>' for x,s in (('маркетинг','background:#190F09;color:#EFE7DF'),('аналітика',''),('дизайн','background:#fff;border-color:#fff'),('продажі',''),('контент','background:#A16E3B;color:#fff;border-color:#A16E3B'),('ваша задача','border-style:dashed'))) + '</div>'))
C.append(at(5,'''<div class="k" style="left:LEFTpx;top:250px">ДЕ БРАТИ · 03</div><div class="h" style="left:LEFTpx;top:290px;font-size:92px">GitHub.<br><span class="br">Але обережно</span></div>
<div class="p" style="left:LEFTpx;top:540px;width:520px">Скілів тут найбільше, бо викласти може будь-хто. Разом зі скілом можна завантажити шкідливий код.</div>
<div class="warn" style="left:''' + str(5*W+600) + '''px;top:500px"><b>Перед встановленням</b><div>✓ хто автор<br>✓ що всередині<br>✗ жодних паролів</div></div>'''))
C.append(at(6,'''<div class="k" style="left:LEFTpx;top:250px">А НАЙКРАЩЕ</div><div class="h" style="left:LEFTpx;top:290px;font-size:100px">Скіл під<br><span class="br">ваш процес</span></div>
<div class="p" style="left:LEFTpx;top:560px;width:720px">Його можна зробити самостійно. Як саме, покажемо в наступному пості.</div>
<div class="h" style="left:LEFTpx;top:1250px;font-size:44px;line-height:1">Підпишіться, <span class="br">щоб не пропустити</span></div>'''))
html=f'''<!doctype html><meta charset="utf-8"><style>@font-face{{font-family:M;src:url(Montserrat.ttf)}}@font-face{{font-family:J;src:url(JetBrainsMono.ttf)}}
*{{margin:0;box-sizing:border-box}}body{{width:{W*N}px;height:{H}px;position:relative;overflow:hidden;font-family:M;color:#190F09;background:linear-gradient(180deg,#F4EEE7,#ECE3D8)}}
.logo{{position:absolute;top:64px;display:flex;align-items:center;gap:12px}}.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}.logo small{{font:700 11px/1 M;letter-spacing:.2em;margin-top:6px;margin-right:-.2em;color:#A16E3B}}
.pg{{position:absolute;top:78px;font:500 22px/1 J;color:#8a7f73}}
.h{{position:absolute;font-weight:800;letter-spacing:-.045em;line-height:1}}.br{{color:#A16E3B}}
.p{{position:absolute;font:500 36px/1.4 M;color:#3b2e24}}.k{{position:absolute;font:800 28px/1 J;color:#A16E3B;letter-spacing:.05em}}
.sw{{position:absolute;top:1250px;font:700 32px/1 M;color:#A16E3B}}
.card{{position:absolute;width:400px;background:#fff;border-radius:26px;box-shadow:0 20px 50px rgba(25,15,9,.1);padding:30px 32px}}
.md{{width:56px;height:68px;border-radius:10px;background:#190F09;color:#F2D29A;font:800 20px/68px J;text-align:center}}
.old{{background:#fff;color:#9c8f82;border-radius:22px;padding:18px 24px;font:600 28px/1.2 M;text-decoration:line-through;text-decoration-color:#A16E3B;text-decoration-thickness:3px}}
.new{{position:absolute;background:#190F09;color:#EFE7DF;border-radius:26px;padding:24px 32px;font:800 44px/1 M}}
.chip{{font:800 36px/1 J;padding:26px 28px;border-radius:22px;background:#190F09;color:#F2D29A}}
.tag{{font:700 32px/1 M;padding:20px 26px;border-radius:999px;border:3px solid #A16E3B;color:#714326}}
.warn{{position:absolute;width:400px;background:#190F09;color:#EFE7DF;border-radius:28px;padding:34px 34px}}.warn b{{display:block;font:800 30px/1.1 M;color:#F2D29A;margin-bottom:18px}}.warn div{{font:600 32px/1.6 M}}
</style>
<svg style="position:absolute;left:0;top:0" width="{W*N}" height="{H}"><path d="{d}" fill="none" stroke="#C99662" stroke-width="5" stroke-dasharray="4 16" stroke-linecap="round"/></svg>
{L}{''.join(C)}{chev}'''
open('pano.html','w').write(html)
