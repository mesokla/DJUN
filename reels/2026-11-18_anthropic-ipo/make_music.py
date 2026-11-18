"""Smooth R&B bed for the reel (72 BPM half-time), built from real samples (see assets/samples/CREDITS.md):
Rhodes electric piano + warm pad (FluidR3), TR-808 drums, 808-style sub bass.
Intro: filtered Rhodes + pad. The beat drops on the «трильйон» line. Reverse cymbal into the logo, final chord + crash.
usage: python3 make_music.py  -> music.wav, soundtrack.wav (voice + music, ducked, -14 LUFS)"""
import numpy as np, wave, subprocess, json, re, os, functools
from scipy import signal

SR = 44100
here = os.path.dirname(os.path.abspath(__file__))
SMP = os.path.join(here, 'assets', 'samples')
tm = json.loads(re.search(r'window.TIMING = (.*);', open(os.path.join(here, 'timing.js')).read()).group(1))
TOTAL, LOGO, DROP = tm['total'], tm['starts'][-1], tm['starts'][1]
BPM = 72; BEAT = 60 / BPM; BAR = 4 * BEAT; S16 = BEAT / 4
N = int((TOTAL + 1) * SR)
rng = np.random.default_rng(3)
FLATS = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

@functools.lru_cache(None)
def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)
def inst(folder, midi, dur=None):
    m = min(max(midi, 36), 83)                                   # files cover octaves 2..5
    x = load(os.path.join(SMP, folder, f'{FLATS[m % 12]}{m // 12 - 1}.mp3'))
    if m != midi:
        r = 2 ** ((midi - m) / 12); idx = np.arange(0, len(x) - 1, r)
        x = np.stack([np.interp(idx, np.arange(len(x)), x[:, c]) for c in range(2)], 1)
    if dur is not None:
        n = min(len(x), int(dur * SR)); x = x[:n].copy(); f = min(n, int(0.25 * SR)); x[n - f:] *= np.linspace(1, 0, f)[:, None]
    return x
def drum(name): return load(os.path.join(SMP, 'tr808', name))

B = {k: np.zeros((N, 2)) for k in ('keys', 'pad', 'bass', 'kick', 'snare', 'hats', 'fx')}
def put(bus, x, t, g=1.0, pan=0.0, fade_in=0.0):
    i = int(round(t * SR))
    if i >= N: return
    x = x * g
    if fade_in: f = min(len(x), int(fade_in * SR)); x[:f] *= np.linspace(0, 1, f)[:, None] ** 2
    if pan: x = x * np.array([np.sqrt(1 - pan), np.sqrt(1 + pan)])
    if i < 0: x = x[-i:]; i = 0
    j = min(N, i + len(x)); B[bus][i:j] += x[:j - i]
def grid(step):
    k = -int(np.ceil(DROP / step)); out = []
    while DROP + k * step < TOTAL: out.append((k, DROP + k * step)); k += 1
    return out

# Fmaj9 – Em7 – Am9 – Dm9  (bass root, Rhodes voicing)
PROG = [(41, [57, 60, 64, 67]), (40, [55, 59, 62, 64]), (45, [55, 60, 64, 71]), (38, [53, 57, 60, 64])]
def chord(t): return PROG[int(np.floor((t - DROP) / BAR + 1e-6)) % 4]
END = LOGO - 0.02
CUT = LOGO - BAR / 2                                             # drums drop out for the last half bar
def swing(k): return S16 * 0.18 if k % 2 else 0.0               # lazy 16th swing

# ---------- Rhodes: chord on 1, soft re-hit on the "and" of 2, grace on 4 ----------
for k, t0 in grid(BAR):
    if t0 >= END or t0 + BAR < 0: continue
    root, notes = chord(t0 + 0.01)
    for step, vel, length in ((0, 0.55, 6), (6, 0.32, 4), (12, 0.25, 3)):
        ts = t0 + step * S16
        if ts >= END: continue
        for v, m in enumerate(notes):
            put('keys', inst('rhodes', m, length * S16 + 0.3), ts + v * 0.011, g=vel, pan=-0.25 + v * 0.17)
    if t0 >= DROP - 0.01:                                           # little top-line answer every other bar
        if k % 2 == 1:
            for s, m in ((10, notes[-1] + 5), (11, notes[-1] + 3), (14, notes[-1])):
                put('keys', inst('rhodes', m + 12, 2 * S16 + 0.2), t0 + s * S16, g=0.22, pan=0.3)

# ---------- warm pad under everything ----------
for k, t0 in grid(BAR / 2):
    if t0 >= END or t0 + BAR < 0: continue
    _, notes = chord(t0 + 0.01)
    for m in notes[1:]:
        put('pad', inst('pad', m + 12, min(BAR / 2 + 1.2, END - t0 + 0.6)), t0 - 0.05, g=0.18, fade_in=0.35)

# ---------- 808 sub bass ----------
def sub(midi, dur):
    t = np.arange(int(dur * SR)) / SR; f = 440 * 2 ** ((midi - 69) / 12)
    ph = 2 * np.pi * np.cumsum(f * (1 + 0.5 * np.exp(-t * 40))) / SR       # tiny pitch drop at the start, 808-style
    env = np.minimum(1, t / 0.005) * np.exp(-t * 1.1) * np.clip((dur - t) / 0.04, 0, 1)
    s = np.tanh(1.6 * np.sin(ph)) * env
    return np.stack([s, s], 1)
for k, t0 in grid(BAR):
    if not (DROP - 0.01 <= t0 < CUT): continue
    root, _ = chord(t0 + 0.01)
    for step, length in ((0, 6), (7, 2), (10, 5)):
        ts = t0 + step * S16
        if ts < CUT: put('bass', sub(root - 12, length * S16), ts, g=0.55)

# ---------- TR-808 drums, half-time ----------
kick, snare, clap = drum('BD2575.WAV'), drum('SD2575.WAV'), drum('CP.WAV')
ch, oh, rim = drum('CH.WAV'), drum('OH25.WAV'), drum('RS.WAV')
kick_times = []
for k, t0 in grid(BAR):
    if not (DROP - 0.01 <= t0 < CUT): continue
    for step in (0, 7, 10):
        ts = t0 + step * S16
        if ts < CUT: put('kick', kick, ts, g=0.9 if step == 0 else 0.7); kick_times.append(ts)
    put('snare', snare, t0 + 8 * S16, g=0.55); put('snare', clap, t0 + 8 * S16 + 0.006, g=0.5, pan=0.08)
    if k % 2 == 1: put('snare', rim, t0 + 14 * S16 + swing(1), g=0.22, pan=-0.2)
for k, t0 in grid(S16):
    if not (DROP - 0.01 <= t0 < CUT): continue
    step = k % 16; bar_i = (k // 16) % 2
    if bar_i == 1 and step >= 12:                                    # hat roll into the next bar (32nds)
        for r in range(2): put('hats', ch, t0 + r * S16 / 2, g=0.16 + 0.04 * r, pan=0.3)
    elif step % 2 == 0:
        put('hats', ch, t0, g=0.26 if step % 4 == 0 else 0.18, pan=0.3)
    elif step in (5, 13):
        put('hats', ch, t0 + swing(1), g=0.10, pan=0.3)
    if step == 6 and bar_i == 0: put('hats', oh, t0, g=0.12, pan=-0.3)

# gentle pump on keys/pad from the kick (keeps the groove breathing)
duck = np.ones(N)
for t0 in kick_times:
    i = int(t0 * SR); seg = np.arange(min(N - i, int(0.35 * SR))) / SR
    duck[i:i + len(seg)] = np.minimum(duck[i:i + len(seg)], 1 - 0.35 * np.exp(-seg / 0.12))
B['keys'] *= duck[:, None]; B['pad'] *= duck[:, None]

# intro: keys + pad low-passed, open up into the drop
tt = np.arange(N) / SR
def lp(x, f): return signal.sosfilt(signal.butter(2, f, 'low', fs=SR, output='sos'), x, axis=0)
xo = np.clip((tt - (DROP - 1.2)) / 1.2, 0, 1)[:, None]
for b in ('keys', 'pad'): B[b] = lp(B[b], 900) * (1 - xo) + B[b] * xo

# ---------- into the logo: reverse cymbal, final chord, crash ----------
cy = drum('CY5050.WAV'); L = min(len(cy), int(1.6 * SR))
rev = cy[:L][::-1] * np.linspace(0, 1, L)[:, None] ** 1.5
put('fx', rev, LOGO - L / SR, g=0.5)
put('fx', cy, LOGO, g=0.35)
for v, m in enumerate([41, 53, 57, 60, 64, 67, 72]):
    put('keys', inst('rhodes', m, 3.0), LOGO + v * 0.014, g=0.55, pan=-0.35 + v * 0.11)
for m in (60, 64, 67, 72):
    put('pad', inst('pad', m + 12, 3.0), LOGO, g=0.25, fade_in=0.05)
put('bass', sub(29, 2.4), LOGO, g=0.6)
put('kick', kick, LOGO, g=0.9)

# ---------- reverb + mix ----------
def plate(x, sec=2.0):
    t = np.arange(int(sec * SR)) / SR
    ir = np.stack([rng.standard_normal(len(t)), rng.standard_normal(len(t))], 1) * np.exp(-t * 3.0)[:, None]
    ir = lp(ir, 6500); ir[:int(0.012 * SR)] = 0; ir /= np.abs(ir).sum(0).max() / 5
    return np.stack([signal.fftconvolve(x[:, c], ir[:, c])[:N] for c in range(2)], 1)
# Rhodes: subtle stereo chorus via a short modulated delay
keys = B['keys']; d = (0.012 + 0.002 * np.sin(2 * np.pi * 0.6 * tt)) * SR
idx = np.clip(np.arange(N) - d, 0, N - 1)
chorus = np.stack([np.interp(idx, np.arange(N), keys[:, 1]), np.interp(idx, np.arange(N), keys[:, 0])], 1)
keys = keys * 0.85 + chorus * 0.35
send = keys * 0.35 + B['pad'] * 0.4 + B['snare'] * 0.3 + B['fx'] * 0.3
dry = keys * 0.95 + B['pad'] * 0.7 + B['bass'] * 0.85 + B['kick'] * 0.8 + B['snare'] * 0.7 + B['hats'] * 0.8 + B['fx'] * 0.8
mix = dry + plate(send) * 0.45
mix = signal.sosfilt(signal.butter(2, 25, 'high', fs=SR, output='sos'), mix, axis=0)
mix = np.tanh(mix * 1.2) / 1.2

# level automation: bed under the voice, takes over on the logo, fades out
g = np.full(N, 0.45)
g = np.where(tt < DROP, 0.45 * 3.2, g)
g = np.where(tt < 0.25, g * tt / 0.25, g)
sw = tt >= LOGO - 1.0
g[sw] = 0.45 + 1.4 * np.clip((tt[sw] - (LOGO - 1.0)) / 1.0, 0, 1) ** 1.5
fo = tt > TOTAL - 1.2
g[fo] *= np.clip((TOTAL - tt[fo]) / 1.2, 0, 1) ** 1.5
mix *= g[:, None]
mix = mix[:int(TOTAL * SR)]
mix = mix / np.abs(mix).max() * 0.89
wv = wave.open(os.path.join(here, 'music.wav'), 'wb'); wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
wv.writeframes((mix * 32767).astype(np.int16).tobytes()); wv.close()

MUSIC_VOL = 0.11
pre = ('[0:a]aresample=44100,aformat=channel_layouts=stereo,apad,asplit=2[v][sc];'
       f'[1:a]volume={MUSIC_VOL}[m];[m][sc]sidechaincompress=threshold=0.03:ratio=3:attack=25:release=350[md];'
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
