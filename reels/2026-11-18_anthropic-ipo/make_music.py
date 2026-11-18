"""Light lo-fi bed for the reel, synthesized (no licensing issues).
Quiet under the voice, swells and resolves on the end card (logo).
usage: python3 make_music.py  -> music.wav, soundtrack.wav (voice + music)"""
import numpy as np, wave, subprocess, json, re, os
SR = 44100
here = os.path.dirname(os.path.abspath(__file__))
tm = json.loads(re.search(r'window.TIMING = (.*);', open(os.path.join(here, 'timing.js')).read()).group(1))
TOTAL, LOGO = tm['total'], tm['starts'][-1]
BPM = 92; beat = 60 / BPM; bar = 4 * beat
n = int(TOTAL * SR) + SR
L = np.zeros(n); R = np.zeros(n)
def note(f): return 440 * 2 ** ((f - 69) / 12)
def add(sig, t, pan=0.0, g=1.0):
    i = int(t * SR); j = min(n, i + len(sig)); s = sig[:j - i] * g
    L[i:j] += s * (1 - pan) ** 0.5; R[i:j] += s * (1 + pan) ** 0.5
def epiano(midi, dur, vel=1.0):
    t = np.arange(int((dur + 1.2) * SR)) / SR; f = note(midi)
    env = np.exp(-t * 2.2) * (1 - np.exp(-t * 300))
    s = np.sin(2*np.pi*f*t) + 0.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*4) + 0.12*np.sin(2*np.pi*3*f*t)*np.exp(-t*7)
    s *= 1 + 0.004*np.sin(2*np.pi*5*t)
    return s * env * vel * 0.18
def bell(midi, vel=1.0):
    t = np.arange(int(3.5 * SR)) / SR; f = note(midi)
    s = np.sin(2*np.pi*f*t) + 0.5*np.sin(2*np.pi*2.76*f*t)*np.exp(-t*3) + 0.25*np.sin(2*np.pi*5.4*f*t)*np.exp(-t*6)
    return s * np.exp(-t * 1.3) * (1 - np.exp(-t * 400)) * vel * 0.12
def bass(midi, dur):
    t = np.arange(int(dur * SR)) / SR; f = note(midi)
    env = np.minimum(1, t * 40) * np.exp(-t * 0.9) * np.minimum(1, (dur - t) * 20).clip(0)
    return (np.sin(2*np.pi*f*t) + 0.2*np.sin(2*np.pi*2*f*t)) * env * 0.22
def kick():
    t = np.arange(int(0.35 * SR)) / SR
    return np.sin(2*np.pi*(45 + 70*np.exp(-t*30))*t) * np.exp(-t*9) * 0.35
rng = np.random.default_rng(7)
def hat(g=1.0):
    t = np.arange(int(0.06 * SR)) / SR; s = rng.standard_normal(len(t)); s = np.diff(s, prepend=0)
    return s * np.exp(-t * 70) * 0.035 * g
# Am7 – Fmaj7 – Cmaj7 – G6
prog = [(57, [60, 64, 67, 69]), (53, [57, 60, 64, 65]), (48, [55, 59, 60, 64]), (55, [55, 59, 62, 64])]
mel = [76, 74, 72, 74, 76, 79, 76, 74]
t = 0.0; k = 0
while t < LOGO - 0.05:
    root, ch = prog[k % 4]
    for v, m in enumerate(ch):
        add(epiano(m, bar, 0.85), t + v * 0.012, pan=-0.3 + 0.2 * v)
    add(epiano(ch[1] + 12, beat, 0.5), t + 2.5 * beat, pan=0.3)
    add(bass(root - 12, bar * 0.95), t)
    if k >= 1:
        for b in range(4):
            if b in (0, 2): add(kick(), t + b * beat)
            add(hat(), t + b * beat + beat / 2, pan=0.4)
            add(hat(0.5), t + b * beat + 3 * beat / 4, pan=0.4)
    if k >= 2:
        add(bell(mel[(2 * k) % 8], 0.55), t + beat, pan=0.25)
        add(bell(mel[(2 * k + 1) % 8], 0.45), t + 3 * beat, pan=-0.25)
    t += bar; k += 1
# end card: resolving Cmaj9 + bell arpeggio on the logo
for v, m in enumerate([48, 55, 60, 64, 67, 71, 74]):
    add(epiano(m, 2.5, 1.0), LOGO + v * 0.03, pan=-0.4 + 0.12 * v)
add(bass(36, 2.6), LOGO)
for i, m in enumerate([72, 76, 79, 84]):
    add(bell(m, 0.8), LOGO + 0.15 + i * 0.18, pan=(-1) ** i * 0.3)
# gain automation: quiet bed under the voice, swell on the logo, fade out
tt = np.arange(n) / SR
g = np.full(n, 0.30)
g = np.where(tt < 0.6, 0.30 * tt / 0.6, g)
sw = (tt >= LOGO - 0.4)
g[sw] = 0.30 + (1.0 - 0.30) * np.clip((tt[sw] - (LOGO - 0.4)) / 0.5, 0, 1)
fo = tt > TOTAL - 0.9
g[fo] *= np.clip((TOTAL - tt[fo]) / 0.9, 0, 1)
L *= g; R *= g
# soft room: two short delays
for d, a in ((0.031, 0.25), (0.047, 0.2)):
    k_ = int(d * SR); L[k_:] += R[:-k_] * a; R[k_:] += L[:-k_] * a
st = np.stack([L, R], 1)[:int(TOTAL * SR)]
st = st / np.abs(st).max() * 0.6
wv = wave.open(os.path.join(here, 'music.wav'), 'wb'); wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
wv.writeframes((st * 32767).astype(np.int16).tobytes()); wv.close()
# mix with the voice; music ducks a bit more while the voice is speaking
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(here, 'voice.mp3'), '-i', os.path.join(here, 'music.wav'), '-filter_complex',
    '[0:a]aresample=44100,aformat=channel_layouts=stereo,apad,asplit=2[v][sc];'
    '[1:a]volume=0.55[m];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=350[md];'
    '[v][md]amix=inputs=2:duration=shortest:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[out]',
    '-map', '[out]', '-t', f'{TOTAL:.3f}', os.path.join(here, 'soundtrack.wav')], check=True)
print('music.wav + soundtrack.wav', TOTAL, 'logo at', LOGO)
