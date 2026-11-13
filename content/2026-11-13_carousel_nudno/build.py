# Carousel «Це нудно…» v2: dark "boring" slides, light "fix" slides, phone mockups, real photos, no mustard.
import pathlib
HERE = pathlib.Path(__file__).parent
SP = pathlib.Path("/tmp/claude-0/-home-user-DJUN/777dd743-7ffe-5505-9410-2959c9da1eb7/scratchpad/fonts")
SK = pathlib.Path("/root/.claude/skills/synced/1eb15ba8-9e80-49cb-a1e0-90964f7bdb55_9f9c214f-933c-41c1-8626-dc01b4556c28/djun-design/assets")
PH = lambda n: (SK / "photos" / n).as_uri()
DARK, LIGHT, INK, GREY, LINE = "#141210", "#F6F3EF", "#141210", "#8E8780", "#E4DED7"
def ff(n, p, w="400", s="normal"): return f'@font-face{{font-family:"{n}";src:url("{p.as_uri()}");font-weight:{w};font-style:{s}}}'
F = "".join([ff("Mont", SK/"fonts/Montserrat.ttf", "100 900"),
    ff("Hand", SP/"fontsource-caveat/files/caveat-cyrillic-600-normal.woff2", "600"),
    ff("Hand", SP/"fontsource-caveat/files/caveat-latin-600-normal.woff2", "600"),
    ff("Serif", SP/"fontsource-playfair-display/files/playfair-display-cyrillic-400-italic.woff2", "400", "italic"),
    ff("Serif", SP/"fontsource-playfair-display/files/playfair-display-latin-400-italic.woff2", "400", "italic")])
CSS = f"""{F}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Mont}}
body.dark{{background:{DARK};color:#fff}} body.light{{background:{LIGHT};color:{INK}}}
.abs{{position:absolute}}
.bgph{{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.1);opacity:.22}}
.grain{{position:absolute;inset:0;mix-blend-mode:overlay;opacity:.35}}
.logo{{position:absolute;left:70px;top:64px;display:flex;align-items:center;gap:12px}}
.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}
.logo small{{font:700 10px/1 Mont;letter-spacing:.2em;margin-top:5px;margin-right:-.2em}}
.dark .logo small{{color:#cfc8c0}} .light .logo small{{color:{GREY}}}
.thin{{position:absolute;font:200 220px/1 Mont;text-transform:uppercase;letter-spacing:.02em}}
.ttl{{position:absolute;left:70px;top:160px;font:200 96px/1 Mont;text-transform:uppercase}}
.hand{{position:absolute;font:600 48px/1 Hand}}
.phone{{position:absolute;width:290px;height:560px;border-radius:44px;background:#0b0a09;padding:12px;box-shadow:0 30px 50px rgba(0,0,0,.45)}}
.light .phone{{box-shadow:0 30px 50px rgba(20,18,16,.25)}}
.scr{{width:100%;height:100%;border-radius:34px;background:#fff;overflow:hidden;position:relative;padding:44px 18px 18px;color:{INK}}}
.notch{{position:absolute;top:10px;left:50%;width:90px;height:22px;margin-left:-45px;border-radius:12px;background:#0b0a09}}
.me{{margin-left:auto;max-width:92%;background:{INK};color:#fff;border-radius:18px 18px 4px 18px;padding:12px 14px;font:600 19px/1.25 Mont}}
.ai{{margin-top:14px;max-width:95%;background:#EEEAE5;border-radius:18px 18px 18px 4px;padding:14px;font:500 17px/1.3 Mont}}
.ln{{height:9px;border-radius:5px;background:#D6D0C9;margin:9px 0}}
.chip{{position:absolute;display:flex;align-items:center;gap:14px;padding:14px 26px 14px 14px;border-radius:999px;background:#fff;font:600 30px/1 Mont;color:{INK};box-shadow:0 10px 24px rgba(20,18,16,.12)}}
.chip .ic{{width:58px;height:58px;border-radius:50%;background:{INK};display:flex;align-items:center;justify-content:center}}
svg.i *{{fill:none;stroke:#fff;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}}
svg.wire path{{fill:none;stroke:{INK};stroke-width:3;stroke-dasharray:8 10;stroke-linecap:round}}
.tag{{display:inline-block;font:700 14px/1 Mont;letter-spacing:.16em;text-transform:uppercase;color:{GREY}}}
.polar{{position:absolute;background:#fff;padding:16px 16px 60px;box-shadow:0 20px 40px rgba(20,18,16,.18)}}
.polar div{{width:100%;height:100%;background-size:cover;background-position:center}}
"""
GRAIN = ('<svg class="grain" width="1080" height="1350"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2"/></filter>'
         '<rect width="100%" height="100%" filter="url(#n)" opacity=".5"/></svg>')
def logo(dark): 
    suf = "_light" if dark else ""
    return (f'<div class="logo"><img src="{(SK/f"logo/crest{suf}.svg").as_uri()}" style="height:46px">'
            f'<span class="w"><img src="{(SK/f"logo/letters{suf}.svg").as_uri()}" style="height:19px"><small>AI академія</small></span></div>')
def page(body, dark, photo=None):
    bg = f'<div class="bgph" style="background-image:url({PH(photo)})"></div>' if photo else ""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{"dark" if dark else "light"}">{bg}{GRAIN}{logo(dark)}{body}</body></html>'
def icon(d): return f'<svg class="i" width="34" height="34" viewBox="0 0 72 72">{d}</svg>'
IC = {
 "роль": '<circle cx="36" cy="26" r="12"/><path d="M14,62 C16,46 56,46 58,62"/>',
 "аудиторія": '<circle cx="24" cy="28" r="9"/><circle cx="48" cy="28" r="9"/><path d="M8,58 C10,46 38,46 40,58"/><path d="M32,58 C34,46 62,46 64,58"/>',
 "приклад тексту": '<rect x="16" y="10" width="40" height="52" rx="4"/><line x1="24" y1="26" x2="48" y2="26"/><line x1="24" y1="38" x2="48" y2="38"/>',
 "формат": '<rect x="10" y="12" width="22" height="22" rx="3"/><rect x="40" y="12" width="22" height="22" rx="3"/><rect x="10" y="40" width="52" height="20" rx="3"/>',
 "тон": '<path d="M8,36 h8 l6,-14 l8,28 l8,-22 l6,12 l6,-6 h14"/>',
 "чого не писати": '<circle cx="36" cy="36" r="24"/><line x1="19" y1="19" x2="53" y2="53"/>',
 "Google Drive": '<path d="M26,12 h20 l18,30 l-10,18 h-36 l-10,-18z"/>',
 "Gmail": '<rect x="10" y="18" width="52" height="36" rx="4"/><polyline points="10,20 36,40 62,20"/>',
 "Календар": '<rect x="12" y="16" width="48" height="44" rx="5"/><line x1="12" y1="30" x2="60" y2="30"/>',
 "Notion": '<rect x="14" y="12" width="44" height="48" rx="4"/><path d="M26,48 V24 L46,48 V24"/>',
 "Slack": '<line x1="28" y1="12" x2="24" y2="60"/><line x1="48" y1="12" x2="44" y2="60"/><line x1="12" y1="28" x2="60" y2="28"/><line x1="12" y1="46" x2="60" y2="46"/>',
 "Telegram": '<path d="M10,34 L62,12 L52,60 L34,46 L26,58 L24,42z"/>',
 "інструкції": '<polyline points="16,26 22,32 32,20"/><line x1="40" y1="26" x2="58" y2="26"/><polyline points="16,46 22,52 32,40"/><line x1="40" y1="46" x2="58" y2="46"/>',
 "Проєкти": '<path d="M8,22 h20 l6,6 h30 v32 h-56z"/>',
 "скіли": '<path d="M36,8 l8,18 l20,2 l-15,13 l5,20 l-18,-11 l-18,11 l5,-20 l-15,-13 l20,-2z"/>',
 "пам'ять": '<path d="M24,14 C12,14 8,26 12,34 C6,40 10,54 22,54 C24,62 34,62 36,56 C38,62 48,62 50,54 C62,54 66,40 60,34 C64,26 60,14 48,14 C46,8 38,8 36,14 C34,8 26,8 24,14z"/>',
}
def chip(name, x, y, rot=0): return f'<div class="chip" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"><span class="ic">{icon(IC[name])}</span>{name}</div>'
def phone(x, y, inner, rot=0, scale=1.0): return f'<div class="phone" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({scale})"><div class="scr"><div class="notch"></div>{inner}</div></div>'
LINES = '<div class="ln" style="width:90%"></div><div class="ln" style="width:75%"></div><div class="ln" style="width:85%"></div><div class="ln" style="width:55%"></div>'

def boring(inner_per_phone, photo, note):
    phones = "".join(phone(70 + i * 320, 420, inner_per_phone, rot=(-4, 0, 4)[i]) for i in range(3))
    return page(f'''<div class="thin" style="left:150px;top:170px">це</div>{phones}
      <div class="thin" style="left:240px;top:1040px;font-size:160px">нудно…</div>
      <div class="hand" style="left:780px;top:250px;color:#cfc8c0;transform:rotate(-8deg)">{note}</div>''', True, photo)

S = {}
S["01"] = boring(f'<div class="me">Напиши пост про AI</div><div class="ai">AI відкриває безмежні можливості для вашого бізнесу…{LINES}</div>' + LINES, "bb_code_screen.jpg", "zzz…")
grid = "".join('<div style="display:flex;border-bottom:2px solid #E4DED7">' + "".join('<div style="flex:1;height:30px;border-right:2px solid #E4DED7"></div>' for _ in range(3)) + '</div>' for _ in range(7))
S["03"] = boring(f'<div style="border:2px solid #E4DED7;border-radius:8px;overflow:hidden">{grid}</div><div style="text-align:center;font:800 34px/1 Mont;margin:14px 0">↓</div><div class="me" style="margin:0 auto;text-align:center">Ctrl+C → Ctrl+V</div>', "bb_students_laptops.jpg", "знову…")
S["05"] = boring('<div class="me">Нагадую: у мене кав\'ярня, пиши коротко, без емодзі, тон дружній…</div><div class="ai">Зрозумів! Чим допомогти?</div><div class="me" style="margin-top:14px">Нагадую: у мене кав\'ярня…</div>', "bb_laptop_sofa.jpg", "вдесяте")

# --- 02: prompt ingredients + 3 different results in phones (one with a real photo)
ch2 = "".join(chip(n, x, y, r) for n, x, y, r in [("роль", 70, 330, -3), ("аудиторія", 360, 310, 2), ("приклад тексту", 690, 340, -2),
                                                   ("формат", 110, 440, 2), ("тон", 420, 430, -3), ("чого не писати", 620, 450, 3)])
p_insta = f'<div class="tag">Instagram</div><div style="margin-top:10px;height:230px;border-radius:12px;background:url({PH("bb_students_laptops.jpg")}) center/cover"></div><div style="font:700 18px/1.3 Mont;margin-top:12px">5 задач, які кав\'ярня може віддати AI вже сьогодні ☕</div>'
p_mail = f'<div class="tag">Лист клієнту</div><div style="font:700 19px/1.3 Mont;margin-top:12px">Добрий день, Олено!</div><div style="font:500 16px/1.4 Mont;margin-top:8px">Дякуємо, що написали. Ваше замовлення вже готове, заберіть його до 18:00…</div>{LINES}'
p_ad = f'<div class="tag">Реклама</div><div style="margin-top:10px;height:170px;border-radius:12px;background:url({PH("bb_laptop_sofa.jpg")}) center/cover"></div><div style="font:800 24px/1.15 Mont;margin-top:12px">Перший AI-асистент за 1 вечір</div><div style="margin-top:12px;padding:12px;border-radius:10px;background:{INK};color:#fff;text-align:center;font:700 16px Mont">Дізнатися більше</div>'
S["02"] = page(f'''<div class="ttl" style="font-size:80px">додайте в промпт:</div>{ch2}
  <div class="hand" style="left:70px;top:560px;color:{GREY};transform:rotate(-2deg)">і отримаєте ↓</div>
  {phone(60, 650, p_insta, -3, .95)}{phone(395, 630, p_mail, 0, .95)}{phone(730, 650, p_ad, 3, .95)}''', False)

# --- 04: connectors hub
hub_x, hub_y = 540, 610
pos = [("Google Drive", 70, 330), ("Gmail", 640, 320), ("Календар", 60, 560), ("Notion", 720, 560), ("Slack", 110, 780), ("Telegram", 680, 790)]
wires = "".join(f'<path d="M{hub_x},{hub_y} C{(hub_x+x+150)/2},{hub_y} {(hub_x+x+150)/2},{y+44} {x+150},{y+44}"/>' for _, x, y in pos)
ch4 = "".join(chip(n, x, y) for n, x, y in pos)
res4 = f'''<div class="abs" style="left:70px;top:1000px;width:940px;display:flex;gap:24px">
  <div style="flex:1;background:#fff;border-radius:22px;padding:22px;box-shadow:0 10px 24px rgba(20,18,16,.1)"><div class="tag">Звіти</div><div style="font:700 24px/1.2 Mont;margin-top:8px">Звіт з таблиць сам</div>
    <div style="display:flex;align-items:flex-end;gap:8px;height:80px;margin-top:12px">{"".join(f'<div style="flex:1;height:{h}%;background:{c};border-radius:4px 4px 0 0"></div>' for h,c in ((35,"#D6D0C9"),(60,"#D6D0C9"),(50,"#D6D0C9"),(95,INK)))}</div></div>
  <div style="flex:1;background:#fff;border-radius:22px;padding:22px;box-shadow:0 10px 24px rgba(20,18,16,.1)"><div class="tag">Пошта</div><div style="font:700 24px/1.2 Mont;margin-top:8px">Чернетки відповідей</div>{LINES}</div>
  <div style="flex:1;background:#fff;border-radius:22px;padding:22px;box-shadow:0 10px 24px rgba(20,18,16,.1)"><div class="tag">День</div><div style="font:700 24px/1.2 Mont;margin-top:8px">План з календаря</div>
    {"".join(f'<div style="display:flex;gap:10px;margin-top:9px;font:600 17px Mont"><b>{t}</b><span style="color:{GREY}">{x}</span></div>' for t,x in (("09:00","дзвінок"),("12:00","звіт"),("16:00","пости")))}</div></div>'''
S["04"] = page(f'''<div class="ttl">підключіть:</div>
  <svg class="wire abs" width="1080" height="1350" style="left:0;top:0">{wires}</svg>{ch4}
  <div class="abs" style="left:{hub_x-90}px;top:{hub_y-90}px;width:180px;height:180px;border-radius:50%;background:{INK};color:#fff;display:flex;align-items:center;justify-content:center;font:800 64px/1 Mont;box-shadow:0 20px 40px rgba(20,18,16,.3)">AI</div>
  {res4}''', False)

# --- 06: saved settings + big phone over a real photo
ch6 = "".join(chip(n, x, y, r) for n, x, y, r in [("інструкції", 70, 320, -2), ("Проєкти", 470, 300, 2), ("скіли", 110, 430, 2), ("пам'ять", 430, 420, -3)])
chat6 = f'<div class="me" style="font-size:22px">Пост на завтра?</div><div class="ai" style="font-size:20px">Готово ✅ Коротко, дружнім тоном, без емодзі, з акцією на капучино, як ви любите.</div><div class="ai" style="font-size:18px;color:{GREY}">Опублікувати о 9:00?</div>'
S["06"] = page(f'''<div class="ttl">збережіть:</div>{ch6}
  <div class="polar" style="left:520px;top:600px;width:500px;height:560px;transform:rotate(4deg)"><div style="background-image:url({PH("bb_laptop_sofa.jpg")})"></div></div>
  {phone(150, 640, chat6, -4, 1.05)}
  <div class="hand" style="left:560px;top:1210px;color:{INK};transform:rotate(-3deg)">AI вже знає ваш бренд</div>''', False)

# --- 07: final
S["07"] = page(f'''<div class="abs" style="left:70px;top:230px;font:200 120px/1 Mont;text-transform:uppercase">AI нудний,</div>
  <div class="abs" style="left:70px;top:370px;width:940px;font:italic 400 112px/1.02 Serif">поки ви його не налаштуєте</div>
  <div class="polar" style="left:90px;top:720px;width:400px;height:420px;transform:rotate(-4deg)"><div style="background-image:url({PH("bb_students_laptops.jpg")})"></div></div>
  <div class="abs" style="left:560px;top:760px;width:440px;font:500 32px/1.45 Mont">Промпт з контекстом. Підключені сервіси. Збережені налаштування.</div>
  <div class="hand" style="left:560px;top:1060px;transform:rotate(-3deg)">збережіть, щоб спробувати →</div>''', False)

out = HERE / "html"; out.mkdir(exist_ok=True)
for f in out.glob("*.html"): f.unlink()
for k, v in S.items(): (out / f"slide_{k}.html").write_text(v, encoding="utf-8")
print("ok")
