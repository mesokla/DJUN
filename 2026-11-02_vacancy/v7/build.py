BASE='''@font-face{font-family:M;src:url(Montserrat.ttf)}@font-face{font-family:J;src:url(JetBrainsMono.ttf)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:M;color:#190F09}
.logo{position:absolute;top:64px;left:72px;display:flex;align-items:center;gap:12px;z-index:5}
.logo .w{display:flex;flex-direction:column;align-items:flex-end}.logo small{font:700 11px/1 M;letter-spacing:.2em;margin-top:6px;margin-right:-.2em;color:#A16E3B}
.pg{position:absolute;top:78px;right:72px;font:500 22px/1 J;z-index:5;color:#6E5F52}
'''
def logo(light=False):
    c,l=('crest_light.svg','letters_light.svg') if light else ('crest.svg','letters.svg')
    return f'<div class="logo"><img src="{c}" style="height:50px"><div class="w"><img src="{l}" style="height:22px"><small>AI академія</small></div></div>'
def P(css,body): return f'<!doctype html><meta charset="utf-8"><style>{BASE}{css}</style>{body}'
S={}
# 1 job board card
S[1]=P('''body{background:#A16E3B}
.pat{position:absolute;left:0;right:0;top:200px;bottom:0;font:800 120px/1.25 M;color:rgba(25,15,9,.07);white-space:pre;letter-spacing:.2em;padding:20px}
.w2{position:absolute;left:64px;right:64px;top:230px;background:#fff;border-radius:22px;box-shadow:0 40px 80px rgba(25,15,9,.35);overflow:hidden}
.bar{display:flex;align-items:center;gap:14px;padding:20px 30px;background:#F3F1EE;border-bottom:1px solid #E5E1DB;font:500 22px/1 J;color:#8a8278}
.dot{width:14px;height:14px;border-radius:50%;background:#D9D4CC}
.in{padding:50px 52px 56px}
.meta{display:flex;gap:12px;flex-wrap:wrap}.meta span{font:600 26px/1 M;padding:12px 18px;border-radius:10px;background:#F3EEE8;color:#6E5F52}
.meta .hot{background:#190F09;color:#EFE7DF}
h1{font-weight:800;font-size:72px;line-height:1.02;letter-spacing:-.03em;margin-top:32px}
.sal{font-weight:800;font-size:68px;color:#A16E3B;margin-top:16px;letter-spacing:-.02em}
.co{display:flex;align-items:center;gap:16px;margin-top:26px;padding-top:26px;border-top:1px solid #EEE8E1}
.co .av{width:64px;height:64px;border-radius:14px;background:#190F09;display:flex;align-items:center;justify-content:center}
.co b{font-weight:700;font-size:32px}.co small{display:block;font:500 22px/1.2 M;color:#8a8278;margin-top:4px}
ul{list-style:none;margin-top:12px}.req{font:700 28px/1 M;margin-top:30px;color:#190F09}li{font:500 33px/1.6 M;color:#3b2e24}li:before{content:"✓  ";color:#A16E3B;font-weight:800}
.btn{display:inline-block;margin-top:36px;background:#190F09;color:#EFE7DF;font:700 32px/1 M;padding:26px 40px;border-radius:14px}
.sw{position:absolute;left:72px;bottom:70px;font:600 28px/1 J;color:#190F09}''',
 '<div class="pat">} O # ›\n› # } O\nO › # }\n# } O ›</div>'+logo().replace('crest.svg','crest_onbrown.svg').replace('letters.svg','letters_onbrown.svg').replace('<small>','<small style="color:#EFE7DF">')+'''<div class="pg" style="color:#190F09">1/6</div>
<div class="w2"><div class="bar"><div class="dot"></div><div class="dot"></div><div class="dot"></div>&nbsp;вакансії · опубліковано сьогодні</div>
<div class="in"><div class="meta"><span class="hot">🔥 Гаряча</span><span>Віддалено</span><span>Повна зайнятість</span></div>
<h1>Шукаємо помічника з рутинних задач</h1><div class="sal">$20 / міс</div>
<div class="req">Вимоги до кандидата:</div><ul><li>працювати 24/7, без вихідних і відпусток</li><li>нічого не забувати</li><li>досвід асистентської роботи від 2 років: таблиці, пошта, документи</li></ul>
<div class="co"><div class="av"><img src="crest_light.svg" style="height:42px"></div><div><b>Джун AI академія</b><small>роботодавець · віддалено</small></div></div>
<div class="btn">Обов'язки →</div></div></div>''')
# 2 duties list + more tags
S[2]=P('''body{background:#EFE7DF}
.k{position:absolute;left:72px;top:190px;font:500 28px/1 J;color:#A16E3B}
h2{position:absolute;left:72px;top:236px;font-weight:800;font-size:96px;line-height:.98;letter-spacing:-.04em}
h2 em{font-style:normal;color:#A16E3B}
.list{position:absolute;left:72px;right:72px;top:420px;border-top:3px solid #190F09}
.it{display:flex;align-items:baseline;gap:30px;padding:34px 0;border-bottom:1.5px solid #D9CBBB}
.it i{font:800 64px/1 M;font-style:normal;color:#A16E3B;min-width:90px;letter-spacing:-.03em}
.it b{font-weight:800;font-size:46px;letter-spacing:-.02em;line-height:1.1}.it span{display:block;font:500 28px/1.3 M;color:#6E5F52;margin-top:6px}
.more{position:absolute;left:72px;right:72px;top:960px}
.more p{font:800 40px/1 M;letter-spacing:-.02em}.more p em{font-style:normal;color:#A16E3B}
.tags{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}.tags span{font:600 24px/1 J;padding:12px 18px;border:2px solid #A16E3B;border-radius:999px;color:#714326}''',
 logo()+'''<div class="pg">2/6</div><div class="k">// що потрібно робити</div><h2>Обов'язки</h2>
<div class="list">
<div class="it"><i>01</i><div><b>Обробляти заявки з пошти</b><span>і вносити їх у таблицю</span></div></div>
<div class="it"><i>02</i><div><b>Готувати щотижневі звіти</b><span>щоп'ятниці, без запізнень</span></div></div>
<div class="it"><i>03</i><div><b>Відповідати всім клієнтам</b><span>на типові питання, швидко й ввічливо</span></div></div>
</div>
<div class="more"><p>…і ще <em>багато іншого:</em></p><div class="tags"><span>листи</span><span>нагадування</span><span>документи</span><span>аналітика</span><span>новини галузі</span><span>контент</span><span>ваша задача</span></div></div>''')
S[3]=P('''body{background:#A16E3B}
.pat{position:absolute;left:0;right:0;top:200px;bottom:0;font:800 120px/1.25 M;color:rgba(25,15,9,.07);white-space:pre;letter-spacing:.2em;padding:20px}
.q{position:absolute;left:72px;right:72px;top:260px;font-weight:800;font-size:96px;line-height:1;letter-spacing:-.04em;color:#190F09}
.q em{font-style:normal;color:#EFE7DF}
.a{position:absolute;left:72px;right:72px;top:720px;background:#190F09;color:#EFE7DF;border-radius:28px;padding:46px 50px;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(25,15,9,.3)}
.a p{font:600 44px/1.25 M;letter-spacing:-.01em}.a p em{font-style:normal;color:#D2A26C}
.a small{display:block;font:500 26px/1 J;color:#B9A897;margin-top:22px}''',
 '<div class="pat">} O # ›\n› # } O\nO › # }\n# } O ›</div>'+logo().replace('crest.svg','crest_onbrown.svg').replace('letters.svg','letters_onbrown.svg').replace('<small>','<small style="color:#EFE7DF">')+'''<div class="pg" style="color:#190F09">3/6</div>
<div class="q">Думаєте,<br>ми <em>трохи</em><br><em>перегнули?</em></div>
<div class="a"><p>Але чесно: ви б і самі хотіли <em>такого співробітника.</em></p><small>і він справді існує →</small></div>''')
# 3 messenger chat
S[4]=P('''body{background:#EFE7DF;color:#190F09}
.k{position:absolute;left:72px;top:180px;font:500 28px/1 J;color:#A16E3B}
h1{position:absolute;left:72px;top:226px;font-weight:800;font-size:92px;line-height:.98;letter-spacing:-.04em}h1 em{font-style:normal;color:#A16E3B}
.ph{position:absolute;left:110px;right:110px;top:470px;bottom:-40px;background:#0E1621;border-radius:56px 56px 0 0;box-shadow:0 30px 70px rgba(25,15,9,.3);overflow:hidden;border:10px solid #190F09;border-bottom:none}
.hd{display:flex;align-items:center;gap:18px;padding:26px 30px;background:#17212B}
.hd .av{width:70px;height:70px;border-radius:50%;background:#EFE7DF;display:flex;align-items:center;justify-content:center}
.hd b{font-weight:700;font-size:30px;color:#fff}.hd small{display:block;font:500 22px/1 M;color:#6AB2F2;margin-top:6px}
.wall{position:absolute;top:122px;left:0;right:0;bottom:0;background:#0E1621;padding:30px 26px}
.m{position:relative;max-width:640px;padding:20px 26px 32px;border-radius:24px;font:500 30px/1.35 M;margin-bottom:16px;color:#fff}
.m .t{position:absolute;right:16px;bottom:8px;font:500 18px/1 M;color:#7d8b99}
.in{background:#182533;border-bottom-left-radius:6px}
.out{background:#2B5278;margin-left:auto;border-bottom-right-radius:6px}.out .t{color:#9cc4e8}''',
 logo()+'''<div class="pg">4/6</div><div class="k">// знайомтесь</div><h1>Це AI&#8209;<em>асистент</em></h1>
<div class="ph"><div class="hd"><div class="av"><img src="crest.svg" style="height:44px"></div><div><b>AI-асистент</b><small>у мережі</small></div></div>
<div class="wall">
<div class="m in">Доброго ранку! ☀️ 3 нові заявки вже в таблиці<span class="t">09:00</span></div>
<div class="m in">Звіт за тиждень готовий, надіслав файлом 📊<span class="t">09:00</span></div>
<div class="m out">Ого. А як тебе найняти? 😄<span class="t">09:02 ✓✓</span></div>
<div class="m in">За 7 днів. Гортайте →<span class="t">09:02</span></div></div></div>''')
# 4 requirements white (same as v2)
S[5]=P('''body{background:#FFFFFF}
.k{position:absolute;left:72px;top:190px;font:500 28px/1 J;color:#A16E3B}
h1{position:absolute;left:72px;top:240px;font-weight:800;font-size:90px;line-height:1;letter-spacing:-.04em}
.list{position:absolute;left:72px;right:72px;top:500px;border-top:3px solid #190F09}
.it{display:flex;align-items:center;gap:30px;padding:36px 0;border-bottom:1.5px solid #E6DACD}
.ic{width:74px;height:74px;border-radius:18px;display:flex;align-items:center;justify-content:center;font:800 44px/1 M;flex:none}
.it b{font-weight:800;font-size:46px;letter-spacing:-.02em;line-height:1.1}.it span{display:block;font:500 28px/1.3 M;color:#6E5F52;margin-top:6px}
.no b{color:#B9A897;text-decoration:line-through;text-decoration-color:#A16E3B;text-decoration-thickness:6px}
.big{position:absolute;right:-120px;bottom:-70px;height:480px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.25))}''',
 logo()+'''<div class="pg">5/6</div><div class="k">// вимоги до вас</div><h1>А що треба<br>вміти вам?</h1>
<div class="list">
<div class="it no"><div class="ic" style="background:#EFE7DF;color:#A16E3B">✕</div><div><b>Програмувати</b><span>код пише AI</span></div></div>
<div class="it"><div class="ic" style="background:#190F09;color:#EFE7DF">✓</div><div><b>Пояснити задачу</b><span>навчимо за 7 днів</span></div></div>
<div class="it"><div class="ic" style="background:#A16E3B;color:#190F09">✓</div><div><b>Перевірити результат</b><span>рішення завжди за вами</span></div></div></div><img class="big" src="glyph_brace.png">''')
# 5 CTA in same language: beige, offer card like slide1
S[6]=P('''body{background:#A16E3B}
.k{position:absolute;left:72px;top:190px;font:500 28px/1 J;color:#190F09}
h1{position:absolute;left:72px;top:236px;font-weight:800;font-size:120px;line-height:.92;letter-spacing:-.05em}h1 em{font-style:normal;color:#EFE7DF}
.sub{position:absolute;left:74px;top:500px;font:500 36px/1.35 M;color:#190F09;width:600px}
.glyph{position:absolute;right:-110px;top:250px;height:470px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.25))}
.card{position:absolute;left:64px;right:64px;top:700px;background:#fff;border-radius:22px;padding:40px 44px;box-shadow:0 30px 60px rgba(25,15,9,.15)}
.row{display:flex;gap:12px;flex-wrap:wrap}.row span{font:600 24px/1 M;padding:12px 18px;border-radius:10px;background:#F3EEE8;color:#6E5F52}
.pr{display:flex;align-items:baseline;gap:18px;margin-top:26px}.pr b{font-weight:800;font-size:84px;letter-spacing:-.03em}.pr s{font:600 40px/1 M;color:#B9A897}
.pr i{font:600 24px/1 J;font-style:normal;color:#fff;background:#A16E3B;padding:10px 14px;border-radius:10px}
.dl{font:600 24px/1 J;color:#A16E3B;margin-top:14px}
.site{position:absolute;left:72px;bottom:80px;font:600 34px/1 J;color:#190F09}
.site span{color:#EFE7DF}''',
 logo().replace('crest.svg','crest_onbrown.svg').replace('letters.svg','letters_onbrown.svg').replace('<small>','<small style="color:#EFE7DF">')+'''<div class="pg" style="color:#190F09">6/6</div><img class="glyph" src="glyph_O.png"><div class="k">// як найняти</div><h1>Найми<br><em>AI</em></h1>
<div class="sub">Інтенсив, де за 7 днів ви налаштуєте свого асистента</div>
<div class="card"><div class="row"><span>старт 9.11</span><span>7 днів</span><span>3 живі дзвінки</span><span>без коду</span></div>
<div class="pr"><b>1 490 ₴</b><s>3 490 ₴</s><i>−57%</i></div><div class="dl">// ціна старту діє до 8 листопада</div></div>
<div class="site"><span>→</span> najmy-ai.djun.com.ua</div>''')
for k,v in S.items(): open(f'slide_{k}.html','w').write(v)
