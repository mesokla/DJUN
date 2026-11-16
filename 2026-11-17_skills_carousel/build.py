BASE='''@font-face{font-family:M;src:url(Montserrat.ttf)}@font-face{font-family:J;src:url(JetBrainsMono.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:M}
.D{background:radial-gradient(70% 55% at 55% 45%,#3a2919 0%,#1e140c 55%,#0e0905 100%);color:#EFE7DF}
.L{background:#EFE7DF;color:#190F09}.W{background:#FFFFFF;color:#190F09}
.logo{position:absolute;top:64px;left:72px;display:flex;align-items:center;gap:12px;z-index:5}.logo .w{display:flex;flex-direction:column;align-items:flex-end}.logo small{font:700 11px/1 M;letter-spacing:.2em;margin-top:6px;margin-right:-.2em;color:#C9935E}
.pg{position:absolute;top:78px;right:72px;font:500 22px/1 J;opacity:.6}
.gold{background:linear-gradient(180deg,#F2D29A,#C99662 55%,#8E5F33);-webkit-background-clip:text;color:transparent}
.br{color:#A16E3B}
h1{position:absolute;left:72px;right:72px;font-weight:800;letter-spacing:-.045em;line-height:1}
p{position:absolute;left:74px;right:90px;font:500 36px/1.4 M}
.D p{color:#D8CBBD}.L p,.W p{color:#3b2e24}
.num{font:800 30px/1 J;color:#C9935E;letter-spacing:.05em}
.g{position:absolute;filter:drop-shadow(0 30px 45px rgba(0,0,0,.4))}
'''
def logo(th):
    c,l=('crest_light.svg','letters_light.svg') if th=='D' else ('crest.svg','letters.svg')
    return f'<div class="logo"><img src="{c}" style="height:48px"><div class="w"><img src="{l}" style="height:20px"><small>AI академія</small></div></div>'
def P(i,th,body,css=''):
    return f'<!doctype html><meta charset="utf-8"><style>{BASE}{css}</style><body class="{th}">{logo(th)}<div class="pg">{i}/7</div>{body}</body>'
S={}
S[1]=P(1,'D','''<img class="g" src="glyph_brace.png" style="right:-90px;top:560px;height:640px;opacity:.9">
<h1 style="top:300px;font-size:104px">Ми пояснили AI<br>наш стиль<br><span class="gold">один раз.</span></h1>
<p style="top:760px;right:420px;font-size:40px">І більше жодного разу не повторювали.</p>
<div style="position:absolute;left:72px;bottom:80px;font:600 30px/1 M;color:#C9935E">Як саме, гортайте →</div>''')
S[2]=P(2,'L','''<div class="num" style="position:absolute;left:72px;top:250px">ЩО ЦЕ</div>
<h1 style="top:300px;font-size:120px">Це <span class="br">скіл</span></h1>
<div style="position:absolute;left:72px;top:500px;width:520px;background:#fff;border-radius:28px;box-shadow:0 20px 50px rgba(25,15,9,.1);padding:34px 36px;transform:rotate(-2deg)">
<div style="display:flex;align-items:center;gap:16px"><div style="width:60px;height:72px;border-radius:10px;background:#190F09;color:#F2D29A;font:800 22px/72px J;text-align:center">.md</div><div><b style="font:800 34px/1 M">Стиль постів</b><div style="font:500 22px/1.3 J;color:#8a7f73;margin-top:6px">skill.md</div></div></div>
<div style="font:500 26px/1.5 J;color:#5d5248;margin-top:24px">коротко, на «ви»<br>без емодзі<br>тон теплий, без пафосу</div></div>
<p style="top:960px">Файл з інструкцією, який AI зберігає як окремий навик. Коли бачить схожу задачу, сам його відкриває, нагадувати не треба.</p>''')
S[3]=P(3,'W','''<h1 style="top:250px;font-size:84px">Без скіла<br>і <span class="br">зі скілом</span></h1>
<div style="position:absolute;left:72px;top:520px;font:600 28px/1 M;color:#8a7f73">щоразу</div>
<div style="position:absolute;left:72px;right:200px;top:570px;display:flex;flex-direction:column;gap:14px">
''' + ''.join(f'<div style="background:#F2EDE7;color:#9c8f82;border-radius:24px;padding:20px 26px;font:600 30px/1.2 M;text-decoration:line-through;text-decoration-color:#A16E3B;text-decoration-thickness:3px;opacity:{o}">Пиши коротко, на «ви», без емодзі…</div>' for o in (1,.75,.5)) + '''</div>
<div style="position:absolute;left:72px;top:960px;font:600 28px/1 M;color:#A16E3B">зі скілом</div>
<div style="position:absolute;left:72px;top:1010px;background:#190F09;color:#EFE7DF;border-radius:28px;padding:26px 34px;font:800 46px/1 M">Зроби пост ✓</div>''')
S[4]=P(4,'D','''<div class="num" style="position:absolute;left:72px;top:250px">ДЕ БРАТИ · 01</div>
<h1 style="top:300px;font-size:96px">Готові скіли<br><span class="gold">від Anthropic</span></h1>
<p style="top:560px">Найпростіший старт. Компанія, яка робить Claude, має офіційні скіли для документів, презентацій, таблиць і PDF. Вмикаються прямо в налаштуваннях.</p>
<div style="position:absolute;left:72px;top:880px;display:flex;gap:18px;flex-wrap:wrap">''' + ''.join(f'<div style="font:800 40px/1 J;padding:30px 34px;border-radius:24px;background:rgba(239,231,223,.08);border:2px solid rgba(201,147,94,.5);color:#F2D29A">{x}</div>' for x in ('DOCX','PPTX','XLSX','PDF')) + '</div>')
S[5]=P(5,'L','''<div class="num" style="position:absolute;left:72px;top:250px;color:#A16E3B">ДЕ БРАТИ · 02</div>
<h1 style="top:300px;font-size:96px">Каталоги,<br>де <span class="br">діляться</span></h1>
<p style="top:560px">Люди викладають свої скіли під різні задачі. Знайшли потрібний, завантажили, додали собі.</p>
<div style="position:absolute;left:72px;right:72px;top:820px;display:flex;flex-wrap:wrap;gap:16px">''' + ''.join(f'<span style="font:700 34px/1 M;padding:22px 28px;border-radius:999px;{s}">{x}</span>' for x,s in (('маркетинг','background:#190F09;color:#EFE7DF'),('аналітика','border:3px solid #A16E3B;color:#714326'),('дизайн','background:#fff'),('продажі','border:3px solid #A16E3B;color:#714326'),('звіти','background:#fff'),('контент','background:#A16E3B;color:#fff'),('HR','background:#fff'),('ваша задача','border:3px dashed #A16E3B;color:#714326'))) + '</div>')
S[6]=P(6,'D','''<div class="num" style="position:absolute;left:72px;top:250px">ДЕ БРАТИ · 03</div>
<h1 style="top:300px;font-size:92px">GitHub.<br><span class="gold">Але обережно</span></h1>
<p style="top:540px">Тут скілів найбільше, бо викласти може будь-хто. І разом зі скілом можна завантажити код, який зашкодить вашому комп'ютеру.</p>
<div style="position:absolute;left:72px;right:72px;top:820px;background:#EFE7DF;color:#190F09;border-radius:30px;padding:38px 42px">
<div style="font:800 34px/1 M;color:#A16E3B;margin-bottom:22px">Перед встановленням</div>
<div style="font:600 34px/1.6 M">✓ гляньте, хто автор<br>✓ подивіться, що всередині<br>✗ не давайте паролів і доступів</div></div>''')
S[7]=P(7,'L','''<img class="g" src="glyph_O.png" style="right:-120px;top:620px;height:440px;filter:drop-shadow(0 30px 40px rgba(25,15,9,.25))">
<div class="num" style="position:absolute;left:72px;top:250px;color:#A16E3B">А НАЙКРАЩЕ</div>
<h1 style="top:300px;font-size:104px">Скіл, який ви<br>зробили <span class="br">самі</span></h1>
<p style="top:560px;right:380px">Під свій процес, свій стиль і свої задачі. Як його створити, покажемо в наступному пості.</p>
<div style="position:absolute;left:72px;bottom:90px;font:800 46px/1.1 M">Підпишіться,<br><span class="br">щоб не пропустити</span></div>''')
for k,v in S.items(): open(f'slide_{k}.html','w').write(v)
