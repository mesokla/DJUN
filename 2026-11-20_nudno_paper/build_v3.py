import random
src = open('build.py').read()
exec(src[:src.index('S=[]')])  # HEAD, TAIL, page()
HEAD = HEAD.replace("body.K{background:url(bg_kraft.jpg)} body.P{background:url(bg_clip.jpg)}",
    "body.T{background:#E5E5E5} body.P{background:url(bg_clip.jpg)}\n"
    ".torn{position:absolute;left:55px;top:300px;width:970px;filter:drop-shadow(0 14px 22px rgba(0,0,0,.14))}")
def page(cls, body): return HEAD % cls + body + TAIL

def T(title, note, inner, below):
    return page('T', f'''<img class="torn" src="torn_paper.png">
<div class="a cav" style="left:130px;top:370px;font-size:150px;transform:rotate(-2deg)">{title}</div>
<div class="a bad rd" style="left:700px;top:520px;font-size:48px;transform:rotate(-8deg)">{note}</div>
{inner}
<div class="a bad" style="left:120px;top:1110px;font-size:46px;transform:rotate(-2deg)">{below}</div>''')

def L(y, t, x=False, sz=50, l=140, rot=0):
    return f'<div class="a neu" style="left:{l}px;top:{y}px;font-size:{sz}px;transform:rotate({rot}deg)"><span {"data-x" if x else ""}>{t}</span></div>'

def P(title, size, inner):
    return page('P', f'<div class="a cav" style="left:190px;top:255px;font-size:{size}px;transform:rotate(-2deg)"><span data-u>{title}</span></div>' + inner)

def checklist(items, top, size=44, sub=31, gap=22):
    li = ''.join(f'<div style="margin:0 0 {gap}px 60px"><span class="neu" data-box style="font-size:{size}px">{a}</span>'
                 f'<div class="bad br" style="font-size:{sub}px;margin-top:2px">{b}</div></div>' for a, b in items)
    return f'<div class="a" style="left:190px;top:{top}px;width:740px">{li}</div>'

S = []
# 1
S.append(T('Це нудно…', 'zzz…',
    L(610, 'Зроби аналітику продажів', True, rot=1) + L(690, 'Зроби аналітику продажів', True, rot=-1) + L(770, 'Зроби аналітику продажів', rot=.5),
    'і щоразу загальні фрази замість висновків'))
# 2
S.append(P('Додайте в промпт:', 94, checklist([
    ('роль', '«ти аналітик онлайн-магазину»'),
    ('дані', '«ось таблиця продажів за жовтень»'),
    ('формат', '«3 головні висновки і 3 дії»'),
    ('тон', '«простими словами, з цифрами»'),
    ('приклад', '«ось звіт, який мені сподобався»'),
    ('чого не писати', '«без “продажі демонструють динаміку”»')], 410, gap=16) +
    '<div class="a bad" style="left:430px;top:1105px;font-size:36px;transform:rotate(-3deg)">і висновки, з якими<br>можна працювати</div>'
    '<i data-ar="360,1075,420,1135,-40,20"></i>'))
# 3
flow = '''<div class="a neu" style="left:150px;top:640px;font-size:54px"><span data-c="#231c17">пошта</span></div>
<div class="a neu" style="left:440px;top:640px;font-size:54px"><span data-c="#231c17">таблиця</span></div>
<div class="a neu" style="left:790px;top:640px;font-size:54px"><span data-c="#231c17">звіт</span></div>
<div class="a bad rd" style="left:330px;top:745px;font-size:32px;transform:rotate(4deg)">Ctrl+C<br>Ctrl+V</div>
<div class="a bad rd" style="left:660px;top:745px;font-size:32px;transform:rotate(-3deg)">Ctrl+C<br>Ctrl+V</div>
<i data-ar="320,676,410,672,0,-12"></i><i data-ar="660,676,760,672,0,-12"></i>'''
S.append(T('Це нудно…', 'знову', flow, 'щоп\'ятниці, 2 години вручну'))
# 4
svc = ['Google Drive', 'Gmail', 'Календар', 'Notion', 'Slack', 'Telegram']
sv = ''.join(f'<span class="neu" style="display:inline-block;font-size:52px;margin:0 44px 30px 0;transform:rotate({random.Random(i).uniform(-3,3):.1f}deg)" {"data-c" if i in (1, 2) else ""}>{s}</span>' for i, s in enumerate(svc))
ex = ['сам збирає звіт з таблиці', 'пише чернетки відповідей на листи', 'нагадує, що у вас сьогодні в календарі']
exl = ''.join(f'<div class="neu" data-box style="font-size:42px;margin:0 0 26px 60px">{e}</div>' for e in ex)
S.append(P('Підключіть:', 110, f'<div class="a" style="left:200px;top:420px;width:700px">{sv}</div>'
    '<div class="a bad br" style="left:200px;top:690px;font-size:46px;transform:rotate(-2deg)">і AI сам:</div>'
    f'<div class="a" style="left:200px;top:790px;width:720px">{exl}</div>'))
# 5
a1, a2 = 'Я діджитал-маркетолог онлайн-магазину,', 'веду рекламу в Meta, пиши коротко і з цифрами…'
S.append(T('Це нудно…', 'вдесяте',
    f'<div class="a neu" style="left:140px;top:600px;font-size:35px;transform:rotate(1deg)"><span data-x>{a1}</span><br><span data-x>{a2}</span></div>'
    f'<div class="a neu" style="left:140px;top:750px;font-size:35px;transform:rotate(-1deg)">{a1}<br>{a2}</div>',
    'і так у кожному новому чаті'))
# 6
S.append(P('Збережіть:', 110, checklist([
    ('власні інструкції', 'хто ви і як із вами працювати'),
    ('Проєкти', 'файли й контекст однієї задачі'),
    ('скіли', 'інструкції для задач, які повторюються'),
    ('пам\'ять', 'AI пам\'ятає попередні розмови')], 420, sub=30, gap=18) +
    '<div class="a neu" style="left:200px;top:900px;width:700px;font-size:38px;transform:rotate(1deg)"><span class="br">Ви:</span> «Підсумуй рекламу за тиждень»</div>'
    '<div class="a neu" style="left:200px;top:1020px;width:700px;font-size:38px;transform:rotate(-1deg)"><span class="br">AI:</span> Готово. Коротко, з цифрами і у вашому стилі.</div>'
    '<div class="a bad" style="left:220px;top:1150px;font-size:34px;transform:rotate(-2deg)">і пояснювати нічого не треба</div>'))
# 7
S.append(page('P', '''<div class="a cav" style="left:190px;top:310px;font-size:118px;line-height:.95;transform:rotate(-2deg)">AI нудний,<br><span class="br">поки ви його<br>не налаштуєте</span></div>
<div class="a neu" style="left:200px;top:760px;width:680px;font-size:40px">Розпишіть задачу в промпті, підключіть сервіси, збережіть налаштування. І AI працює на вас.</div>
<div class="a bad br" style="left:200px;top:1010px;font-size:36px;transform:rotate(-3deg)"><span data-u="#8C5A2B">збережіть, щоб спробувати</span></div>
<div class="a ink" style="left:700px;top:1110px;display:flex;align-items:center;gap:10px;opacity:.85;transform:rotate(-6deg)"><img src="crest.svg" style="height:56px"><img src="letters.svg" style="height:22px"></div>'''))
for i, h in enumerate(S, 1): open(f'v3_{i}.html', 'w').write(h)
