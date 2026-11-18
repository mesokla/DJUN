"""Modern minimal house bed for the reel (120 BPM, F minor), synthesized: no licensing issues.
Intro: filtered pads + pluck; the beat drops on the «трильйон» line; riser into an impact on the logo.
usage: python3 make_music.py  -> music.wav, soundtrack.wav (voice + music, ducked, -14 LUFS)"""
import numpy as np, wave, subprocess, json, re, os
from scipy import signal

SR = 44100
here = os.path.dirname(os.path.abspath(__file__))
tm = json.loads(re.search(r'window.TIMING = (.*);', open(os.path.join(here, 'timing.js')).read()).group(1))
TOTAL, LOGO, DROP = tm['total'], tm['starts'][-1], tm['starts'][1]
BPM = 120; BEAT = 60 / BPM; BAR = 4 * BEAT
N = int((TOTAL + 0.5) * SR)
rng = np.random.default_rng(11)

def bus(): return np.zeros((N, 2))
def T(sec): return np.arange(int(sec * SR)) / SR
def hz(m): return 440 * 2 ** ((m - 69) / 12)
def put(b, sig, t, pan=0.0, g=1.0):
    i = int(t * SR)
    if i >= N or i + len(sig) <= 0: return
    s = sig[max(0, -i):]; i = max(0, i); j = min(N, i + len(s)); s = s[:j - i] * g
    b[i:j, 0] += s * np.sqrt((1 - pan) / 2) * 1.414; b[i:j, 1] += s * np.sqrt((1 + pan) / 2) * 1.414
def lp(x, f, order=2): return signal.sosfilt(signal.butter(order, f, 'low', fs=SR, output='sos'), x, axis=0)
def hp(x, f, order=2): return signal.sosfilt(signal.butter(order, f, 'high', fs=SR, output='sos'), x, axis=0)
def bp(x, lo, hi): return signal.sosfilt(signal.butter(2, [lo, hi], 'band', fs=SR, output='sos'), x, axis=0)
def saw(f, t, ph=0.0): return signal.sawtooth(2 * np.pi * f * t + ph)

# grid: a downbeat lands exactly on DROP
def grid(step):
    k = -int(DROP / step) - 1; out = []
    while DROP + k * step < TOTAL:
        out.append((k, DROP + k * step)); k += 1
    return out

# F minor: Fm9 – Dbmaj7 – Abmaj7 – Eb6/9
PROG = [(41, [56, 60, 63, 67]), (37, [56, 60, 61, 65]), (44, [55, 60, 63, 68]), (39, [55, 58, 63, 65])]
def chord_at(t):
    bar_i = int(np.floor((t - DROP) / BAR + 1e-6)); return PROG[bar_i % 4]

# ---------- pads (wide detuned saws) ----------
pad = bus()
for k, t0 in grid(BAR):
    if t0 >= LOGO - 0.01 or t0 + BAR <= 0: continue
    root, notes = chord_at(t0 + 0.01)
    dur = min(BAR, LOGO - t0) + 0.6
    t = T(dur)
    env = np.minimum(1, t / 0.06) * np.clip((dur - t) / 0.6, 0, 1)
    for m in notes:
        for side, dets in ((-0.7, (-14, -5, 9)), (0.7, (-9, 4, 15))):
            s = sum(saw(hz(m) * 2 ** (c / 1200), t, rng.uniform(0, 6.28)) for c in dets) / 3
            put(pad, s * env * 0.05, t0, pan=side)
pad_dark = lp(pad, 650, 2); pad_open = lp(pad, 2400, 2)
tt = np.arange(N) / SR
x = np.clip((tt - (DROP - 1.6)) / 1.6, 0, 1)[:, None]          # filter opens into the drop
pad = pad_dark * (1 - x) + pad_open * x

# ---------- kick + sidechain envelope ----------
drums = bus(); kicks = []
kick_end = LOGO - BAR / 2                                        # last half bar before the logo: build, no kick
for k, t0 in grid(BEAT):
    if DROP - 0.01 <= t0 < kick_end: kicks.append(t0)
t = T(0.45)
ph = 2 * np.pi * np.cumsum(46 + 120 * np.exp(-t * 32)) / SR
kick = np.tanh(1.8 * np.sin(ph) * np.exp(-t * 7.5)) * 0.9
click = hp(rng.standard_normal(len(t)) * np.exp(-t * 900), 2500) * 0.25
kick = kick + click
for t0 in kicks: put(drums, kick, t0, g=0.85)
duck = np.ones(N)
for t0 in kicks:
    i = int(t0 * SR); seg = np.arange(min(N - i, int(0.45 * SR))) / SR
    duck[i:i + len(seg)] = np.minimum(duck[i:i + len(seg)], 1 - 0.75 * np.exp(-seg / 0.11))
pad *= duck[:, None]

# ---------- clap, hats ----------
t = T(0.35); nz = rng.standard_normal(len(t))
cl = np.zeros(len(t))
for d in (0, 0.009, 0.018):
    i = int(d * SR); e = np.exp(-np.arange(len(t) - i) / SR * 90); cl[i:] += nz[:len(t) - i] * e
cl += nz * np.exp(-t * 14) * 0.35
clap = bp(cl, 900, 4200) * 0.55
t = T(0.05); chh = hp(rng.standard_normal(len(t)), 7000) * np.exp(-t * 110) * 0.22
t = T(0.22); ohh = hp(rng.standard_normal(len(t)), 6500) * np.exp(-t * 16) * 0.16
claps = []
for k, t0 in grid(BEAT):
    if not (DROP - 0.01 <= t0 < kick_end): continue
    if k % 2 == 1: put(drums, clap, t0, pan=0.05); claps.append(t0)
    put(drums, ohh, t0 + BEAT / 2, pan=0.25)
for k, t0 in grid(BEAT / 4):
    if not (DROP - 0.01 <= t0 < kick_end): continue
    if k % 4 in (1, 3): put(drums, chh, t0, pan=-0.3, g=0.6 + 0.4 * (k % 8 == 3))

# ---------- bass: sub + filtered saw on the offbeats (house) ----------
bass = bus()
for k, t0 in grid(BEAT):
    on = t0 + BEAT / 2
    if not (DROP - 0.01 <= t0 < kick_end): continue
    root, _ = chord_at(t0 + 0.01)
    t = T(0.36); env = np.minimum(1, t / 0.004) * np.exp(-t * 5) * np.clip((0.36 - t) / 0.03, 0, 1)
    s = np.sin(2 * np.pi * hz(root) * t) * 0.9 + lp(saw(hz(root + 12), t), 520) * 0.35
    put(bass, np.tanh(1.4 * s) * env * 0.55, on)

# ---------- pluck arp with ping-pong delay ----------
arp = bus()
for k, t0 in grid(BEAT / 4):
    if t0 >= LOGO - 0.02 or t0 < 0: continue
    _, notes = chord_at(t0 + 0.01)
    seq = [notes[0] + 12, notes[2] + 12, notes[1] + 12, notes[3] + 12]
    if k % 8 in (2, 5, 7): continue                                     # syncopated gaps
    m = seq[k % 4]; t = T(0.3)
    s = lp(saw(hz(m), t) * np.exp(-t * 16), 3200) * 0.6 + np.sin(2 * np.pi * hz(m) * t) * np.exp(-t * 10) * 0.5
    g = 0.10 if t0 < DROP else 0.16
    put(arp, s, t0, pan=0.2 if k % 2 else -0.2, g=g)
d = int(BEAT * 0.75 * SR); dl = np.zeros_like(arp)
for rep, a in enumerate((0.45, 0.28, 0.16)):
    sh = d * (rep + 1); dl[sh:, (rep + 1) % 2] += arp[:-sh].sum(1) * a / 2
arp = arp + lp(dl, 3500)

# ---------- riser + impact on the logo ----------
fx = bus()
rl = 2.0; t = T(rl); nz = rng.standard_normal(len(t)); out = np.zeros(len(t)); blk = 2048
for i in range(0, len(t), blk):
    c = 500 * (14 ** (i / len(t)))
    out[i:i + blk] = bp(nz[max(0, i - 4096):i + blk], c * 0.7, min(c * 1.5, 18000))[-len(nz[i:i + blk]):]
riser = out * (t / rl) ** 2 * 0.35
riser += np.sin(2 * np.pi * np.cumsum(220 * 2 ** (2 * t / rl)) / SR) * (t / rl) ** 3 * 0.05
put(fx, riser, LOGO - rl)
t = T(2.6); ph = 2 * np.pi * np.cumsum(38 + 70 * np.exp(-t * 9)) / SR
put(fx, np.tanh(2 * np.sin(ph) * np.exp(-t * 2.2)) * 0.8, LOGO)                 # sub boom
t = T(2.6)
for i, m in enumerate([41, 53, 56, 60, 63, 67, 72]):                             # Fm9 stab, open
    s = sum(saw(hz(m) * 2 ** (c / 1200), t) for c in (-10, 0, 10)) / 3
    put(fx, lp(s, 3000) * np.exp(-t * 1.6) * np.minimum(1, t / 0.01) * 0.07, LOGO, pan=-0.6 + 0.2 * i)
for i, m in enumerate([72, 75, 79, 84, 87]):                                     # sparkle
    tt2 = T(1.2); s = np.sin(2 * np.pi * hz(m) * tt2) * np.exp(-tt2 * 4) * 0.12
    put(fx, s, LOGO + 0.08 + i * BEAT / 4, pan=0.35 * (-1) ** i)

# ---------- reverb ----------
def reverb(x, sec=2.2, damp=6000):
    t = T(sec); ir = np.stack([rng.standard_normal(len(t)), rng.standard_normal(len(t))], 1) * np.exp(-t * 3.2)[:, None]
    ir = lp(ir, damp); ir /= np.abs(ir).sum(0).max() / 6
    return np.stack([signal.fftconvolve(x[:, c], ir[:, c])[:N] for c in range(2)], 1)
send = pad * 0.35 + arp * 0.5 + fx * 0.35 + bp(drums, 800, 5000) * 0.12
wet = reverb(send)
mix = pad * 0.8 + drums * 1.0 + bass * 0.9 + arp * 0.8 + fx * 1.0 + wet * 0.5
mix = hp(mix, 30)

# glue: gentle bus saturation, then level automation (quiet under the voice, full on the logo)
mix = np.tanh(mix * 1.3) / 1.3
g = np.full(N, 0.42)
g = np.where(tt < DROP, 0.42 * 2.6, g)                          # filtered intro is quiet by nature
g = np.where(tt < 0.3, g * tt / 0.3, g)
sw = tt >= LOGO - 1.2
g[sw] = 0.42 + 1.9 * np.clip((tt[sw] - (LOGO - 1.2)) / 1.2, 0, 1) ** 1.5      # logo: music takes over
fo = tt > TOTAL - 1.0
g[fo] *= np.clip((TOTAL - tt[fo]) / 1.0, 0, 1)
mix *= g[:, None]
mix = mix[:int(TOTAL * SR)]
mix = mix / np.abs(mix).max() * 0.89
wv = wave.open(os.path.join(here, 'music.wav'), 'wb'); wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
wv.writeframes((mix * 32767).astype(np.int16).tobytes()); wv.close()

pre = ('[0:a]aresample=44100,aformat=channel_layouts=stereo,apad,asplit=2[v][sc];'
       '[1:a]volume=0.13[m];[m][sc]sidechaincompress=threshold=0.03:ratio=3:attack=25:release=300[md];'
       '[v][md]amix=inputs=2:duration=shortest:normalize=0')
ins = ['-i', os.path.join(here, 'voice.mp3'), '-i', os.path.join(here, 'music.wav')]
# two-pass linear loudnorm: hits -14 LUFS without pumping the quiet music up in the pauses
r = subprocess.run(['ffmpeg', '-hide_banner', '-y'] + ins + ['-filter_complex', pre + ',loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json[out]',
                    '-map', '[out]', '-t', f'{TOTAL:.3f}', '-f', 'null', '-'], capture_output=True, text=True).stderr
mj = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:measured_I={mj['input_i']}:measured_TP={mj['input_tp']}"
      f":measured_LRA={mj['input_lra']}:measured_thresh={mj['input_thresh']}:offset={mj['target_offset']}")
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', pre + ',' + ln + ',aresample=44100[out]',
               '-map', '[out]', '-t', f'{TOTAL:.3f}', os.path.join(here, 'soundtrack.wav')], check=True)
print('music.wav + soundtrack.wav', TOTAL, 'drop at', DROP, 'logo at', LOGO)
