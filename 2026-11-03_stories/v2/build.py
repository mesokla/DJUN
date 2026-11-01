BASE='''@font-face{font-family:M;src:url(Montserrat.ttf)}@font-face{font-family:J;src:url(JetBrainsMono.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:M}
.logo{position:absolute;top:250px;left:80px;display:flex;align-items:center;gap:14px;z-index:3}
.logo .w{display:flex;flex-direction:column;align-items:flex-end}.logo small{font:700 13px/1 M;letter-spacing:.2em;margin-top:7px;margin-right:-.2em;color:#D2A26C}
'''
DARK="background:radial-gradient(70% 40% at 50% 40%,#3d2c1a 0%,#24190f 45%,#140e08 80%,#0e0905 100%);color:#EFE7DF"
DOTS='<div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(217,180,140,.55) 1.8px,transparent 2.4px);background-size:48px 48px;-webkit-mask:radial-gradient(70% 45% at 50% 40%,#000 0%,rgba(0,0,0,.45) 60%,rgba(0,0,0,.15) 100%)"></div>'
GOLD="background:linear-gradient(180deg,#F2D29A 0%,#C99662 55%,#8E5F33 100%);-webkit-background-clip:text;color:transparent"
def logo(light=True):
    c,l=('crest_light.svg','letters_light.svg') if light else ('crest.svg','letters.svg')
    return f'<div class="logo"><img src="{c}" style="height:60px"><div class="w"><img src="{l}" style="height:25px"><small>AI академія</small></div></div>'
S={}
# 1: giant centered type + floating role chips; quiz bottom
S['1_who']=f'''<!doctype html><meta charset="utf-8"><style>{BASE}
body{{background:url(meme_field.jpg) 30% center/cover;color:#fff}}
.dim{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,6,3,.78) 0%,rgba(10,6,3,.45) 30%,rgba(10,6,3,.15) 55%,rgba(10,6,3,.35) 100%)}}
h1{{position:absolute;left:80px;right:80px;top:400px;font-weight:800;font-size:130px;line-height:.95;letter-spacing:-.05em;text-shadow:0 6px 30px rgba(0,0,0,.5)}}
</style><div class="dim"></div>{logo()}<h1>Ким ви<br>працюєте?</h1>'''
# 2: sticker on top half, giant 3D brace, text anchored bottom
S['2_other']=f'''<!doctype html><meta charset="utf-8"><style>{BASE}
body{{background:#EFE7DF;color:#190F09}}
.logo small{{color:#A16E3B}}
.g{{position:absolute;right:-180px;top:330px;height:820px;filter:drop-shadow(0 30px 50px rgba(25,15,9,.3))}}
.arrow{{position:absolute;left:80px;top:1120px;font:500 30px/1 J;color:#A16E3B}}
h1{{position:absolute;left:80px;right:80px;top:1170px;font-weight:800;font-size:84px;line-height:1;letter-spacing:-.04em}}
h1 em{{font-style:normal;color:#A16E3B}}
.s{{position:absolute;left:82px;top:1480px;font:500 34px/1.35 M;color:#6E5F52}}
</style>{logo(False)}<img class="g" src="glyph_brace.png">

<h1>Не знайшли<br>себе? <em>Впишіть<br>свій варіант</em></h1>
'''
# 3: routine wall of Ctrl+C/V, centered question, poll bottom
rows=''.join(f'<div style="opacity:{o}">Ctrl+C → Ctrl+V &nbsp;·&nbsp; звіт_фінал_2.xlsx &nbsp;·&nbsp; «А скільки коштує?»</div>' for o in [.05,.09,.13,.09,.05])
S['3_time']=f'''<!doctype html><meta charset="utf-8"><style>{BASE}
body{{{DARK}}}
.wall{{position:absolute;left:-80px;top:1180px;width:1400px;font:600 40px/1.9 J;color:#D2A26C;white-space:nowrap;transform:rotate(-6deg)}}
.k{{position:absolute;left:80px;top:420px;font:500 30px/1 J;color:#D2A26C}}
h1{{position:absolute;left:80px;right:80px;top:470px;font-weight:800;font-size:112px;line-height:.98;letter-spacing:-.045em;color:#EFE7DF}}
h1 em{{font-style:normal;{GOLD}}}
p{{position:absolute;left:82px;right:120px;top:850px;font:500 38px/1.4 M;color:#C9B8A6}}
</style>{DOTS}<div class="wall">{rows}</div>{logo()}
<div class="k">// тільки чесно</div>
<h1>Скільки годин<br>на тиждень<br><em>з'їдає рутина?</em></h1>
<p>Ті самі звіти, ті самі листи і «а можеш ще раз скинути той файл?»</p>'''
for k,v in S.items(): open(f'story_{k}.html','w').write(v)
