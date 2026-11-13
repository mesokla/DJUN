# Reel frames v2: 4 tasks, with drawn illustrations / infographics. 1080x1920, content kept above y=1590 (Instagram UI).
import pathlib
HERE = pathlib.Path(__file__).parent
SP = pathlib.Path("/tmp/claude-0/-home-user-DJUN/777dd743-7ffe-5505-9410-2959c9da1eb7/scratchpad/fonts")
SK = pathlib.Path("/root/.claude/skills/synced/1eb15ba8-9e80-49cb-a1e0-90964f7bdb55_9f9c214f-933c-41c1-8626-dc01b4556c28/djun-design/assets")
INK, BROWN, PAPER, BEIGE, MUTED = "#190F09", "#A16E3B", "#F4EEE7", "#EFE7DF", "#8C7B6B"
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
body.dark{{background:{INK};color:{BEIGE}}}
.grain{{position:absolute;inset:0;mix-blend-mode:multiply;opacity:.55;pointer-events:none}}
.abs{{position:absolute}}
.logo{{position:absolute;left:80px;top:240px;display:flex;align-items:center;gap:14px}}
.logo .w{{display:flex;flex-direction:column;align-items:flex-end}}
.logo small{{font:700 11px/1 Mont;letter-spacing:.2em;color:{BROWN};margin-top:6px;margin-right:-.2em}}
.num{{position:absolute;right:80px;top:200px;font:italic 400 220px/1 Serif;color:{BROWN}}}
.title{{position:absolute;left:80px;top:400px;width:920px;font:800 84px/0.98 Mont;letter-spacing:-.045em}}
.it{{font:italic 400 1.04em/1 Serif;color:{BROWN};letter-spacing:-.02em}}
.card{{position:absolute;background:#fff;padding:20px}}
.card img{{display:block;width:100%}}
.src{{position:absolute;left:80px;font:600 36px/1 Hand;color:{MUTED}}}
.tip{{position:absolute;left:80px;width:860px;font:600 56px/1.02 Hand;color:{INK};transform:rotate(-2deg)}}
.big{{position:absolute;left:80px;width:920px;font:800 112px/0.98 Mont;letter-spacing:-.05em}}
.lab{{font:700 30px/1.15 Mont;letter-spacing:-.01em}}
.hand{{font:600 44px/1 Hand;color:{BROWN}}}
svg.d{{position:absolute;overflow:visible}}
@keyframes pop{{from{{opacity:0;translate:0 46px}}to{{opacity:1;translate:0 0}}}}
@keyframes zin{{from{{opacity:0;scale:1.18}}to{{opacity:1;scale:1}}}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
@keyframes swbg{{to{{background:#CFC3B6}}}}
@keyframes knob{{to{{translate:-64px 0}}}}
.a{{animation:pop .55s cubic-bezier(.2,.8,.2,1) both}}
.z{{animation:zin .9s cubic-bezier(.2,.8,.2,1) both}}
.dr{{stroke-dasharray:1;stroke-dashoffset:1;animation:draw .9s ease-in-out both}}
.sw.toff{{background:{BROWN};animation:swbg .35s ease both}}
.sw.toff i{{right:8px;animation:knob .35s ease both}}
svg.d .p{{fill:none;stroke:{INK};stroke-width:6;stroke-linecap:round;stroke-linejoin:round;filter:url(#rough)}}
svg.d .b{{fill:none;stroke:{BROWN};stroke-width:7;stroke-linecap:round;stroke-linejoin:round;filter:url(#rough)}}
.bub{{position:absolute;padding:26px 32px;font:500 38px/1.25 Mont;border-radius:28px}}
.bub.me{{background:#fff;border:3px solid {INK};border-bottom-left-radius:4px}}
.bub.bot{{background:{INK};color:{BEIGE};border-bottom-right-radius:4px}}
.bub small{{display:block;font:700 22px/1 Mont;letter-spacing:.12em;text-transform:uppercase;opacity:.6;margin-bottom:10px}}
.book{{position:absolute;width:118px;height:120px;display:flex;align-items:center;justify-content:center;font:italic 400 70px/1 Serif}}
.book.real{{background:{INK};color:{BEIGE}}}
.book.fake{{border:4px dashed {BROWN};color:{BROWN}}}
.tog{{position:absolute;display:flex;align-items:center;gap:30px;font:700 46px/1 Mont}}
.sw{{width:130px;height:66px;border-radius:40px;position:relative;flex:none}}
.sw i{{position:absolute;top:8px;width:50px;height:50px;border-radius:50%;background:#fff}}
.sw.on{{background:{BROWN}}} .sw.on i{{right:8px}}
.sw.off{{background:#CFC3B6}} .sw.off i{{left:8px}}
"""
DEFS = ('<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/>'
        '<feDisplacementMap in="SourceGraphic" scale="5"/></filter></svg>'
        '<svg class="grain" width="1080" height="1920"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2"/>'
        '<feColorMatrix values="0 0 0 0 .45  0 0 0 0 .38  0 0 0 0 .3  0 0 0 .22 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
def logo(light=False):
    suf = "_light" if light else ""
    return (f'<div class="logo"><img src="{(SK/f"logo/crest{suf}.svg").as_uri()}" style="height:54px">'
            f'<span class="w"><img src="{(SK/f"logo/letters{suf}.svg").as_uri()}" style="height:22px"><small>AI академія</small></span></div>')
SCRIPT = """<script>
window.setT = t => {
  document.getAnimations().forEach(a => { a.pause(); a.currentTime = t * 1000; });
  document.querySelectorAll('[data-count]').forEach(el => {
    const [n, s, d] = el.dataset.count.split(',').map(Number);
    const k = Math.min(1, Math.max(0, (t - s) / d)); el.textContent = (el.dataset.pre || '') + Math.round(n * (1 - Math.pow(1 - k, 3))).toLocaleString('uk-UA') + (el.dataset.suf || '');
  });
};
</script>"""
D = lambda t: f"animation-delay:{t}s;"
def page(body, dark=False):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{"dark" if dark else ""}">{DEFS}{body}{SCRIPT}</body></html>'

def case(n, title, art, head, src, tip, t0=3.6, tt=None):
    return page(f'''{logo()}<div class="num a">{n}</div><div class="title a" style="{D(.15)}">{title}</div>{art}
      <div class="abs a" style="left:80px;top:1240px;width:880px;{D(t0)}">
        <div class="card" style="position:relative;transform:rotate(-1.5deg)"><img src="{S(head)}"></div>
        <div class="src" style="position:relative;left:0;margin-top:18px">{src}</div>
        <div class="tip a" style="position:relative;left:0;margin-top:16px;{D(tt if tt is not None else t0+.7)}">{tip}</div></div>''')

# --- illustrations ---
db = '''<svg class="d" style="left:640px;top:930px" width="340" height="380">
  <ellipse class="p dr" pathLength="1" style="{D(.2)}" cx="170" cy="50" rx="140" ry="40"/><path class="p dr" pathLength="1" style="{D(.4)}" d="M30,50 V300 C30,355 310,355 310,300 V50"/>
  <path class="p dr" pathLength="1" style="{D(.6)}" d="M30,135 C30,190 310,190 310,135"/><path class="p dr" pathLength="1" style="{D(.7)}" d="M30,220 C30,275 310,275 310,220"/>
  <path class="b dr" pathLength="1" style="stroke-width:9;animation-duration:.5s;{D(1.7)}" d="M175,20 L150,110 L200,160 L140,240 L190,300 L160,370"/></svg>'''
hook = page(f'''{logo()}
  <div class="card z" style="left:70px;top:350px;width:940px;transform:rotate(-2deg)"><img src="{S('05_replit_headline')}"></div>
  <div class="big" style="top:580px"><span class="a" style="display:inline-block;{D(.2)}">AI стер</span><br><span class="a" style="display:inline-block;{D(.5)}">базу компанії.</span><br><span class="it a" style="display:inline-block;{D(1.4)}">Повністю.</span></div>
  <div class="abs a" style="left:80px;top:1010px;width:520px;{D(.8)}">
    <div class="lab" data-count="1200,0.8,1.0" data-suf="+" style="font-size:64px;font-weight:800;letter-spacing:-.04em">1 200+</div><div class="lab" style="color:{MUTED}">керівників у базі</div>
    <div class="lab" data-count="1190,1.0,1.0" data-suf="+" style="font-size:64px;font-weight:800;letter-spacing:-.04em;margin-top:26px">1 190+</div><div class="lab" style="color:{MUTED}">компаній</div></div>
  {db}
  <div class="hand abs a" style="left:80px;top:1400px;transform:rotate(-3deg);{D(2.2)}">«я знищив місяці роботи за секунди» · AI-агент</div>
  <div class="src a" style="top:1490px;font-size:46px;color:#A16E3B;{D(2.6)}">реальна історія · Fortune, липень 2025</div>''')

icons = f'''<svg class="d" style="left:80px;top:1360px" width="920" height="200">
  <path class="p dr" pathLength="1" style="animation-delay:1.18s" d="M20,30 h150 a20,20 0 0 1 20,20 v70 a20,20 0 0 1 -20,20 h-90 l-40,35 v-35 h-20 a20,20 0 0 1 -20,-20 v-70 a20,20 0 0 1 20,-20z"/>
  <path class="p dr" pathLength="1" style="animation-delay:1.36s" d="M270,20 h120 l40,40 v130 h-160z"/><path class="p dr" pathLength="1" style="animation-delay:1.54s" d="M300,90 h100 M300,125 h100 M300,160 h60"/>
  <path class="p dr" pathLength="1" style="animation-delay:1.72s" d="M520,40 h40 v150 h-40z M580,40 h40 v150 h-40z"/><path class="b dr" pathLength="1" style="animation-delay:1.90s" d="M640,45 h40 v145 h-40z" stroke-dasharray="14 12"/>
  <rect class="p dr" pathLength="1" style="animation-delay:2.08s" x="790" y="95" width="110" height="95" rx="10"/><path class="p dr" pathLength="1" style="animation-delay:2.26s" d="M815,95 v-30 a30,30 0 0 1 60,0 v30"/></svg>'''
lst = page(f'''{logo()}<div class="big" style="top:420px;font-size:150px"><span class="it z" style="display:inline-block;font-size:440px;line-height:.78;{D(.45)}">4</span><br><span class="a" style="display:inline-block;{D(.8)}">задачі, які я б <span class="it">поки</span> не довіряв AI</span></div>{icons}''')

chat = f'''<div class="bub me a" style="left:80px;top:740px;width:640px;{D(1.6)}"><small>клієнт</small>Можна повернути гроші за квиток?</div>
  <div class="bub bot a" style="left:300px;top:930px;width:680px;{D(2.9)}"><small>чат-бот Air Canada</small>Так, подайте заявку протягом 90 днів ✓</div>
  <svg class="d" style="left:90px;top:1000px" width="200" height="200"><path class="b dr" pathLength="1" style="{D(6.4)}" d="M30,150 L120,60 M95,35 L145,85 M75,55 L125,105"/><path class="b dr" pathLength="1" style="{D(6.7)}" d="M20,180 h110"/></svg>
  <div class="hand abs a" style="left:90px;top:1180px;transform:rotate(-3deg);{D(4.7)}">таких правил не було → суд: платить компанія</div>'''

report = f'''<svg class="d" style="left:90px;top:720px" width="420" height="480">
  <path class="p dr" pathLength="1" style="{D(.5)}" d="M20,20 h260 l80,80 v360 h-340z"/><path class="p dr" pathLength="1" style="{D(.9)}" d="M280,20 v80 h80"/>
  <path class="p dr" pathLength="1" style="animation-duration:1.4s;{D(1.0)}" d="M60,150 h240 M60,200 h240 M60,250 h180 M60,300 h240 M60,350 h200 M60,400 h150"/>
  <ellipse class="b dr" pathLength="1" style="{D(7.1)}" cx="160" cy="250" rx="120" ry="34"/><ellipse class="b dr" pathLength="1" style="{D(8.4)}" cx="170" cy="350" rx="135" ry="34"/></svg>
  <div class="abs a" style="left:560px;top:760px;width:440px;{D(3.6)}"><div class="lab" data-count="440000,3.6,1.2" data-pre="A$" style="font-size:72px;font-weight:800;letter-spacing:-.04em">440 000</div><div class="lab" style="color:{MUTED}">вартість звіту</div></div>
  <div class="hand abs a" style="left:560px;top:960px;width:440px;transform:rotate(-3deg);{D(7.3)}">вигадана цитата судді</div>
  <div class="hand abs a" style="left:560px;top:1060px;width:440px;transform:rotate(-3deg);{D(8.6)}">дослідження, яких не існує</div>'''

books = "".join(f'<div class="book a {"real" if i in (1,5,7,11,13) else "fake"}" style="left:{80+ (i%5)*150}px;top:{720+(i//5)*140}px;animation-delay:{1.3+i*.09:.2f}s">{"" if i in (1,5,7,11,13) else "?"}</div>' for i in range(15))
books += f'''<div class="abs a" style="left:850px;top:740px;width:180px;animation-delay:4.7s"><div class="lab" data-count="10,4.7,0.8" style="font-size:96px;font-weight:800;color:{BROWN};letter-spacing:-.05em">10</div><div class="lab">з 15 книжок не існує</div></div>'''

toggles = f'''<div class="tog a" style="left:80px;top:760px;{D(.6)}"><span class="sw on"><i></i></span>Читати дані</div>
  <div class="tog a" style="left:80px;top:880px;{D(.8)}"><span class="sw toff" style="{D(5.5)}"><i style="{D(5.5)}"></i></span>Змінювати</div>
  <div class="tog a" style="left:80px;top:1000px;{D(1.0)}"><span class="sw toff" style="{D(6.0)}"><i style="{D(6.0)}"></i></span>Видаляти</div>
  <svg class="d" style="left:700px;top:760px" width="280" height="330"><rect class="p dr" pathLength="1" style="{D(.6)}" x="40" y="140" width="200" height="170" rx="16"/><path class="p dr" pathLength="1" style="{D(6.3)}" d="M85,140 v-50 a55,55 0 0 1 110,0 v50"/><circle class="b dr" pathLength="1" style="{D(1.0)}" cx="140" cy="215" r="18"/><path class="b dr" pathLength="1" style="{D(1.2)}" d="M140,233 v35"/></svg>
  <div class="hand abs a" style="left:80px;top:1130px;transform:rotate(-3deg);{D(6.4)}">зміни тільки після вашого «так»</div>'''

FRAMES = {
 "00_hook": hook, "00_list": lst,
 "01_clients": case("01", "Відповіді клієнтам <span class='it'>без контролю</span>", chat, "02_aircanada_headline", "CBS News · лютий 2024", "боту чіткі правила, складні питання людині", t0=5.4, tt=7.5),
 "02_reports": case("02", "Звіти <span class='it'>без перевірки джерел</span>", report, "03_deloitte_headline", "CTV News / AP · жовтень 2025", "звіти з AI робимо, але кожну цифру й джерело перевіряємо", t0=4.4, tt=9.2),
 "03_publish": case("03", "Публікація <span class='it'>без вичитки</span>", books, "04_suntimes_headline", "CBS Chicago · травень 2025", "все, що йде назовні, вичитує людина", t0=2.4, tt=5.5),
 "04_access": case("04", "Повний доступ <span class='it'>до робочих систем</span>", toggles, "05_replit_headline", "Fortune · липень 2025", "AI отримує права тільки на читання", t0=2.2, tt=6.8),
 "05_end": page(f'''{logo(True)}
      <div class="big a" style="top:560px;font-size:100px;color:{BEIGE};{D(.3)}">AI ваш найкращий помічник, <span class="it">але важливо вміти ним користуватися</span></div>
   <svg class="d" style="left:80px;top:1080px" width="640" height="120"><path class="b dr" pathLength="1" style="{D(1.6)}" d="M10,60 C150,20 300,95 630,50"/></svg>
   <div class="abs a" style="left:80px;top:1190px;width:900px;font:500 40px/1.35 Mont;color:#C9B8A6;{D(3.1)}">Ми показали, як робити не треба. Решта за вами.</div>
   <div class="hand abs a" style="left:80px;top:1440px;font-size:56px;{D(4.4)}">збережіть і перешліть колезі</div>''', dark=True),
}
out = HERE / "html"; out.mkdir(exist_ok=True)
for f in out.glob("*.html"): f.unlink()
for k, v in FRAMES.items(): (out / f"{k}.html").write_text(v, encoding="utf-8")
print("ok")
