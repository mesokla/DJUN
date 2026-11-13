# Original melodic soundtrack for the reel, generated in code (no samples).
# 100 BPM, A minor: piano arpeggios + bass + soft pad + a simple lead motif; resolves to C major at the end.
# Also renders the message notification sounds as a separate stem.
import numpy as np, wave, pathlib
SR = 44100; DUR = 44.8; N = int(SR * DUR)
BEAT = 0.6; BAR = BEAT * 4
HERE = pathlib.Path(__file__).parent
mus = np.zeros((N, 2)); sfx = np.zeros((N, 2))

def hz(m): return 440 * 2 ** ((m - 69) / 12)        # MIDI -> Hz
def put(buf, sig, t0, g=1.0, pan=0.0):
    i = int(t0 * SR); j = min(N, i + len(sig))
    if j <= i: return
    buf[i:j, 0] += sig[: j - i] * g * np.sqrt((1 - pan) / 2) * 1.41
    buf[i:j, 1] += sig[: j - i] * g * np.sqrt((1 + pan) / 2) * 1.41

def piano(m, L=1.6, bright=1.0):
    t = np.arange(int(L * SR)) / SR; f = hz(m); s = np.zeros(len(t))
    for k, a in enumerate([1, .5, .28, .16, .09, .05], 1):
        s += a * bright ** (k - 1) * np.sin(2 * np.pi * f * k * t * (1 + 0.0004 * k)) * np.exp(-t * (1.8 + 1.1 * k))
    att = np.minimum(1, t / 0.004)
    return s * att * 0.5
def bell(m, L=2.0):
    t = np.arange(int(L * SR)) / SR; f = hz(m)
    s = np.sin(2 * np.pi * f * t) * np.exp(-t * 2.2) + .35 * np.sin(2 * np.pi * f * 2.0 * t) * np.exp(-t * 3.5) \
        + .15 * np.sin(2 * np.pi * f * 3.01 * t) * np.exp(-t * 5)
    return s * np.minimum(1, t / 0.006) * 0.45
def bass(m, L):
    t = np.arange(int(L * SR)) / SR; f = hz(m)
    s = np.sin(2 * np.pi * f * t) + .3 * np.sin(2 * np.pi * 2 * f * t)
    return s * np.minimum(1, t / 0.02) * np.minimum(1, (L - t) / 0.15) * np.exp(-t * 0.6) * 0.5
def pad(ms, L):
    t = np.arange(int(L * SR)) / SR; s = np.zeros(len(t))
    for m in ms:
        for d in (-0.3, 0.3): s += np.sin(2 * np.pi * (hz(m) + d) * t)
    return s / (2 * len(ms)) * np.minimum(1, t / 0.6) * np.minimum(1, (L - t) / 0.8) * 0.5
def kick():
    t = np.arange(int(0.35 * SR)) / SR
    return np.sin(2 * np.pi * np.cumsum(45 + 70 * np.exp(-t * 35)) / SR) * np.exp(-t * 9) * 0.8
def swell(L=1.2):                       # soft reverse-cymbal style swell
    t = np.arange(int(L * SR)) / SR
    n = np.random.default_rng(3).standard_normal(len(t))
    X = np.fft.rfft(n); f = np.fft.rfftfreq(len(n), 1 / SR); X *= (f > 3000) / (1 + (f / 9000) ** 2)
    return np.fft.irfft(X, len(n)) * (t / L) ** 3 * 0.5

# chords as MIDI: Am, F, C, G  (root for bass, arp tones)
CH = [(45, [57, 60, 64, 69]), (41, [57, 60, 65, 69]), (48, [55, 60, 64, 67]), (43, [55, 59, 62, 67])]
END = 41.5
# lead motif (bar-relative beat, midi, length beats) for one 4-bar cycle
MOTIF = [(0, 76, 1.5), (1.5, 74, .5), (2, 72, 1), (3, 71, 1),
         (4, 72, 2), (6, 69, 2),
         (8, 67, 1.5), (9.5, 69, .5), (10, 72, 1), (11, 74, 1),
         (12, 71, 3)]

bar_i = 0; t0 = 0.0
while t0 < END - 0.01:
    root, arp = CH[bar_i % 4]
    put(mus, bass(root, BAR), t0, 0.55)
    put(mus, pad([m - 12 for m in arp[:3]], BAR + 0.8), t0, 0.35)
    pattern = [0, 1, 2, 3, 2, 1, 2, 3]                      # 8th-note arpeggio
    for k, p in enumerate(pattern):
        put(mus, piano(arp[p], 1.2, 0.8), t0 + k * BEAT / 2, 0.42 if k % 2 == 0 else 0.32, pan=-0.25 + 0.5 * (p / 3))
    t0 += BAR; bar_i += 1

def lead(start, cycles, g):
    for c in range(cycles):
        for b, m, l in MOTIF:
            tt = start + c * 4 * BAR + b * BEAT
            if tt < END - 0.2: put(mus, bell(m, max(1.2, l * BEAT + 0.8)), tt, g, pan=0.15)
lead(0.0, 1, 0.55)            # catchy motif right in the hook (0-9.6 s)
lead(4 * BAR * 2, 1, 0.30)    # quieter repeat later in the body (19.2-28.8 s)

# hook energy: gentle swell into the first downbeat, soft kick on beats until the first cut
put(mus, swell(1.0), 0.0, 0.0)
for tt in np.arange(0, 7.6, BEAT): put(mus, kick(), tt, 0.45)
put(mus, swell(1.2), 7.6 - 1.2, 0.35)

# ending: C major chord + final melody note, ring out
for m in (48, 60, 64, 67, 72): put(mus, piano(m, 4.0, 0.9), END, 0.45)
put(mus, pad([48, 55, 60, 64], 6.0), END, 0.5); put(mus, bell(76, 4.0), END + 0.6, 0.5)

# notification sounds for the chat bubbles (scene 01 starts at 10.5 s; bubbles at +0.8 and +1.9)
def notif(m1, m2):
    t = np.arange(int(0.5 * SR)) / SR
    a = np.sin(2 * np.pi * hz(m1) * t) * np.exp(-t * 18)
    b = np.zeros(len(t)); o = int(0.09 * SR); tb = t[: len(t) - o]
    b[o:] = np.sin(2 * np.pi * hz(m2) * tb) * np.exp(-tb * 12)
    return (a + b) * 0.6
put(sfx, notif(84, 88), 6.55 + 1.6, 0.9)    # client message
put(sfx, notif(88, 91), 6.55 + 2.9, 0.9)    # bot reply

def save(buf, name, fade=True):
    b = buf / max(1e-9, np.max(np.abs(buf))) * 0.89
    if fade:
        f = np.ones(N); f[-int(2 * SR):] = np.linspace(1, 0, int(2 * SR)); b *= f[:, None]
    with wave.open(str(HERE / "audio" / name), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((b * 32767).astype(np.int16).tobytes())
save(mus, "music.wav"); save(sfx, "sfx.wav", fade=False); print("ok")
