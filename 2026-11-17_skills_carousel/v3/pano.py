import math
W,H,N=1080,1350,7
TH=['D','L','L','L','L','L','D']
def yat(x): return 1190+55*math.sin(x/430)+25*math.sin(x/170+1)
def ang(x): return math.degrees(math.atan((yat(x+6)-yat(x-6))/12))
d='M'+' L'.join(f'{x},{yat(x):.1f}' for x in range(-60,W*N+61,12))
CAR='''<svg viewBox="0 0 330 150" width="330" height="150"><defs><linearGradient id="cb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E2B57E"/><stop offset=".55" stop-color="#B07A45"/><stop offset="1" stop-color="#7A4F2A"/></linearGradient></defs>
<g stroke="#C99662" stroke-width="6" stroke-linecap="round" opacity=".7"><line x1="-70" y1="70" x2="-15" y2="70"/><line x1="-100" y1="92" x2="-25" y2="92"/><line x1="-55" y1="114" x2="-12" y2="114"/></g>
<path d="M14,98 Q14,72 44,68 L96,63 Q126,28 166,25 L222,25 Q254,27 280,62 L304,68 Q322,72 322,96 L322,108 Q322,116 312,116 L22,116 Q14,116 14,106 Z" fill="url(#cb)"/>
<path d="M110,63 Q134,38 166,35 L192,35 L192,63 Z" fill="#190F09"/><path d="M202,35 L222,35 Q246,37 266,63 L202,63 Z" fill="#190F09"/>
<path d="M120,58 Q138,42 160,40" stroke="#F2D29A" stroke-width="3" fill="none" opacity=".5"/>
<line x1="197" y1="66" x2="197" y2="110" stroke="#6b4426" stroke-width="3"/><rect x="214" y="76" width="22" height="5" rx="2.5" fill="#6b4426"/>
<path d="M30,86 L300,86" stroke="#F2D29A" stroke-width="4" opacity=".55"/>
<ellipse cx="314" cy="82" rx="7" ry="9" fill="#FFE8B8"/><rect x="14" y="80" width="9" height="12" rx="3" fill="#C2452D"/>
<circle cx="82" cy="116" r="28" fill="#190F09"/><circle cx="82" cy="116" r="12" fill="#D6AA72"/><circle cx="256" cy="116" r="28" fill="#190F09"/><circle cx="256" cy="116" r="12" fill="#D6AA72"/></svg>'''
CX=[i*W+x for i,x in enumerate([700,520,640,880,560,620,860])]
cars=''.join(f'<div class="car" style="left:{x-170}px;top:{yat(x)-150}px;transform:rotate({ang(x):.1f}deg)">{CAR}</div>' for x in CX)
bg=''.join(f'<div class="bg {t}" style="left:{i*W}px"></div>' for i,t in enumerate(TH))
def logo(i):
    l='_light' if TH[i]=='D' else ''
    return f'<div class="logo" style="left:{i*W+72}px"><img src="crest{l}.svg" style="height:48px"><div class="w"><img src="letters{l}.svg" style="height:20px"><small>AI академія</small></div></div><div class="pg {TH[i]}" style="left:{i*W+940}px">{i+1}/7</div>'
L=''.join(logo(i) for i in range(N)).replace('>1/7<','><',1)
def at(i,s): return s.replace('LEFT',str(i*W+72)).replace('XX',str(i*W))
S=[]
S.append(at(0,'''<div class="h" style="left:LEFTpx;top:300px;font-size:150px;color:#EFE7DF">AI-скіли:</div>
<div class="h gold" style="left:LEFTpx;top:470px;font-size:108px;padding-bottom:10px">що це і де<br>їх брати</div>
<div class="p" style="left:LEFTpx;top:740px;width:760px;color:#d9cbbb">І чому з ними AI нарешті робить так, як треба саме вам.</div>'''))
S.append(at(1,'''<div class="k" style="left:LEFTpx;top:250px">ЩО ЦЕ</div><div class="h" style="left:LEFTpx;top:290px;font-size:96px">Скіл це <span class="br">навик</span><br>для AI</div>
<div class="p" style="left:LEFTpx;top:540px;width:470px">Ви один раз описуєте, як робити задачу. AI зберігає це й сам відкриває, щойно бачить схожу.</div>
<div class="card" style="left:XX+600px;top:520px;transform:rotate(3deg)"><div style="display:flex;align-items:center;gap:14px"><div class="md">.md</div><div><b style="font:800 30px/1 M">Стиль постів</b><div style="font:500 20px/1.3 J;color:#8a7f73;margin-top:6px">skill.md</div></div></div><div style="font:500 22px/1.6 J;color:#5d5248;margin-top:18px">коротко, на «ви»<br>без емодзі<br>теплий тон</div></div>'''))
S.append(at(2,'''<div class="k" style="left:LEFTpx;top:250px">НАВІЩО</div><div class="h" style="left:LEFTpx;top:290px;font-size:88px">Більше не треба<br><span class="br">повторювати</span></div>
<div style="position:absolute;left:LEFTpx;top:520px;width:600px;display:flex;flex-direction:column;gap:12px">'''+''.join(f'<div class="old" style="opacity:{o}">Пиши коротко, на «ви», без емодзі…</div>' for o in (1,.7,.45))+'''</div>
<div class="new" style="left:LEFTpx;top:800px">Зроби пост ✓</div>'''))
S.append(at(3,'''<div class="k" style="left:LEFTpx;top:250px">ДЕ БРАТИ · 01</div><div class="h" style="left:LEFTpx;top:290px;font-size:88px">Каталог прямо<br><span class="br">в Claude</span></div>
<div class="p" style="left:LEFTpx;top:500px;width:920px;font-size:33px">Плюсик у чаті → Skills → Переглянути. Там тисячі скілів за темами, серед них офіційні від Anthropic для Word, Excel, PowerPoint і PDF.</div>
<img class="ui" src="ui_menu.png" style="left:LEFTpx;top:690px;width:470px;transform:rotate(-2deg)">
<img class="ui" src="ui_catalog.png" style="left:XX+560px;top:660px;width:430px;transform:rotate(2deg)">'''))
S.append(at(4,'''<div class="k" style="left:LEFTpx;top:250px">ДЕ БРАТИ · 02</div><div class="h" style="left:LEFTpx;top:290px;font-size:88px">Маркетплейс<br><span class="br">скілів</span></div>
<div class="p" style="left:LEFTpx;top:500px;width:470px">На сайті skillsmp.com зібрали понад 4 мільйони скілів. Шукаєте за задачею, читаєте опис, завантажуєте.</div>
<div class="tagl" style="left:LEFTpx;top:900px">skillsmp.com</div>
<img class="ui" src="ui_mp.png" style="left:XX+590px;top:470px;width:420px;transform:rotate(3deg)">'''))
S.append(at(5,'''<div class="k" style="left:LEFTpx;top:250px">ДЕ БРАТИ · 03</div><div class="h" style="left:LEFTpx;top:290px;font-size:92px">GitHub.<br><span class="br">Але обережно</span></div>
<div class="p" style="left:LEFTpx;top:520px;width:520px">Більшість цих мільйонів зібрали саме звідти, а викласти на GitHub може будь-хто. Разом зі скілом легко завантажити шкідливий код.</div>
<div class="warn" style="left:XX+610px;top:520px"><b>Перед встановленням</b><div>✓ хто автор<br>✓ що всередині<br>✗ жодних паролів</div></div>'''))
S.append(at(6,'''<div class="k" style="left:LEFTpx;top:250px;color:#C9935E">А НАЙКРАЩЕ</div><div class="h" style="left:LEFTpx;top:290px;font-size:96px;color:#EFE7DF">Скіл під<br><span class="gold">ваш процес</span></div>
<div class="p" style="left:LEFTpx;top:520px;width:480px;color:#d9cbbb">Його можна створити разом з Claude, без коду. Як саме, покажемо в наступному пості.</div>
<img class="ui dk" src="ui_add.png" style="left:XX+600px;top:540px;width:400px;transform:rotate(-2deg)">
<div class="h" style="left:LEFTpx;top:840px;font-size:48px;color:#EFE7DF;line-height:1.1">Підпишіться,<br><span class="gold">щоб не пропустити</span></div>'''))
body=''.join(S).replace('XX+','')
import re
body=re.sub(r'left:(\d+)\+(\d+)px',lambda m:f'left:{int(m[1])+int(m[2])}px',''.join(S))
html=f'''<!doctype html><meta charset="utf-8"><style>@font-face{{font-family:M;src:url(Montserrat.ttf)}}@font-face{{font-family:J;src:url(JetBrainsMono.ttf)}}
*{{margin:0;box-sizing:border-box}}body{{width:{W*N}px;height:{H}px;position:relative;overflow:hidden;font-family:M;color:#190F09}}
.bg{{position:absolute;top:0;width:{W}px;height:{H}px}}.bg.L{{background:linear-gradient(180deg,#F4EEE7,#ECE3D8)}}.bg.D{{background:radial-gradient(70% 55% at 55% 40%,#3a2919 0%,#1e140c 60%,#0e0905 100%)}}
.logo{{position:absolute;top:64px;display:flex;align-items:center;gap:12px}}.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}.logo small{{font:700 11px/1 M;letter-spacing:.2em;margin-top:6px;margin-right:-.2em;color:#A16E3B}}
.pg{{position:absolute;top:78px;width:68px;text-align:right;font:500 22px/1 J;color:#8a7f73}}.pg.D{{color:#a8937d}}
.h{{position:absolute;font-weight:800;letter-spacing:-.045em;line-height:1}}.br{{color:#A16E3B}}
.gold{{background:linear-gradient(180deg,#F2D29A,#C99662 55%,#8E5F33);-webkit-background-clip:text;color:transparent}}
.p{{position:absolute;font:500 36px/1.4 M;color:#3b2e24}}.k{{position:absolute;font:800 28px/1 J;color:#A16E3B;letter-spacing:.05em}}
.card{{position:absolute;width:400px;background:#fff;border-radius:26px;box-shadow:0 20px 50px rgba(25,15,9,.1);padding:30px 32px}}
.md{{width:56px;height:68px;border-radius:10px;background:#190F09;color:#F2D29A;font:800 20px/68px J;text-align:center}}
.old{{background:#fff;color:#9c8f82;border-radius:22px;padding:18px 24px;font:600 28px/1.2 M;text-decoration:line-through;text-decoration-color:#A16E3B;text-decoration-thickness:3px}}
.new{{position:absolute;background:#190F09;color:#EFE7DF;border-radius:26px;padding:24px 32px;font:800 44px/1 M}}
.ui{{position:absolute;border-radius:22px;box-shadow:0 24px 60px rgba(25,15,9,.28)}}.ui.dk{{box-shadow:0 0 0 2px rgba(239,231,223,.15),0 24px 60px rgba(0,0,0,.5)}}
.tagl{{position:absolute;font:800 34px/1 J;padding:20px 26px;border-radius:999px;border:3px solid #A16E3B;color:#714326}}
.warn{{position:absolute;width:400px;background:#190F09;color:#EFE7DF;border-radius:28px;padding:34px 34px}}.warn b{{display:block;font:800 30px/1.1 M;color:#F2D29A;margin-bottom:18px}}.warn div{{font:600 32px/1.6 M}}
.car{{position:absolute;width:330px;height:150px;transform-origin:170px 150px;filter:drop-shadow(0 14px 16px rgba(0,0,0,.25))}}
</style>{bg}
<svg style="position:absolute;left:0;top:0" width="{W*N}" height="{H}"><path d="{d}" fill="none" stroke="#A16E3B" stroke-width="70"/><path d="{d}" fill="none" stroke="#21160e" stroke-width="60"/><path d="{d}" fill="none" stroke="#E9CB95" stroke-width="5" stroke-dasharray="26 22"/></svg>
{L}{body}{cars}'''
open('pano.html','w').write(html)
