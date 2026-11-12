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
# Waypoints in panorama coordinates (slide i spans x = i*1080 ... (i+1)*1080).
# The line changes height from slide to slide: bottom, rises on 2, middle on 3, bottom on 4, top on 5, underline on 6.
PTS = [(860,1000),(900,1120),(1000,1225),
       (1110,1150),(1065,1110),(1040,1175),(1130,1235),
       (1480,1255),(1850,1205),(2065,960),(2070,700),(2060,540),
       (2135,445),(2095,480),(2150,535),(2250,508),
       (2660,520),(3060,505),(3170,700),(3175,950),(3150,1150),
       (3230,1215),(3265,1150),(3200,1135),(3215,1205),(3310,1245),
       (3740,1255),(4100,1215),(4250,1000),(4255,620),(4255,320),
       (4300,200),(4335,145),(4295,120),(4280,175),(4370,200),
       (4820,185),(5150,205),(5325,480),(5335,900),(5320,1150),
       (5395,1220),(5425,1160),(5365,1140),(5375,1210),(5445,1240),
       (5420,1080),(5418,880),(5460,805),(5900,800),(6280,792),(6320,768)]

def smooth(pts, k=1.0):
    d = f"M {pts[0][0]},{pts[0][1]} "
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]; p1, p2 = pts[i], pts[i + 1]; p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) * k / 6, p1[1] + (p2[1] - p0[1]) * k / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) * k / 6, p2[1] - (p3[1] - p1[1]) * k / 6)
        d += f"C {c1[0]:.0f},{c1[1]:.0f} {c2[0]:.0f},{c2[1]:.0f} {p2[0]},{p2[1]} "
    return d
line = smooth(PTS)

NEWS = ("У сучасному світі штучний інтелект відіграє ключову роль у трансформації бізнесу. Давайте розберемося, чому це не просто інструмент, "
        "а справжній партнер для команди. Варто зазначити, що нові технології відкривають безмежні можливості. Експерти наголошують: "
        "той, хто не адаптується, ризикує відстати. Отже, підсумуємо: майбутнє вже тут, і воно відіграє вирішальну роль. ")

def slide1(x):
    sent = [t.strip() + "." for t in NEWS.split(".") if t.strip()]
    cols = "".join(f'<div class="col">{" ".join((sent[i*2:] + sent[:i*2]) * 4)}</div>' for i in range(4))
    return (f'<div class="mast" style="left:{x+80}px;top:196px;width:920px">'
            f'<div class="mast-row"><span>№ 404</span><span>четвер</span><span>ціна: ваша увага</span></div>'
            f'<div class="mast-title">Щоденний AI-вісник</div></div>'
            f'<div class="news" style="left:{x+80}px;top:360px;width:920px">{cols}</div>'
            f'<div class="cover-h" style="left:{x+56}px;top:590px;width:968px">Як зробити, щоб ніхто не&nbsp;здогадався,<br><span class="it">що текст писав</span> <span class="ai">AI</span></div>'
            f'<svg class="pen" style="left:0;top:0" width="{W}" height="{H}"><path id="aicircle" d=""/></svg>'
            f'<div class="hand" style="left:{x+80}px;top:1150px;transform:rotate(-3deg)">гортайте, тут 4 кроки →</div>')

def slide2(x):
    phrases = [("«Давайте розберемося»", 560), ("«Це не просто X, а Y»", 690), ("«Відіграє ключову роль»", 820)]
    out = [f'<div class="kick" style="left:{x+80}px;top:220px">крок 1</div>',
           f'<div class="h2" style="left:{x+80}px;top:280px;width:880px">Викресліть фрази, <span class="it">які видають AI</span></div>']
    paths = []
    for i, (t, y) in enumerate(phrases):
        out.append(f'<div class="phrase" style="left:{x+80}px;top:{y}px">{t}</div>')
        wpx = {0: 640, 1: 600, 2: 700}[i]
        paths.append(f'<path class="strike s{i}" d="{scribble(90, y + 46, wpx, i + 3)}"/>')
    out.append(f'<svg class="pen" style="left:{x}px;top:0" width="{W}" height="{H}">{"".join(paths)}'
               f'<path d="M 300,1010 C 250,1000 200,970 190,925"/><path d="M 172,945 L 190,920 L 208,948"/></svg>')
    out.append(f'<div class="hand" style="left:{x+320}px;top:990px;width:520px;transform:rotate(-3deg)">скіл Humanizer для Claude прибирає їх сам</div>')
    return "".join(out)

def slide3(x):
    return (f'<div class="kick light" style="left:{x+80}px;top:220px">крок 2</div>'
            f'<div class="h2 light" style="left:{x+80}px;top:280px;width:920px">Покажіть AI, <span class="it tan">як пишете саме ви</span></div>'
            f'<div class="card" style="left:{x+110}px;top:610px;width:780px;transform:rotate(-3deg)"><div class="tape"></div>'
            f'«Ось 3 мої пости. Розбери мій стиль: довжину речень, тон, слова, як я починаю й закінчую текст. Далі пиши так само.»</div>'
            f'<div class="hand tan" style="left:{x+110}px;top:1040px;width:820px;transform:rotate(-2deg)">збережіть у налаштуваннях: ChatGPT → Персоналізація, Claude → Стилі</div>')

def slide4(x):
    items = ["що ви продаєте і кому", "ціни та умови", "3–5 текстів, які вам подобаються", "слова, яких не можна вживати"]
    rows = "".join(f'<div class="row"><span class="box"></span>{t}</div>' for t in items)
    ticks = "".join(f'<path d="M 192,{684 + i*96} l 14,16 l 30,-40"/>' for i in range(4))
    return (f'<div class="kick" style="left:{x+180}px;top:220px">крок 3</div>'
            f'<div class="h2" style="left:{x+180}px;top:280px;width:800px">Без контексту AI пише <span class="it">для всіх і ні&nbsp;для&nbsp;кого</span></div>'
            f'<div class="body" style="left:{x+180}px;top:572px;width:780px">У «Проєкт» ChatGPT чи Claude додайте:</div>'
            f'<div class="list" style="left:{x+180}px;top:652px">{rows}</div>'
            f'<svg class="pen" style="left:{x}px;top:0" width="{W}" height="{H}">{ticks}</svg>')

def slide5(x):
    return (f'<div class="bigq" style="left:{x+560}px;top:330px">«</div>'
            f'<div class="kick" style="left:{x+80}px;top:250px">крок 4</div>'
            f'<div class="h2" style="left:{x+80}px;top:310px;width:880px">Зробіть з AI <span class="it">суворого редактора</span></div>'
            f'<div class="quote" style="left:{x+80}px;top:610px;width:880px">«Перечитай текст як суворий редактор. Знайди фрази, які звучать як AI: <span class="mark">канцелярит, пафос, повтори</span>, зайві вступи. Перепиши простіше. Нових фактів не додавай.»</div>'
            f'<div class="hand" style="left:{x+80}px;top:1110px;width:600px;transform:rotate(-3deg)">і попросіть окремо список змін</div>')

def slide6(x):
    return (f'<div class="h1 light" style="left:{x+80}px;top:560px;width:940px">AI пише так, <span class="it">як ви його налаштуєте</span></div>'
            f'<div class="body light" style="left:{x+120}px;top:900px;width:700px">Спробуйте хоча б один крок сьогодні.</div>'
            f'<div class="hand" style="left:{x+560}px;top:1080px;transform:rotate(-4deg)">збережіть, щоб не загубити</div>')

css = f"""
{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W*N}px;height:{H}px;position:relative;overflow:hidden;background:{PAPER};font-family:Mont,sans-serif;color:{INK}}}
.bg{{position:absolute;top:0;width:{W}px;height:{H}px}}
.news{{position:absolute;height:960px;display:grid;grid-template-columns:repeat(4,1fr);overflow:hidden;-webkit-mask-image:linear-gradient(#000 70%,transparent)}}
.col{{font:italic 400 19px/1.45 Serif;color:#CDBFB0;padding:0 14px;border-left:1.5px solid #D9CCBE;text-align:justify;hyphens:auto}}
.col:first-child{{border-left:none;padding-left:0}}
.mast{{position:absolute;border-top:3px solid #B9A897;border-bottom:1.5px solid #B9A897;padding:12px 0 14px}}
.mast-row{{display:flex;justify-content:space-between;font:600 20px/1 Mont;letter-spacing:.12em;text-transform:uppercase;color:#B9A897}}
.mast-title{{font:italic 400 92px/1 Serif;text-align:center;letter-spacing:-.02em;margin-top:12px;color:#B9A897}}
.cover-h{{position:absolute;font:800 100px/1.0 Mont;letter-spacing:-.045em;background:#FBF8F4;padding:30px 24px 34px;transform:rotate(-1.5deg)}}
.cover-h .ai{{font:italic 400 1.04em/1 Serif;color:{BROWN}}}
.tan{{color:#E3C9A8!important}}
.tape{{position:absolute;top:-22px;left:42%;width:150px;height:44px;background:rgba(255,255,255,.55);transform:rotate(4deg)}}
.bigq{{position:absolute;font:italic 400 900px/1 Serif;color:{BROWN};opacity:.12}}
.notebook{{background-image:repeating-linear-gradient(transparent 0 94px, rgba(161,110,59,.22) 94px 96px);background-position:0 48px}}
.margin{{position:absolute;top:190px;width:3px;height:{H-190}px;background:rgba(161,110,59,.55)}}
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
.card{{position:absolute;background:{BEIGE};padding:56px 60px;font:italic 400 44px/1.35 Serif;color:{INK}}}
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

bgs = (f'<div class="bg" style="left:{2*W}px;background:#714326"></div>'
       f'<div class="bg notebook" style="left:{3*W}px;background:#FBF8F4"></div><div class="margin" style="left:{3*W+140}px"></div>'
       f'<div class="bg" style="left:{4*W}px;background:#FFFFFF"></div>'
       f'<div class="bg" style="left:{5*W}px;background:{INK}"></div>')
body = (defs + bgs + grain
        + "".join(logo(i * W, light=(i in (2, 5))) for i in range(N))
        + slide1(0) + slide2(W) + slide3(2 * W) + slide4(3 * W) + slide5(4 * W) + slide6(5 * W)
        + f'<svg class="line" style="left:0;top:0" width="{W*N}" height="{H}"><defs><clipPath id="cb"><rect x="0" y="0" width="{2*W}" height="{H}"/><rect x="{3*W}" y="0" width="{3*W}" height="{H}"/></clipPath>'
          f'<clipPath id="cs3"><rect x="{2*W}" y="0" width="{W}" height="{H}"/></clipPath></defs>'
          f'<path id="mainline" d="{line}" clip-path="url(#cb)"/><path d="{line}" clip-path="url(#cs3)" style="stroke:#E3C9A8"/></svg>')
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
