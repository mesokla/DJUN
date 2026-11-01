BASE='''@font-face{font-family:M;src:url(Montserrat.ttf)}@font-face{font-family:J;src:url(JetBrainsMono.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:M}
.logo{position:absolute;top:64px;left:72px;display:flex;align-items:center;gap:12px;z-index:5}
.logo .w{display:flex;flex-direction:column;align-items:flex-end}.logo small{font:700 11px/1 M;letter-spacing:.2em;margin-top:6px;margin-right:-.2em}
.pg{position:absolute;top:78px;right:72px;font:500 22px/1 J;z-index:5}
'''
def logo(dark=True,col='#A16E3B'):
    c,l=('crest.svg','letters.svg') if dark else ('crest_light.svg','letters_light.svg')
    return f'<div class="logo"><img src="{c}" style="height:50px"><div class="w"><img src="{l}" style="height:22px"><small style="color:{col}">AI академія</small></div></div>'
def P(css,body): return f'<!doctype html><meta charset="utf-8"><style>{BASE}{css}</style>{body}'
S={}
# 1 — job listing card on brown
S[1]=P('''body{background:#A16E3B}
.pat{position:absolute;inset:0;top:220px;font:800 120px/1.25 M;color:rgba(25,15,9,.07);white-space:pre;letter-spacing:.2em;padding:20px}
.card{position:absolute;left:90px;right:90px;top:250px;background:#EFE7DF;border-radius:28px;padding:56px 56px 50px;box-shadow:0 40px 80px rgba(25,15,9,.35);transform:rotate(-2.5deg)}
.tag{display:inline-block;font:600 24px/1 J;color:#EFE7DF;background:#190F09;padding:12px 18px;border-radius:999px}
.card h1{font-weight:800;font-size:92px;line-height:.98;letter-spacing:-.04em;color:#190F09;margin-top:30px}
.card h1 em{font-style:normal;color:#A16E3B}
.rows{margin-top:40px}.r{display:flex;justify-content:space-between;align-items:center;padding:20px 0;border-top:2px dashed rgba(25,15,9,.18)}
.r span{font:500 26px/1 J;color:#6E5F52}.r b{font-weight:800;font-size:42px;color:#190F09}
.stamp{position:absolute;right:70px;top:190px;width:250px;height:250px;border-radius:50%;border:6px solid #01403D;color:#01403D;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(14deg);font:800 34px/1.05 M;text-align:center;background:rgba(239,231,223,.0)}
.stamp small{font:600 18px/1 J;letter-spacing:.15em;margin-top:8px}
.sw{position:absolute;left:90px;bottom:80px;font:600 28px/1 J;color:#190F09}''',
 '<div class="pat">} O # ›\n› # } O\nO › # }\n# } O ›</div>'+logo(True,'#190F09').replace('#A16E3B','#190F09')+'''<div class="pg" style="color:#190F09">1/5</div>
<div class="card"><span class="tag">● відкрита вакансія</span><h1>Шукаємо<br><em>співробітника</em></h1>
<div class="rows"><div class="r"><span>зарплата</span><b>$20 / міс</b></div><div class="r"><span>графік</span><b>24/7</b></div><div class="r"><span>лікарняні</span><b>ніколи 🙂</b></div></div></div>
<div class="stamp">ТЕРМІНОВО<small>// djun hr</small></div>
<div class="sw">що він робитиме →</div>''')
# 2 — sticky notes on beige
S[2]=P('''body{background:#EFE7DF}
h2{position:absolute;left:72px;top:180px;font-weight:800;font-size:84px;line-height:1;letter-spacing:-.04em;color:#190F09}
h2 em{font-style:normal;color:#A16E3B}
.n{position:absolute;width:430px;padding:40px 36px 44px;box-shadow:0 22px 40px rgba(25,15,9,.18)}
.n i{display:block;font:600 22px/1 J;font-style:normal;margin-bottom:22px;opacity:.75}
.n b{display:block;font-weight:800;font-size:44px;line-height:1.05;letter-spacing:-.02em}
.n span{display:block;font:500 26px/1.3 M;margin-top:14px;opacity:.85}
.pin{position:absolute;top:-14px;left:50%;width:28px;height:28px;margin-left:-14px;border-radius:50%;background:#190F09;box-shadow:0 4px 8px rgba(0,0,0,.3)}
.time{position:absolute;right:72px;bottom:80px;font:600 26px/1.3 J;color:#6E5F52;text-align:right}''',
 logo(True)+'''<div class="pg" style="color:#6E5F52">2/5</div>
<h2>Що він<br><em>робитиме:</em></h2>
<div class="n" style="left:70px;top:430px;background:#FFFFFF;color:#190F09;transform:rotate(-4deg)"><div class="pin"></div><i>// пн–пт</i><b>Заявки з пошти в таблицю</b><span>без Ctrl+C → Ctrl+V</span></div>
<div class="n" style="right:60px;top:520px;background:#190F09;color:#EFE7DF;transform:rotate(3deg)"><div class="pin" style="background:#A16E3B"></div><i>// щоп'ятниці</i><b>Звіт з тих самих цифр</b><span>сам, у Telegram</span></div>
<div class="n" style="left:150px;top:850px;background:#A16E3B;color:#190F09;transform:rotate(-1.5deg)"><div class="pin"></div><i>// щодня</i><b>«А скільки коштує?»</b><span>відповідає клієнтам сам</span></div>
<div class="time">зараз це ~8 год<br>вашого тижня</div>''')
# 3 — green chat reveal
S[3]=P('''body{background:#01403D;color:#EFE7DF}
.k{position:absolute;left:72px;top:190px;font:500 28px/1 J;color:#9FD3CB}
h1{position:absolute;left:72px;top:240px;font-weight:800;font-size:118px;line-height:.95;letter-spacing:-.045em}
h1 em{font-style:normal;color:#D9B48C}
.chat{position:absolute;left:72px;right:72px;top:640px}
.b{max-width:760px;padding:34px 38px;border-radius:32px;font:500 38px/1.35 M;margin-bottom:26px}
.ai{background:#EFE7DF;color:#190F09;border-bottom-left-radius:8px}
.me{background:#A16E3B;color:#190F09;margin-left:auto;border-bottom-right-radius:8px}
.who{display:flex;align-items:center;gap:14px;font:600 22px/1 J;color:#9FD3CB;margin-bottom:12px}
.av{width:56px;height:56px;border-radius:50%;background:#EFE7DF;display:flex;align-items:center;justify-content:center}''',
 logo(False,'#9FD3CB')+'''<div class="pg" style="color:#9FD3CB">3/5</div>
<div class="k">// знайомтесь</div><h1>Це AI&#8209;<br><em>асистент</em></h1>
<div class="chat">
<div class="who"><div class="av"><img src="crest.svg" style="height:36px"></div>Ваш AI-асистент · 09:00</div>
<div class="b ai">Доброго ранку! 3 нові заявки вже в таблиці, звіт за тиждень надіслав вам 👌</div>
<div class="b me">А як тебе найняти?</div>
<div class="b ai">За тиждень. Гортайте →</div></div>''')
# 4 — white, resume requirements with strike
S[4]=P('''body{background:#FFFFFF;color:#190F09}
.k{position:absolute;left:72px;top:190px;font:500 28px/1 J;color:#A16E3B}
h1{position:absolute;left:72px;top:240px;font-weight:800;font-size:90px;line-height:1;letter-spacing:-.04em}
.list{position:absolute;left:72px;right:72px;top:500px;border-top:3px solid #190F09}
.it{display:flex;align-items:center;gap:30px;padding:36px 0;border-bottom:1.5px solid #E6DACD}
.ic{width:74px;height:74px;border-radius:18px;display:flex;align-items:center;justify-content:center;font:800 44px/1 M;flex:none}
.it b{font-weight:800;font-size:46px;letter-spacing:-.02em;line-height:1.1}
.it span{display:block;font:500 28px/1.3 M;color:#6E5F52;margin-top:6px}
.no b{color:#B9A897;text-decoration:line-through;text-decoration-color:#A16E3B;text-decoration-thickness:6px}
.big{position:absolute;right:-120px;bottom:-70px;height:480px;opacity:.95;filter:drop-shadow(0 30px 40px rgba(0,0,0,.25))}''',
 logo(True)+'''<div class="pg" style="color:#6E5F52">4/5</div>
<div class="k">// вимоги до вас</div><h1>А що треба<br>вміти вам?</h1>
<div class="list">
<div class="it no"><div class="ic" style="background:#EFE7DF;color:#A16E3B">✕</div><div><b>Програмувати</b><span>код пише AI</span></div></div>
<div class="it"><div class="ic" style="background:#190F09;color:#EFE7DF">✓</div><div><b>Пояснити задачу</b><span>навчимо за 7 днів</span></div></div>
<div class="it"><div class="ic" style="background:#A16E3B;color:#190F09">✓</div><div><b>Перевірити результат</b><span>рішення завжди за вами</span></div></div></div><img class="big" src="glyph_brace.png">''')
# 5 — ink CTA with big 3D O and price tag
S[5]=P('''body{background:radial-gradient(70% 50% at 70% 60%,#3d2c1a 0%,#1a110a 60%,#100a06 100%);color:#EFE7DF}
.k{position:absolute;left:72px;top:190px;font:500 28px/1 J;color:#D2A26C}
h1{position:absolute;left:72px;top:240px;font-weight:800;font-size:130px;line-height:.92;letter-spacing:-.05em}
h1 em{font-style:normal;color:#D2A26C}
.sub{position:absolute;left:74px;top:520px;font:500 36px/1.35 M;color:#E4D8CB;width:560px}
.glyph{position:absolute;right:-90px;top:430px;height:560px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.6))}
.tag{position:absolute;left:72px;top:780px;background:#EFE7DF;color:#190F09;padding:30px 40px;border-radius:24px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.4)}
.tag b{font-weight:800;font-size:76px;letter-spacing:-.03em}.tag s{font:600 36px/1 M;color:#8f7f70;margin-left:16px}
.tag small{display:block;font:600 24px/1 J;color:#A16E3B;margin-top:10px}
.date{position:absolute;left:72px;top:1030px;display:flex;gap:16px}
.date span{font:600 26px/1 J;padding:14px 20px;border:2px solid rgba(210,162,108,.6);border-radius:999px;color:#EFE7DF}
.site{position:absolute;left:72px;bottom:80px;font:600 32px/1 J;color:#D2A26C}''',
 logo(False,'#D2A26C')+'''<div class="pg" style="color:#B9A897">5/5</div>
<img class="glyph" src="glyph_O.png">
<div class="k">// як найняти</div><h1>Найми<br><em>AI</em></h1>
<div class="sub">Інтенсив, де за 7 днів ви налаштуєте свого асистента</div>
<div class="tag"><b>1 490 ₴</b><s>3 490 ₴</s><small>до 8 листопада</small></div>
<div class="date"><span>старт 9.11</span><span>7 днів</span><span>3 живі дзвінки</span></div>
<div class="site">najmy-ai.djun.com.ua</div>''')
for k,v in S.items(): open(f'slide_{k}.html','w').write(v)
