# Generates carousel.html: 6 slides 1080x1350, "ЦЕ ●●● СКУЧНО…" / "БЕЗ ЦЬОГО:" in Kraken purple
OUT = '/home/user/DJUN/kraken-boring-carousel/carousel.html'

I = {  # simple stroke icons, viewBox 0 0 48 48
    'key': '<circle cx="16" cy="24" r="8"/><path d="M24 24h18M36 24v7M42 24v5"/>',
    'phone': '<rect x="14" y="5" width="20" height="38" rx="4"/><path d="M21 37h6"/><path d="M19 20l4 4 7-8"/>',
    'lock': '<rect x="10" y="21" width="28" height="21" rx="4"/><path d="M16 21v-6a8 8 0 0 1 16 0v6"/><path d="M24 29v6"/>',
    'list': '<path d="M18 13h22M18 24h22M18 35h22"/><path d="M7 13l2.5 2.5L14 11M7 24l2.5 2.5L14 22M7 35l2.5 2.5L14 33"/>',
    'bell': '<path d="M12 33V22a12 12 0 0 1 24 0v11l3 4H9z"/><path d="M20 41a4 4 0 0 0 8 0"/>',
    'shield': '<path d="M24 5l15 6v11c0 10-6.5 17-15 21C15.5 39 9 32 9 22V11z"/><path d="M17 23l5 5 9-10"/>',
    'limit': '<path d="M6 36l10-10 8 6 12-16 6 4"/><path d="M6 16h36" stroke-dasharray="3 4"/>',
    'stop': '<path d="M6 14l10 8 8-4 12 14"/><path d="M6 36h36" stroke-dasharray="3 4"/><circle cx="36" cy="36" r="3"/>',
    'take': '<path d="M6 38l10-10 8 4 14-18"/><path d="M6 12h36" stroke-dasharray="3 4"/><circle cx="38" cy="12" r="3"/>',
    'trail': '<path d="M6 34l8-8 6 4 8-12 6 4 8-10"/><path d="M6 42l8-8 6 4 8-12 6 4 8-10" stroke-dasharray="3 4"/>',
    'trigger': '<path d="M27 4L12 27h11l-2 17 15-23H25z"/>',
    'chart': '<path d="M10 8v32M30 6v28"/><rect x="7" y="14" width="6" height="16" rx="1"/><rect x="27" y="12" width="6" height="14" rx="1"/><path d="M20 12v24M40 16v18"/>',
    'clock': '<circle cx="24" cy="24" r="17"/><path d="M24 14v10l7 5"/>',
    'pie': '<path d="M22 8a16 16 0 1 0 18 18H22z"/><path d="M27 4v17h17A17 17 0 0 0 27 4z"/>',
}


def ic(n, c='#6B3FF5', s=60):
    return (f'<svg viewBox="0 0 48 48" width="{s}" height="{s}" fill="none" stroke="{c}" stroke-width="3" '
            f'stroke-linecap="round" stroke-linejoin="round">{I[n]}</svg>')


def chip(n, label, ticker=None):
    inner = f'<b class="tk">{ticker}</b>' if ticker else ic(n)
    return f'<div class="ing"><div class="ball">{inner}</div><span>{label}</span></div>'


def sticky():
    return '<div class="sticky"><span>пароль:</span>123456</div>'


def mbtn():
    return '<div class="mbtn"><i>за ринком</i>Купити</div>'


def board():
    return f'<div class="board">{ic("clock", "#FF6B6B", 64)}<b>Ринок<br>закрито</b><small>відкриється вранці</small></div>'


def shieldres(t, sub, n):
    dots = ''.join('<i></i>' for _ in range(n))
    return (f'<div class="res"><div class="rsh">{ic("shield", "#fff", 110)}</div>'
            f'<div class="rdots">{dots}</div><b>{t}</b><small>{sub}</small></div>')


def chartres(t, lines):
    L = ''
    if 'tp' in lines:
        L += '<line x1="10" y1="40" x2="250" y2="40" class="tp"/><text x="250" y="30" class="lt" text-anchor="end">TP</text>'
    if 'lim' in lines:
        L += '<line x1="10" y1="118" x2="250" y2="118" class="lim"/><text x="250" y="108" class="lt" text-anchor="end">LIMIT</text>'
    if 'sl' in lines:
        L += '<line x1="10" y1="168" x2="250" y2="168" class="sl"/><text x="250" y="190" class="lt" text-anchor="end">SL</text>'
    if 'trail' in lines:
        L += ('<polyline points="10,178 70,178 70,158 140,158 140,134 200,134 200,112 250,112" class="trl"/>'
              '<text x="250" y="102" class="lt" text-anchor="end">TRAIL</text>')
    return (f'<div class="res card"><svg viewBox="0 0 260 200" width="260" height="200">'
            f'<polyline points="10,150 45,130 75,140 110,95 140,105 175,70 210,80 250,55" class="px"/>{L}</svg>'
            f'<b>{t}</b></div>')


def stockres(t, tks):
    c = ''.join(f'<span>{x}</span>' for x in tks)
    return f'<div class="res card"><div class="tks">{c}</div><b>{t}</b></div>'


def slideA(item):
    return (f'<section class="s a"><h2 class="ce">ЦЕ</h2><div class="row">{item}{item}{item}</div>'
            f'<h2 class="sk">СКУЧНО…</h2><img class="lg" src="logo.svg"></section>')


def slideB(ings, res, disc=''):
    d = f'<p class="disc">{disc}</p>' if disc else ''
    return (f'<section class="s b"><h2 class="bz">БЕЗ ЦЬОГО:</h2><div class="grid">{"".join(ings)}</div>'
            f'<div class="rrow">{"".join(res)}</div>{d}<img class="lg" src="logo.svg"></section>')


S = [
    slideA(sticky()),
    slideB([chip('key', 'Passkey'), chip('phone', '2FA'), chip('lock', 'Блокування налаштувань'),
            chip('list', 'Білий список адрес'), chip('bell', 'Сповіщення про вхід'), chip('shield', 'Підтвердження виводу')],
           [shieldres('Базовий', 'Passkey + 2FA', 2), shieldres('Посилений', '+ блокування', 3),
            shieldres('Максимум', '+ білий список', 4)]),
    slideA(mbtn()),
    slideB([chip('limit', 'Лімітний ордер'), chip('stop', 'Стоп-лосс'), chip('take', 'Тейк-профіт'),
            chip('trail', 'Трейлінг-стоп'), chip('trigger', 'Тригер-ордер'), chip('chart', 'Індикатори')],
           [chartres('Ліміт + стоп', ['lim', 'sl']), chartres('Стоп + тейк', ['sl', 'tp']),
            chartres('Трейлінг-стоп', ['trail'])]),
    slideA(board()),
    slideB([chip('clock', 'Торгівля 24/5'), chip('pie', 'Частки акцій'), chip('', 'NVIDIA', 'NVDAx'),
            chip('', 'Apple', 'AAPLx'), chip('', 'Tesla', 'TSLAx'), chip('', 'S&amp;P 500', 'SPYx')],
           [stockres('Технології', ['NVDAx', 'AAPLx']), stockres('Індекс', ['SPYx']),
            stockres('Мікс', ['TSLAx', 'SPYx', 'NVDAx'])],
           'Не є інвестиційною порадою. Торгівля пов’язана з ризиком. Доступність залежить від регіону.'),
]

CSS = '''*{margin:0;padding:0;box-sizing:border-box}body{font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased;background:#222}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:#7B5CF0;color:#fff}
.lg{position:absolute;left:50%;transform:translateX(-50%);bottom:42px;width:180px;opacity:.9}
h2{position:absolute;font-weight:300;letter-spacing:-2px;line-height:1}
.ce{left:150px;top:190px;font-size:230px}.sk{left:220px;top:930px;font-size:150px}
.row{position:absolute;left:0;right:0;top:470px;height:400px;display:flex;justify-content:center;align-items:center;gap:40px}
.sticky{width:290px;height:290px;background:#FFE26A;color:#2b2410;transform:rotate(-4deg);box-shadow:0 30px 50px rgba(30,10,80,.35);display:flex;flex-direction:column;justify-content:center;padding:0 30px;font-weight:600;font-size:60px;line-height:1;letter-spacing:-2px}
.sticky span{font-size:30px;font-weight:500;margin-bottom:14px;opacity:.7;letter-spacing:0}
.row .sticky:nth-child(2){transform:rotate(3deg)}.row .sticky:nth-child(3){transform:rotate(-2deg)}
.mbtn{width:290px;height:160px;border-radius:30px;background:#2FBF71;box-shadow:0 30px 50px rgba(30,10,80,.35),inset 0 -8px 0 rgba(0,0,0,.15);display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:600;font-size:62px;line-height:1;letter-spacing:-1.5px}
.mbtn i{font-style:normal;font-size:26px;font-weight:500;opacity:.85;margin-bottom:10px;letter-spacing:0}
.board{width:300px;height:330px;border-radius:30px;background:#17151f;box-shadow:0 30px 50px rgba(30,10,80,.35);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;text-align:center}
.board b{font-size:50px;font-weight:600;letter-spacing:-1.5px;line-height:1.05;color:#FF6B6B}.board small{font-size:24px;color:#9b98aa}
.bz{left:90px;top:150px;font-size:128px}
.grid{position:absolute;left:70px;right:70px;top:350px;display:grid;grid-template-columns:repeat(3,1fr);row-gap:40px}
.ing{display:flex;flex-direction:column;align-items:center;gap:16px;text-align:center}
.ball{width:136px;height:136px;border-radius:50%;background:#fff;display:grid;place-items:center;box-shadow:0 18px 34px rgba(30,10,80,.3)}
.tk{font-size:30px;font-weight:700;color:#6B3FF5;letter-spacing:-.5px}
.ing span{font-size:32px;font-weight:400;line-height:1.15;max-width:290px}
.rrow{position:absolute;left:50px;right:50px;top:905px;display:flex;justify-content:space-between}
.res{width:300px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px}
.res b{font-size:36px;font-weight:500;letter-spacing:-.5px}.res small{font-size:26px;opacity:.8}
.rsh{width:160px;height:160px;border-radius:50%;background:rgba(255,255,255,.14);display:grid;place-items:center}
.rdots{display:flex;gap:10px}.rdots i{width:14px;height:14px;border-radius:50%;background:#fff}
.card{background:#17151f;border-radius:28px;padding:22px 18px 24px;box-shadow:0 24px 44px rgba(30,10,80,.35)}
.px{fill:none;stroke:#fff;stroke-width:4;stroke-linejoin:round}
.tp{stroke:#2FBF71;stroke-width:3;stroke-dasharray:8 7}.sl{stroke:#FF6B6B;stroke-width:3;stroke-dasharray:8 7}.lim{stroke:#B7A3FF;stroke-width:3;stroke-dasharray:8 7}
.trl{fill:none;stroke:#FF9F5A;stroke-width:3;stroke-dasharray:8 7}.lt{fill:#cfcbe0;font-weight:600;font-size:18px;font-family:Inter}
.tks{height:200px;display:flex;flex-wrap:wrap;align-content:center;justify-content:center;gap:12px}
.tks span{background:#fff;color:#6B3FF5;border-radius:999px;padding:10px 18px;font-size:28px;font-weight:700}
.disc{position:absolute;left:70px;right:70px;bottom:96px;text-align:center;font-size:19px;color:rgba(255,255,255,.75)}
'''

with open(OUT, 'w', encoding='utf8') as f:
    f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(S)}</body></html>')
print('ok')
