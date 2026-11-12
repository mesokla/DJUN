# Builds the panorama HTML (6 slides x 1080 = 6480 x 1350) for the "AI text" carousel, v2.
import pathlib, random
HERE = pathlib.Path(__file__).parent
SP = pathlib.Path("/tmp/claude-0/-home-user-DJUN/777dd743-7ffe-5505-9410-2959c9da1eb7/scratchpad/fonts")
SK = pathlib.Path("/root/.claude/skills/synced/1eb15ba8-9e80-49cb-a1e0-90964f7bdb55_9f9c214f-933c-41c1-8626-dc01b4556c28/djun-design/assets")
W, H, N = 1080, 1350, 6
INK, BROWN, BEIGE, PAPER, MUTED = "#190F09", "#A16E3B", "#EFE7DF", "#F4EEE7", "#8C7B6B"

def ff(name, path, weight="400", style="normal"):
    return f'@font-face{{font-family:"{name}";src:url("{path.as_uri()}");font-weight:{weight};font-style:{style}}}'

fonts = "".join([
    ff("Mont", SK / "fonts/Montserrat.ttf", "100 900"),
    ff("Hand", SP / "fontsource-caveat/files/caveat-cyrillic-600-normal.woff2", "600"),
    ff("Hand", SP / "fontsource-caveat/files/caveat-latin-600-normal.woff2", "600"),
    ff("Serif", SP / "fontsource-playfair-display/files/playfair-display-cyrillic-400-italic.woff2", "400", "italic"),
    ff("Serif", SP / "fontsource-playfair-display/files/playfair-display-latin-400-italic.woff2", "400", "italic"),
])

def logo(x, light=False):
    suf = "_light" if light else ""
    return (f'<div class="logo" style="left:{x+80}px"><img src="{(SK/f"logo/crest{suf}.svg").as_uri()}" style="height:60px">'
            f'<span class="w"><img src="{(SK/f"logo/letters{suf}.svg").as_uri()}" style="height:24px"><small>AI академія</small></span></div>')

def scribble(x, y, w, seed, amp=14, n=None):
    """Hand-drawn zig-zag strike over a phrase."""
    r = random.Random(seed); n = n or max(6, int(w / 38))
    pts = [f"M{x:.0f},{y + r.uniform(-4, 4):.0f}"]
    for i in range(1, n + 1):
        px = x + w * i / n + r.uniform(-6, 6)
        py = y + (amp if i % 2 else -amp) + r.uniform(-5, 5)
        pts.append(f"L{px:.0f},{py:.0f}")
    return " ".join(pts)

# ---------- the pencil line running through the whole carousel ----------
# Waypoints chosen to pass through empty areas; loops sit on the slide joins.
line = ("M 860,1000 "                                   # leaves the circle around «AI» on slide 1
        "C 900,1100 880,1240 1000,1230 "
        "C 1140,1205 1180,1110 1110,1080 C 1040,1050 1000,1150 1080,1190 "   # curl on join 1|2
        "C 1300,1300 1600,1290 1850,1270 "
        "C 2050,1255 2170,1240 2230,1170 C 2280,1110 2190,1080 2150,1140 C 2110,1200 2220,1260 2330,1255 "  # curl on 2|3
        "C 2700,1240 2950,1300 3150,1250 "
        "C 3260,1222 3300,1150 3240,1120 C 3170,1090 3130,1190 3220,1230 C 3420,1310 3800,1300 4100,1270 "   # curl on 3|4
        "C 4250,1255 4330,1200 4300,1150 C 4270,1100 4190,1140 4230,1200 C 4280,1270 4500,1300 4800,1280 "  # curl on 4|5
        "C 5100,1260 5300,1250 5380,1180 C 5430,1130 5350,1095 5320,1150 C 5290,1205 5420,1250 5560,1180 "  # curl on 5|6
        "C 5600,1110 5400,1000 5415,870 C 5425,790 5900,800 6280,792 C 6310,791 6330,780 6320,768 ")              # rises into the final slide and ends under the headline

def slide1(x):
    filler = ("У сучасному світі штучний інтелект відіграє ключову роль. Давайте розберемося, чому це не просто інструмент, а справжній партнер. "
              "Варто зазначити, що це відкриває безмежні можливості для бізнесу. Отже, підсумуємо: майбутнє вже тут. ") * 2
    return f'''
    <div class="filler" style="left:{x+80}px;top:210px;width:920px;height:270px;overflow:hidden;-webkit-mask-image:linear-gradient(#000 40%,transparent)">{filler}</div>
    <div class="h1" style="left:{x+80}px;top:560px;width:940px">Як зробити, щоб ніхто не&nbsp;здогадався,<br><span class="it">що текст писав</span> <span class="ai">AI</span></div>
    <svg class="pen" style="left:0;top:0" width="{W}" height="{H}"><path id="aicircle" d=""/></svg>
    <div class="hand" style="left:{x+80}px;top:1120px;transform:rotate(-3deg)">гортайте, тут 4 кроки →</div>
    '''

def slide2(x):
    phrases = [("«Давайте розберемося»", 560), ("«Це не просто X, а Y»", 690), ("«Відіграє ключову роль»", 820)]
    out = [f'<div class="kick" style="left:{x+80}px;top:220px">крок 1</div>',
           f'<div class="h2" style="left:{x+80}px;top:280px;width:920px">Викресліть фрази, <span class="it">які видають AI</span></div>']
    paths = []
    for i, (t, y) in enumerate(phrases):
        out.append(f'<div class="phrase" style="left:{x+80}px;top:{y}px">{t}</div>')
        wpx = {0: 640, 1: 600, 2: 700}[i]
        paths.append(f'<path class="strike s{i}" d="{scribble(90, y + 50, wpx, i + 3)}"/>')
    out.append(f'<svg class="pen" style="left:{x}px;top:0" width="{W}" height="{H}">{"".join(paths)}'
               f'<path d="M 800,1000 C 860,990 900,940 905,905" /><path d="M 885,925 L 905,900 L 925,928"/></svg>')
    out.append(f'<div class="hand" style="left:{x+560}px;top:1000px;width:440px;transform:rotate(-3deg)">скіл Humanizer для Claude прибирає їх сам</div>')
    return "".join(out)

def slide3(x):
    return f'''
    <div class="kick" style="left:{x+80}px;top:220px">крок 2</div>
    <div class="h2" style="left:{x+80}px;top:280px;width:920px">Покажіть AI, <span class="it">як пишете саме ви</span></div>
    <div class="card" style="left:{x+120}px;top:600px;width:800px;transform:rotate(-2deg)">
      «Ось 3 мої пости. Розбери мій стиль: довжину речень, тон, слова, як я починаю й закінчую текст. Далі пиши так само.»
    </div>
    <div class="hand" style="left:{x+120}px;top:1010px;width:820px;transform:rotate(-2deg)">збережіть у налаштуваннях: ChatGPT → Персоналізація, Claude → Стилі</div>
    '''

def slide4(x):
    items = ["що ви продаєте і кому", "ціни та умови", "3–5 текстів, які вам подобаються", "слова, яких не можна вживати"]
    rows = "".join(f'<div class="row"><span class="box"></span>{t}</div>' for t in items)
    ticks = "".join(f'<path d="M {92},{652 + i*96} l 14,16 l 30,-40"/>' for i in range(4))
    return f'''
    <div class="kick" style="left:{x+80}px;top:220px">крок 3</div>
    <div class="h2" style="left:{x+80}px;top:280px;width:940px">Без контексту AI пише <span class="it">для всіх і ні&nbsp;для&nbsp;кого</span></div>
    <div class="body" style="left:{x+80}px;top:540px;width:900px">Створіть «Проєкт» у ChatGPT або Claude і додайте:</div>
    <div class="list" style="left:{x+80}px;top:620px">{rows}</div>
    <svg class="pen" style="left:{x}px;top:0" width="{W}" height="{H}">{ticks}</svg>
    '''

def slide5(x):
    return f'''
    <div class="kick" style="left:{x+80}px;top:220px">крок 4</div>
    <div class="h2" style="left:{x+80}px;top:280px;width:920px">Зробіть з AI <span class="it">суворого редактора</span></div>
    <div class="quote" style="left:{x+80}px;top:590px;width:900px">«Перечитай текст як суворий редактор. Знайди фрази, які звучать як AI: <span class="mark">канцелярит, пафос, повтори</span>, зайві вступи. Перепиши простіше. Нових фактів не додавай.»</div>
    <div class="hand" style="left:{x+520}px;top:1010px;width:480px;transform:rotate(-3deg)">і попросіть окремо список змін</div>
    '''

def slide6(x):
    return f'''
    <div class="h1 light" style="left:{x+80}px;top:560px;width:940px">AI пише так, <span class="it br">як ви його налаштуєте</span></div>
    <div class="body light" style="left:{x+80}px;top:900px;width:700px">Спробуйте хоча б один крок сьогодні.</div>
    <div class="hand" style="left:{x+560}px;top:1080px;transform:rotate(-4deg)">збережіть, щоб не загубити</div>
    '''

css = f"""
{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W*N}px;height:{H}px;position:relative;overflow:hidden;background:{PAPER};font-family:Mont,sans-serif;color:{INK}}}
.ink{{position:absolute;top:0;left:{W*5}px;width:{W}px;height:{H}px;background:{INK}}}
.grain{{position:absolute;inset:0;pointer-events:none;mix-blend-mode:multiply;opacity:.55}}
.logo{{position:absolute;top:84px;display:flex;align-items:center;gap:16px}}
.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}
.logo small{{font:700 12px/1 Mont;letter-spacing:.2em;color:{BROWN};margin-top:7px;margin-right:-.2em}}
.filler{{position:absolute;font:500 30px/1.5 Mont;color:#CBBDAE;letter-spacing:-.01em}}
.h1{{position:absolute;font:800 104px/1.0 Mont;letter-spacing:-.045em}}
.h2{{position:absolute;font:800 78px/1.02 Mont;letter-spacing:-.04em}}
.it{{font:italic 400 1.04em/1 Serif;letter-spacing:-.02em;color:{BROWN}}}
.h1 .ai{{font:italic 400 1.04em/1 Serif;color:{BROWN}}}
.kick{{position:absolute;font:600 44px/1 Hand;color:{BROWN};transform:rotate(-3deg)}}
.phrase{{position:absolute;font:italic 400 66px/1.2 Serif;color:{INK}}}
.hand{{position:absolute;font:600 46px/1.08 Hand;color:{BROWN}}}
.hand.light{{color:{BROWN}}}
.card{{position:absolute;background:#FFFFFF;padding:56px 60px;font:italic 400 44px/1.35 Serif;color:{INK}}}
.body{{position:absolute;font:500 36px/1.4 Mont;color:{INK}}}
.list{{position:absolute;font:600 44px/1 Mont;letter-spacing:-.02em}}
.row{{height:96px;display:flex;align-items:center;gap:30px}}
.box{{width:40px;height:40px;border:3px solid {INK};flex:none}}
.quote{{position:absolute;font:italic 400 50px/1.32 Serif}}
.mark{{background:linear-gradient(transparent 58%, rgba(161,110,59,.38) 58%, rgba(161,110,59,.38) 92%, transparent 92%)}}
body .light{{color:{BEIGE}}}
svg.pen,svg.line{{position:absolute;overflow:visible}}
svg.pen path,svg.line path{{fill:none;stroke:{BROWN};stroke-width:6;stroke-linecap:round;stroke-linejoin:round;filter:url(#rough)}}
svg.pen path.strike{{stroke-width:7}}
"""

grain = f'''<svg class="grain" width="{W*N}" height="{H}"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/>
<feColorMatrix values="0 0 0 0 .45  0 0 0 0 .38  0 0 0 0 .3  0 0 0 .22 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'''
defs = '<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter></svg>'

body = (defs + '<div class="ink"></div>' + grain
        + "".join(logo(i * W, light=(i == 5)) for i in range(N))
        + slide1(0) + slide2(W) + slide3(2 * W) + slide4(3 * W) + slide5(4 * W) + slide6(5 * W)
        + f'<svg class="line" style="left:0;top:0" width="{W*N}" height="{H}"><path id="mainline" d="{line}"/></svg>')
script = """<script>
document.fonts.ready.then(()=>{const r=document.querySelector('.ai').getBoundingClientRect();
const cx=r.left+r.width*.56, cy=r.top+r.height*.55, rx=r.width*.72, ry=r.height*.6;
document.getElementById('aicircle').setAttribute('d',
`M ${cx-rx*.2},${cy-ry} C ${cx-rx*1.15},${cy-ry*.9} ${cx-rx*1.1},${cy+ry*1.05} ${cx},${cy+ry} C ${cx+rx*1.1},${cy+ry*.95} ${cx+rx*1.08},${cy-ry*1.05} ${cx-rx*.05},${cy-ry*1.08} C ${cx-rx*.5},${cy-ry*1.1} ${cx-rx*.7},${cy-ry*.8} ${cx-rx*.55},${cy-ry*.6}`);
document.body.dataset.ready=1;});
</script>"""
body += script
(HERE / "panorama.html").write_text(f'<!doctype html><html lang="uk"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>', encoding="utf-8")
print("ok")
