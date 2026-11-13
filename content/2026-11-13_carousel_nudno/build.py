# Carousel «Це нудно…» про AI: 7 slides 1080x1350, one brand colour, thin uppercase type, cut-out objects.
import pathlib
HERE = pathlib.Path(__file__).parent
SP = pathlib.Path("/tmp/claude-0/-home-user-DJUN/777dd743-7ffe-5505-9410-2959c9da1eb7/scratchpad/fonts")
SK = pathlib.Path("/root/.claude/skills/synced/1eb15ba8-9e80-49cb-a1e0-90964f7bdb55_9f9c214f-933c-41c1-8626-dc01b4556c28/djun-design/assets")
BG, INK, BEIGE, BROWN, MUTED = "#714326", "#190F09", "#EFE7DF", "#A16E3B", "#8C7B6B"
def ff(n, p, w="400", s="normal"): return f'@font-face{{font-family:"{n}";src:url("{p.as_uri()}");font-weight:{w};font-style:{s}}}'
F = "".join([ff("Mont", SK/"fonts/Montserrat.ttf", "100 900"),
    ff("Hand", SP/"fontsource-caveat/files/caveat-cyrillic-600-normal.woff2", "600"),
    ff("Serif", SP/"fontsource-playfair-display/files/playfair-display-cyrillic-400-italic.woff2", "400", "italic"),
    ff("Serif", SP/"fontsource-playfair-display/files/playfair-display-latin-400-italic.woff2", "400", "italic")])
CSS = f"""{F}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{BG};font-family:Mont;color:#fff}}
.grain{{position:absolute;inset:0;mix-blend-mode:multiply;opacity:.5}}
.abs{{position:absolute}}
.logo{{position:absolute;left:70px;top:64px;display:flex;align-items:center;gap:12px;opacity:.95}}
.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}
.logo small{{font:700 10px/1 Mont;letter-spacing:.2em;color:{BEIGE};margin-top:5px;margin-right:-.2em}}
.thin{{position:absolute;font:300 210px/1 Mont;letter-spacing:.02em;text-transform:uppercase;color:#fff}}
.ttl{{position:absolute;left:70px;top:170px;font:300 92px/1 Mont;text-transform:uppercase;letter-spacing:.01em;color:#fff}}
.card{{position:absolute;background:#fff;border-radius:26px;color:{INK};box-shadow:0 18px 30px rgba(25,15,9,.28)}}
.bub{{background:{BEIGE};border-radius:20px 20px 4px 20px;padding:16px 18px;font:600 26px/1.2 Mont;color:{INK}}}
.ln{{height:12px;border-radius:6px;background:#D9D2CA;margin-top:12px}}
.ing{{position:absolute;width:300px;text-align:center}}
.ing .ic{{width:132px;height:132px;margin:0 auto;border-radius:50%;background:{BEIGE};display:flex;align-items:center;justify-content:center;box-shadow:0 12px 22px rgba(25,15,9,.25)}}
.ing .lb{{font:400 30px/1.1 Mont;margin-top:14px;color:#fff}}
.res{{position:absolute;width:300px;height:330px;background:#fff;border-radius:26px;color:{INK};padding:26px;box-shadow:0 18px 30px rgba(25,15,9,.28)}}
.res .k{{font:700 18px/1 Mont;letter-spacing:.14em;text-transform:uppercase;color:{BROWN}}}
.res .t{{font:700 30px/1.15 Mont;margin-top:12px;letter-spacing:-.01em}}
.chip{{display:inline-block;padding:8px 14px;border-radius:999px;background:{BEIGE};font:700 18px/1 Mont;margin:4px 4px 0 0}}
svg.i path,svg.i rect,svg.i circle,svg.i line,svg.i polyline{{fill:none;stroke:{INK};stroke-width:5;stroke-linecap:round;stroke-linejoin:round}}
"""
GRAIN = ('<svg class="grain" width="1080" height="1350"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2"/>'
         '<feColorMatrix values="0 0 0 0 .3  0 0 0 0 .2  0 0 0 0 .12  0 0 0 .3 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
LOGO = (f'<div class="logo"><img src="{(SK/"logo/crest_onbrown.svg").as_uri()}" style="height:46px">'
        f'<span class="w"><img src="{(SK/"logo/letters_onbrown.svg").as_uri()}" style="height:19px"><small>AI академія</small></span></div>')
def page(b): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{GRAIN}{LOGO}{b}</body></html>'
def icon(d, s=72): return f'<svg class="i" width="{s}" height="{s}" viewBox="0 0 72 72">{d}</svg>'

IC = {
 "роль": '<circle cx="36" cy="26" r="12"/><path d="M14,62 C16,46 56,46 58,62"/><path d="M26,20 h20"/>',
 "аудиторія": '<circle cx="24" cy="28" r="9"/><circle cx="48" cy="28" r="9"/><path d="M8,58 C10,46 38,46 40,58"/><path d="M32,58 C34,46 62,46 64,58"/>',
 "приклад тексту": '<rect x="16" y="10" width="40" height="52" rx="4"/><line x1="24" y1="24" x2="48" y2="24"/><line x1="24" y1="34" x2="48" y2="34"/><line x1="24" y1="44" x2="40" y2="44"/>',
 "формат": '<rect x="10" y="12" width="22" height="22" rx="3"/><rect x="40" y="12" width="22" height="22" rx="3"/><rect x="10" y="40" width="52" height="20" rx="3"/>',
 "тон": '<path d="M10,36 h6 l6,-14 l8,28 l8,-22 l6,12 l6,-6 h12"/>',
 "чого не писати": '<circle cx="36" cy="36" r="24"/><line x1="19" y1="19" x2="53" y2="53"/>',
 "Google Drive": '<path d="M26,12 h20 l18,30 l-10,18 h-36 l-10,-18z"/><line x1="26" y1="12" x2="44" y2="42"/>',
 "Gmail": '<rect x="10" y="18" width="52" height="36" rx="4"/><polyline points="10,20 36,40 62,20"/>',
 "Календар": '<rect x="12" y="16" width="48" height="44" rx="5"/><line x1="12" y1="30" x2="60" y2="30"/><line x1="24" y1="10" x2="24" y2="22"/><line x1="48" y1="10" x2="48" y2="22"/>',
 "Notion": '<rect x="14" y="12" width="44" height="48" rx="4"/><path d="M26,48 V24 L46,48 V24"/>',
 "Slack": '<line x1="28" y1="12" x2="24" y2="60"/><line x1="48" y1="12" x2="44" y2="60"/><line x1="12" y1="28" x2="60" y2="28"/><line x1="12" y1="46" x2="60" y2="46"/>',
 "Telegram-бот": '<path d="M10,34 L62,12 L52,60 L34,46 L26,58 L24,42z"/><line x1="24" y1="42" x2="62" y2="12"/>',
 "власні інструкції": '<rect x="14" y="10" width="44" height="52" rx="4"/><polyline points="22,26 26,30 34,22"/><line x1="38" y1="26" x2="50" y2="26"/><polyline points="22,42 26,46 34,38"/><line x1="38" y1="42" x2="50" y2="42"/>',
 "Проєкти": '<path d="M8,22 h20 l6,6 h30 v32 h-56z"/>',
 "скіли": '<path d="M36,8 l8,18 l20,2 l-15,13 l5,20 l-18,-11 l-18,11 l5,-20 l-15,-13 l20,-2z"/>',
 "пам'ять": '<path d="M24,14 C12,14 8,26 12,34 C6,40 10,54 22,54 C24,62 34,62 36,56 C38,62 48,62 50,54 C62,54 66,40 60,34 C64,26 60,14 48,14 C46,8 38,8 36,14 C34,8 26,8 24,14z"/><line x1="36" y1="14" x2="36" y2="56"/>',
}

def boring(objects_html):
    return page(f'<div class="thin" style="left:150px;top:170px">це</div>{objects_html}<div class="thin" style="left:230px;top:960px;font-size:150px">нудно…</div>')

def trio(inner, w=300, h=380, top=470):
    return "".join(f'<div class="card" style="left:{50+i*335}px;top:{top}px;width:{w}px;height:{h}px;padding:24px;transform:rotate({(-2,1,-1)[i]}deg)">{inner}</div>' for i in range(3))

def ingredients(title, items, results, ttl_size=84):
    cols = 3; out = [f'<div class="ttl" style="font-size:{ttl_size}px">{title}</div>']
    for k, name in enumerate(items):
        r, c = divmod(k, cols)
        out.append(f'<div class="ing" style="left:{40+c*340}px;top:{330+r*230}px"><div class="ic">{icon(IC[name])}</div><div class="lb">{name}</div></div>')
    for k, (kind, title2, extra) in enumerate(results):
        out.append(f'<div class="res" style="left:{40+k*340}px;top:{800 if len(items)>3 else 640}px"><div class="k">{kind}</div><div class="t">{title2}</div>{extra}</div>')
    return page("".join(out))

lines = '<div class="ln" style="width:90%"></div><div class="ln" style="width:80%"></div><div class="ln" style="width:86%"></div><div class="ln" style="width:60%"></div>'
S = {}
S["01"] = boring(trio(f'<div class="bub">Напиши пост про AI</div><div style="margin-top:26px;font:700 16px/1 Mont;letter-spacing:.14em;color:{MUTED}">AI</div>{lines}<div class="ln" style="width:75%"></div><div class="ln" style="width:50%"></div>'))
S["02"] = ingredients("додайте в промпт:", ["роль", "аудиторія", "приклад тексту", "формат", "тон", "чого не писати"], [
   ("Instagram", "Карусель для власниць кав'ярень", '<div style="display:flex;gap:8px;margin-top:22px">' + "".join(f'<div style="flex:1;height:110px;border-radius:10px;background:{c}"></div>' for c in (BEIGE, "#D9C3A8", BEIGE)) + '</div>'),
   ("Лист", "Відповідь клієнту без канцеляриту", '<div style="margin-top:16px">' + lines + '</div>'),
   ("Реклама", "Текст оголошення на 3 рядки", f'<div style="margin-top:20px;padding:14px;border-radius:12px;background:{BEIGE};font:700 20px/1.2 Mont">-20% на перший курс</div><div style="margin-top:14px;display:inline-block;padding:10px 18px;border-radius:10px;background:{INK};color:#fff;font:700 18px Mont">Записатися</div>')])
grid = "".join(f'<div style="height:30px;border-bottom:2px solid #E3DCD4;display:flex">' + "".join('<div style="flex:1;border-right:2px solid #E3DCD4"></div>' for _ in range(4)) + '</div>' for _ in range(5))
S["03"] = boring(trio(f'<div style="border:2px solid #E3DCD4;border-radius:8px;overflow:hidden">{grid}</div><div style="text-align:center;font:800 40px/1 Mont;margin:18px 0 8px;color:{BROWN}">↓</div><div class="bub" style="text-align:center">Ctrl+C<br>Ctrl+V</div>'))
S["04"] = ingredients("підключіть:", ["Google Drive", "Gmail", "Календар", "Notion", "Slack", "Telegram-бот"], [
   ("Звіти", "Звіт з таблиць збирається сам", f'<div style="display:flex;align-items:flex-end;gap:10px;height:120px;margin-top:20px">' + "".join(f'<div style="flex:1;height:{h}%;background:{c};border-radius:6px 6px 0 0"></div>' for h, c in ((40, BEIGE), (65, "#D9C3A8"), (55, BEIGE), (90, BROWN))) + '</div>'),
   ("Пошта", "Чернетки відповідей на листи", '<div style="margin-top:16px">' + lines + '</div>'),
   ("День", "План дня з календаря", "".join(f'<div style="margin-top:12px;display:flex;gap:10px;font:600 20px Mont"><span style="color:{BROWN}">{t}</span><span>{x}</span></div>' for t, x in (("09:00", "дзвінок"), ("12:00", "звіт"), ("16:00", "пости"))))], ttl_size=110)
S["05"] = boring(trio('<div class="bub" style="font-size:24px">Нагадую: у мене кав\'ярня, пиши коротко, без емодзі, тон дружній…</div>', h=330, top=500))
S["06"] = ingredients("збережіть:", ["власні інструкції", "Проєкти", "скіли", "пам'ять"][:3] + [], [], ttl_size=110)
# slide 6: 4 items in a row + one wide result card
items6 = ["власні інструкції", "Проєкти", "скіли", "пам'ять"]
b6 = ['<div class="ttl" style="font-size:110px">збережіть:</div>']
for k, n in enumerate(items6):
    b6.append(f'<div class="ing" style="left:{40+k*250}px;top:340px;width:250px"><div class="ic">{icon(IC[n])}</div><div class="lb">{n}</div></div>')
b6.append(f'''<div class="card" style="left:70px;top:680px;width:940px;height:440px;padding:40px">
  <div style="display:flex;justify-content:flex-end"><div class="bub" style="font-size:30px">Пост на завтра?</div></div>
  <div style="margin-top:28px;max-width:720px;background:{INK};color:{BEIGE};border-radius:20px 20px 20px 4px;padding:22px 26px;font:500 30px/1.3 Mont">Готово. Коротко, дружнім тоном, без емодзі, з акцією на капучино, як ви любите.</div>
  <div style="margin-top:26px;font:600 34px/1 Hand;color:{BROWN}">AI вже знає ваш бренд з першого повідомлення</div></div>''')
S["06"] = page("".join(b6))
S["07"] = page(f'''<div class="thin" style="left:70px;top:300px;font-size:120px;line-height:1.05">AI нудний,</div>
  <div class="abs" style="left:70px;top:450px;width:940px;font:italic 400 118px/1.02 Serif;color:{BEIGE}">поки ви його не налаштуєте</div>
  <div class="abs" style="left:70px;top:820px;width:900px;font:400 36px/1.4 Mont;color:{BEIGE}">Промпт з контекстом, підключені сервіси і збережені налаштування. Три кроки, і AI працює на вас.</div>
  <div class="abs" style="left:70px;top:1100px;font:600 54px/1 Hand;color:{BEIGE};transform:rotate(-2deg)">збережіть, щоб спробувати →</div>''')
out = HERE / "html"; out.mkdir(exist_ok=True)
for k, v in S.items(): (out / f"slide_{k}.html").write_text(v, encoding="utf-8")
print("ok")
