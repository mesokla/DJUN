BASE='''@font-face{font-family:M;src:url(Montserrat.ttf)}@font-face{font-family:J;src:url(JetBrainsMono.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:M}
.logo{position:absolute;top:250px;left:80px;display:flex;align-items:center;gap:14px}
.logo .w{display:flex;flex-direction:column;align-items:flex-end}.logo small{font:700 13px/1 M;letter-spacing:.2em;margin-top:7px;margin-right:-.2em;color:#A16E3B}
.k{position:absolute;left:80px;top:400px;font:500 30px/1 J}
h1{position:absolute;left:80px;right:80px;top:450px;font-weight:800;font-size:100px;line-height:1;letter-spacing:-.04em}
.hint{position:absolute;left:80px;right:80px;font:500 36px/1.35 M}
.slot{position:absolute;left:80px;right:80px;border:3px dashed;border-radius:28px;display:flex;align-items:center;justify-content:center;font:500 26px/1 J}
.g{position:absolute;filter:drop-shadow(0 30px 50px rgba(0,0,0,.45))}
'''
DARK="background:radial-gradient(70% 40% at 55% 40%,#3d2c1a 0%,#24190f 45%,#140e08 80%,#0e0905 100%);color:#EFE7DF"
DOTS='<div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(217,180,140,.55) 1.8px,transparent 2.4px);background-size:48px 48px;-webkit-mask:radial-gradient(70% 45% at 55% 40%,#000 0%,rgba(0,0,0,.45) 60%,rgba(0,0,0,.15) 100%)"></div>'
GOLD="background:linear-gradient(180deg,#F2D29A 0%,#C99662 55%,#8E5F33 100%);-webkit-background-clip:text;color:transparent"
def logo(light):
    c,l=('crest_light.svg','letters_light.svg') if light else ('crest.svg','letters.svg')
    return f'<div class="logo"><img src="{c}" style="height:64px"><div class="w"><img src="{l}" style="height:27px"><small>AI академія</small></div></div>'
def P(css,body,slot=True,dark=False):
    sl='<div class="slot" style="top:1000px;height:440px;border-color:{0};color:{0}">місце для стікера</div>'.format('rgba(210,162,108,.45)' if dark else 'rgba(161,110,59,.45)') if slot else ''
    return f'<!doctype html><meta charset="utf-8"><style>{BASE}{css}</style>{body}{sl}'
S={}
S['1_who']=P('body{'+DARK+'}.k{color:#D2A26C}h1 em{font-style:normal;'+GOLD+'}.hint{top:800px;color:#C9B8A6}',
 DOTS+logo(True)+'<div class="k">// давайте знайомитись</div><h1>Ким ви<br><em>працюєте?</em></h1><div class="hint">Оберіть варіант ↓</div><img class="g" src="glyph_O.png" style="right:-150px;bottom:-40px;height:420px;opacity:.9">',dark=True)
S['2_other']=P('body{background:#EFE7DF;color:#190F09}.k{color:#A16E3B}h1 em{font-style:normal;color:#A16E3B}.hint{top:800px;color:#6E5F52}',
 logo(False)+'<div class="k">// не знайшли себе?</div><h1>Напишіть<br><em>свою професію</em></h1><div class="hint">Нам цікаво, хто нас читає ↓</div><img class="g" src="glyph_brace.png" style="right:-120px;bottom:-60px;height:440px">')
S['3_time']=P('body{'+DARK+'}.k{color:#D2A26C}h1{font-size:88px}h1 em{font-style:normal;'+GOLD+'}.hint{top:880px;color:#C9B8A6}',
 DOTS+logo(True)+'<div class="k">// чесне опитування</div><h1>Скільки годин на тиждень іде на <em>одну й ту саму рутину?</em></h1><div class="hint">Таблиці, звіти, однакові відповіді ↓</div><img class="g" src="glyph_hash.png" style="right:-150px;bottom:-40px;height:400px;opacity:.9">',dark=True).replace('top:1000px;height:440px','top:1050px;height:420px')
for k,v in S.items():
    open(f'story_{k}.html','w').write(v)
    open(f'story_{k}_clean.html','w').write(v.split('<div class="slot"')[0])
