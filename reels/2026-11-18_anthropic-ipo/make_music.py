"""Cinematic corporate bed for the reel, built from real instrument samples (see assets/samples/CREDITS.md).
C minor, 84 BPM. Intro: soft piano ostinato. From the «трильйон» line: contrabass, violins, low pulse.
Before the logo: reversed piano swell; on the logo: full piano + strings chord.
usage: python3 make_music.py  -> music.wav, soundtrack.wav (voice + music, ducked, -14 LUFS)"""
import numpy as np, wave, subprocess, json, re, os, functools
from scipy import signal

SR = 44100
here = os.path.dirname(os.path.abspath(__file__))
SMP = os.path.join(here, 'assets', 'samples')
tm = json.loads(re.search(r'window.TIMING = (.*);', open(os.path.join(here, 'timing.js')).read()).group(1))
TOTAL, LOGO, DROP = tm['total'], tm['starts'][-1], tm['starts'][1]
BPM = 84; BEAT = 60 / BPM; BAR = 4 * BEAT; E8 = BEAT / 2
N = int((TOTAL + 1) * SR)
rng = np.random.default_rng(5)
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

@functools.lru_cache(None)
def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)

def bank(folder, fmt):
    out = {}
    for f in os.listdir(os.path.join(SMP, folder)):
        m = re.match(fmt, f)
        if m:
            name, octv = m.group(1).replace('s', '#'), int(m.group(2))
            out[NAMES.index(name) + 12 * (octv + 1)] = os.path.join(SMP, folder, f)
    return out
PIANO6 = bank('piano6', r'^([A-G]#?)(\d)v6\.mp3$')
PIANO10 = bank('piano10', r'^([A-G]#?)(\d)v10\.mp3$')
VIOLIN = bank('violin', r'^([A-G]s?)(\d)\.mp3$')
BASS = bank('contrabass', r'^([A-G]s?)(\d)\.mp3$')
CELLO = bank('cello', r'^([A-G]s?)(\d)\.mp3$')

def sample(b, midi, dur=None):
    base = min(b, key=lambda k: abs(k - midi))
    x = load(b[base]); r = 2 ** ((midi - base) / 12)
    if r != 1:
        idx = np.arange(0, len(x) - 1, r)
        x = np.stack([np.interp(idx, np.arange(len(x)), x[:, c]) for c in range(2)], 1)
    if dur is not None:
        n = min(len(x), int(dur * SR)); x = x[:n].copy()
        f = min(n, int(0.35 * SR)); x[n - f:] *= np.linspace(1, 0, f)[:, None]
    return x

mix_bus = {k: np.zeros((N, 2)) for k in ('piano', 'strings', 'bass', 'pulse', 'fx')}
def put(name, x, t, g=1.0, pan=0.0, fade_in=0.0):
    i = int(t * SR)
    if i >= N: return
    x = x * g
    if fade_in: f = min(len(x), int(fade_in * SR)); x[:f] *= np.linspace(0, 1, f)[:, None] ** 2
    if pan: x = x * np.array([np.sqrt(1 - pan), np.sqrt(1 + pan)])
    if i < 0: x = x[-i:]; i = 0
    j = min(N, i + len(x)); mix_bus[name][i:j] += x[:j - i]

def grid(step):
    k = -int(np.ceil(DROP / step)); out = []
    while DROP + k * step < TOTAL: out.append((k, DROP + k * step)); k += 1
    return out

# C minor: Cm – Ab – Eb – Bb   (root, violin dyad, ostinato [low, high])
PROG = [(36, (67, 75), (63, 72)), (32, (68, 72), (63, 72)), (39, (67, 70), (63, 70)), (34, (65, 74), (62, 70))]
def chord(t): return PROG[int(np.floor((t - DROP) / BAR + 1e-6)) % 4]
END = LOGO - 0.02

# piano: left-hand octave on each bar, right-hand 8th ostinato (accent on beats)
for k, t0 in grid(BAR):
    if t0 >= END or t0 + BAR < 0: continue
    root, _, _ = chord(t0 + 0.01)
    lh = min(BAR, END - t0) + 0.4
    put('piano', sample(PIANO6, root + 12, lh), t0, g=0.55, pan=-0.15)
    if t0 >= DROP - 0.01: put('piano', sample(PIANO6, root, lh), t0, g=0.45, pan=-0.2)
for k, t0 in grid(E8):
    if t0 >= END or t0 < 0: continue
    _, _, (lo, hi) = chord(t0 + 0.01)
    note = hi if k % 2 == 0 else lo
    vel = 0.30 if k % 2 else 0.42
    if t0 < DROP: vel *= 0.8
    put('piano', sample(PIANO6, note, E8 * 1.6), t0, g=vel, pan=0.18)

# strings from the drop: contrabass root + violin dyad, slow attacks
for k, t0 in grid(BAR):
    if t0 < DROP - 0.01 or t0 >= END: continue
    root, (v1, v2), _ = chord(t0 + 0.01)
    d = min(BAR, END - t0) + 0.5
    put('bass', sample(BASS, root + 12, d), t0, g=0.9, fade_in=0.08)
    put('strings', sample(VIOLIN, v1, d), t0 - 0.15, g=0.32, pan=-0.35, fade_in=0.5)
    put('strings', sample(VIOLIN, v2, d), t0 - 0.15, g=0.28, pan=0.35, fade_in=0.5)
    if k >= 4: put('strings', sample(CELLO, root + 24, min(d, 3.0)), t0, g=0.35, pan=-0.1, fade_in=0.3)

# low pulse (felt, no click): 8th-note sub thumps under the bass, beat 1 accented
t = np.arange(int(0.4 * SR)) / SR
thump = np.sin(2 * np.pi * np.cumsum(42 + 30 * np.exp(-t * 25)) / SR) * np.exp(-t * 9)
for k, t0 in grid(E8):
    if not (DROP - 0.01 <= t0 < LOGO - BAR / 2): continue
    g = 0.5 if k % 8 == 0 else (0.28 if k % 2 == 0 else 0.14)
    put('pulse', np.stack([thump, thump], 1), t0, g=g)

# into the logo: reversed piano chord swell, then the full chord + strings + boom
final = [24, 36, 43, 48, 55, 63, 67, 72]
rev = sum(sample(PIANO10, m, 2.2) * 0.22 for m in final[2:])[::-1]
put('fx', rev * np.linspace(0, 1, len(rev))[:, None] ** 2, LOGO - len(rev) / SR, g=0.9)
for i, m in enumerate(final):
    put('piano', sample(PIANO10, m, 3.2), LOGO + i * 0.008, g=0.38, pan=-0.4 + 0.1 * i)
for m, pan in ((67, -0.4), (72, 0.0), (75, 0.4)):
    put('strings', sample(VIOLIN, m, 3.0), LOGO, g=0.35, pan=pan, fade_in=0.12)
put('bass', sample(BASS, 36, 3.0), LOGO, g=1.0)
t = np.arange(int(2.5 * SR)) / SR
boom = np.tanh(1.6 * np.sin(2 * np.pi * np.cumsum(36 + 50 * np.exp(-t * 8)) / SR) * np.exp(-t * 2.0))
put('fx', np.stack([boom, boom], 1), LOGO, g=0.55)

# hall reverb, gentle bus glue
def hall(x, sec=2.8):
    t = np.arange(int(sec * SR)) / SR
    ir = np.stack([rng.standard_normal(len(t)), rng.standard_normal(len(t))], 1) * np.exp(-t * 2.4)[:, None]
    ir = signal.sosfilt(signal.butter(2, 5000, 'low', fs=SR, output='sos'), ir, axis=0)
    ir[:int(0.02 * SR)] = 0; ir /= np.abs(ir).sum(0).max() / 5
    return np.stack([signal.fftconvolve(x[:, c], ir[:, c])[:N] for c in range(2)], 1)
B = mix_bus
send = B['piano'] * 0.45 + B['strings'] * 0.6 + B['fx'] * 0.4 + B['bass'] * 0.1
dry = B['piano'] * 0.9 + B['strings'] * 0.85 + B['bass'] * 0.8 + B['pulse'] * 0.7 + B['fx'] * 0.9
mix = dry + hall(send) * 0.55
mix = signal.sosfilt(signal.butter(2, 28, 'high', fs=SR, output='sos'), mix, axis=0)
mix = np.tanh(mix * 1.1) / 1.1

# level automation: soft bed under the voice, takes over on the logo, fades out
tt = np.arange(N) / SR
g = np.full(N, 0.42)
g = np.where(tt < DROP, 0.42 * 2.2, g)                          # piano-only intro is quieter by nature
g = np.where(tt < 0.25, g * tt / 0.25, g)
sw = tt >= LOGO - 1.2
g[sw] = 0.42 + 1.6 * np.clip((tt[sw] - (LOGO - 1.2)) / 1.2, 0, 1) ** 1.5
fo = tt > TOTAL - 1.2
g[fo] *= np.clip((TOTAL - tt[fo]) / 1.2, 0, 1) ** 1.5
mix *= g[:, None]
mix = mix[:int(TOTAL * SR)]
mix = mix / np.abs(mix).max() * 0.89
wv = wave.open(os.path.join(here, 'music.wav'), 'wb'); wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
wv.writeframes((mix * 32767).astype(np.int16).tobytes()); wv.close()

pre = ('[0:a]aresample=44100,aformat=channel_layouts=stereo,apad,asplit=2[v][sc];'
       '[1:a]volume=0.27[m];[m][sc]sidechaincompress=threshold=0.03:ratio=3:attack=25:release=350[md];'
       '[v][md]amix=inputs=2:duration=shortest:normalize=0')
ins = ['-i', os.path.join(here, 'voice.mp3'), '-i', os.path.join(here, 'music.wav')]
r = subprocess.run(['ffmpeg', '-hide_banner', '-y'] + ins + ['-filter_complex', pre + ',loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json[out]',
                    '-map', '[out]', '-t', f'{TOTAL:.3f}', '-f', 'null', '-'], capture_output=True, text=True).stderr
mj = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:measured_I={mj['input_i']}:measured_TP={mj['input_tp']}"
      f":measured_LRA={mj['input_lra']}:measured_thresh={mj['input_thresh']}:offset={mj['target_offset']}")
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', pre + ',' + ln + ',aresample=44100[out]',
               '-map', '[out]', '-t', f'{TOTAL:.3f}', os.path.join(here, 'soundtrack.wav')], check=True)
print('music.wav + soundtrack.wav', TOTAL, 'drop at', DROP, 'logo at', LOGO)
