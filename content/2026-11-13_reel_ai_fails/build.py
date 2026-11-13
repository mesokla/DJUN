# Vertical 1080x1920 frames for the reel «5 задач, які я б поки не довіряв AI».
import pathlib, json
HERE = pathlib.Path(__file__).parent
SP = pathlib.Path("/tmp/claude-0/-home-user-DJUN/777dd743-7ffe-5505-9410-2959c9da1eb7/scratchpad/fonts")
SK = pathlib.Path("/root/.claude/skills/synced/1eb15ba8-9e80-49cb-a1e0-90964f7bdb55_9f9c214f-933c-41c1-8626-dc01b4556c28/djun-design/assets")
INK, BROWN, PAPER = "#190F09", "#A16E3B", "#F4EEE7"
S = lambda n: (HERE / "screens_trim" / f"{n}.png").as_uri()

def ff(name, path, weight="400", style="normal"):
    return f'@font-face{{font-family:"{name}";src:url("{path.as_uri()}");font-weight:{weight};font-style:{style}}}'
FONTS = "".join([ff("Mont", SK / "fonts/Montserrat.ttf", "100 900"),
    ff("Hand", SP / "fontsource-caveat/files/caveat-cyrillic-600-normal.woff2", "600"),
    ff("Hand", SP / "fontsource-caveat/files/caveat-latin-600-normal.woff2", "600"),
    ff("Serif", SP / "fontsource-playfair-display/files/playfair-display-cyrillic-400-italic.woff2", "400", "italic"),
    ff("Serif", SP / "fontsource-playfair-display/files/playfair-display-latin-400-italic.woff2", "400", "italic")])

CSS = f"""{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;position:relative;overflow:hidden;background:{PAPER};font-family:Mont;color:{INK}}}
body.dark{{background:{INK};color:#EFE7DF}}
.grain{{position:absolute;inset:0;mix-blend-mode:multiply;opacity:.55;pointer-events:none}}
.logo{{position:absolute;left:80px;top:250px;display:flex;align-items:center;gap:14px}}
.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}
.logo small{{font:700 11px/1 Mont;letter-spacing:.2em;color:{BROWN};margin-top:6px;margin-right:-.2em}}
.num{{position:absolute;left:70px;top:330px;font:italic 400 300px/1 Serif;color:{BROWN};opacity:.9}}
.title{{position:absolute;left:80px;top:640px;width:920px;font:800 92px/1.0 Mont;letter-spacing:-.045em}}
.title .it{{font:italic 400 1.04em/1 Serif;color:{BROWN};letter-spacing:-.02em}}
.card{{position:absolute;background:#fff;padding:22px}}
.card img{{display:block;width:100%}}
.src{{position:absolute;left:80px;font:600 46px/1.1 Hand;color:{BROWN}}}
.big{{position:absolute;left:80px;width:920px;font:800 120px/0.98 Mont;letter-spacing:-.05em}}
.big .it{{font:italic 400 1.04em/1 Serif;color:{BROWN}}}
svg.pen{{position:absolute;left:0;top:0;overflow:visible}}
svg.pen path{{fill:none;stroke:{BROWN};stroke-width:7;stroke-linecap:round;stroke-linejoin:round;filter:url(#rough)}}
.stamp{{position:absolute;font:800 130px/1 Mont;color:#A16E3B;border:12px solid #A16E3B;padding:10px 34px;transform:rotate(-12deg);opacity:.88;white-space:nowrap;mix-blend-mode:multiply}}
"""
DEFS = ('<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/>'
        '<feDisplacementMap in="SourceGraphic" scale="5"/></filter></svg>'
        '<svg class="grain" width="1080" height="1920"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2"/>'
        '<feColorMatrix values="0 0 0 0 .45  0 0 0 0 .38  0 0 0 0 .3  0 0 0 .22 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')

def logo(light=False):
    suf = "_light" if light else ""
    return (f'<div class="logo"><img src="{(SK/f"logo/crest{suf}.svg").as_uri()}" style="height:54px">'
            f'<span class="w"><img src="{(SK/f"logo/letters{suf}.svg").as_uri()}" style="height:22px"><small>AI академія</small></span></div>')

def page(body, dark=False):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{"dark" if dark else ""}">{DEFS}{body}</body></html>'

def case(n, title, head, quote, src, stamp=None):
    st = f'<div class="stamp" style="left:470px;top:1440px">{stamp}</div>' if stamp else ""
    return page(f'''{logo()}<div class="num">{n}</div><div class="title">{title}</div>
      <div class="card" style="left:70px;top:960px;width:940px;transform:rotate(-1.5deg)"><img src="{S(head)}"></div>
      <div class="card" style="left:110px;top:1210px;width:880px;transform:rotate(1deg)"><img src="{S(quote)}"></div>
      <div class="src" style="top:1500px;transform:rotate(-2deg)">{src}</div>{st}''')

FRAMES = {
 "00_hook": page(f'''{logo()}
   <div class="card" style="left:60px;top:420px;width:960px;transform:rotate(-2deg)"><img src="{S('05_replit_headline')}"></div>
   <div class="big" style="top:800px">AI видалив базу компанії.<br><span class="it">А потім вибачився</span></div>
   <div class="src" style="top:1420px;transform:rotate(-2deg)">Fortune · липень 2025</div>'''),
 "00_list": page(f'''{logo()}<div class="big" style="top:620px;font-size:150px"><span class="it" style="font-size:420px;line-height:.8">5</span><br>задач, які я б <span class="it">поки</span> не довіряв AI</div>'''),
 "01_legal": case("01", "Юридичні <span class='it'>документи</span>", "01_avianca_headline", "01_avianca_quote", "Bloomberg Law · червень 2023", "$5 000"),
 "02_clients": case("02", "Відповіді клієнтам <span class='it'>без контролю</span>", "02_aircanada_headline", "02_aircanada_quote", "CBS News · лютий 2024"),
 "03_reports": case("03", "Звіти з цифрами <span class='it'>і джерелами</span>", "03_deloitte_headline", "03_deloitte_quote", "CTV News / AP · жовтень 2025"),
 "04_publish": case("04", "Публікація <span class='it'>без вичитки</span>", "04_suntimes_headline", "04_suntimes_quote", "CBS Chicago · травень 2025", "10 з 15"),
 "05_access": case("05", "Доступ до <span class='it'>робочих систем</span>", "05_replit_headline", "05_replit_quote", "Fortune · липень 2025"),
 "06_cta": page(f'''{logo(True)}<div class="big" style="top:640px;color:#EFE7DF">Останнє слово <span class="it">за людиною</span></div>
   <div class="src" style="top:1180px;font-size:60px">напишіть ПЕРЕВІРКА ↓</div>''', dark=True),
}
out = HERE / "html"; out.mkdir(exist_ok=True)
for k, v in FRAMES.items():
    (out / f"{k}.html").write_text(v, encoding="utf-8")
print(json.dumps(list(FRAMES)))
