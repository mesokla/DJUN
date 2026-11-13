# Generates an original soundtrack for the reel (no samples, no licensing issues).
# Epic hook (boom, taiko-style drums, riser), whooshes on scene cuts, soft pad bed under the voice, resolve at the end.
import numpy as np, wave, pathlib
SR = 44100; DUR = 48.0; N = int(SR * DUR)
rng = np.random.default_rng(7)
out = np.zeros((N, 2))
CUTS = [7.6, 10.5, 18.8, 28.55, 34.5, 41.5]

def lp(x, fc):            # FFT low-pass
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (f / fc) ** 4); return np.fft.irfft(X, len(x))
def hp(x, fc):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (fc / np.maximum(f, 1)) ** 4); return np.fft.irfft(X, len(x))
def add(sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR); j = min(N, i + len(sig))
    if j <= i: return
    l, r = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
    out[i:j, 0] += sig[: j - i] * gain * l * 1.41; out[i:j, 1] += sig[: j - i] * gain * r * 1.41

def boom(len_s=3.0):
    t = np.arange(int(len_s * SR)) / SR
    f = 38 + 80 * np.exp(-t * 5)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.4)
    noise = lp(rng.standard_normal(len(t)), 900) * np.exp(-t * 9)
    return np.tanh(1.6 * (sub + 0.5 * noise))
def taiko(len_s=0.9, pitch=70):
    t = np.arange(int(len_s * SR)) / SR
    f = pitch + 60 * np.exp(-t * 30)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6)
    skin = lp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 35) * 0.5
    return np.tanh(1.4 * (body + skin))
def snap(len_s=0.4):
    t = np.arange(int(len_s * SR)) / SR
    return hp(rng.standard_normal(len(t)), 1500) * np.exp(-t * 18)
def whoosh(len_s=0.6):
    t = np.arange(int(len_s * SR)) / SR
    n = rng.standard_normal(len(t)); env = np.sin(np.pi * t / len_s) ** 2
    return hp(lp(n, 3000), 300) * env
def riser(len_s=1.0):
    t = np.arange(int(len_s * SR)) / SR
    n = hp(rng.standard_normal(len(t)), 800) * (t / len_s) ** 2
    tone = np.sin(2 * np.pi * np.cumsum(200 + 600 * (t / len_s) ** 2) / SR) * (t / len_s) ** 3 * 0.3
    return n * 0.6 + tone
def pad(freqs, len_s, att=0.8, rel=1.2):
    t = np.arange(int(len_s * SR)) / SR; s = np.zeros(len(t))
    for f in freqs:
        for det in (-0.25, 0.25):
            s += np.sin(2 * np.pi * (f + det) * t) + 0.3 * np.sin(2 * np.pi * 2 * (f + det) * t)
    env = np.minimum(1, t / att) * np.minimum(1, (len_s - t) / rel)
    return s / (len(freqs) * 2.6) * env

# --- hook: boom + drums building to the first cut ---
add(boom(), 0.0, 0.9)
beat = 0.6
for k, tt in enumerate(np.arange(0.6, 7.6, beat)):
    add(taiko(pitch=64 if k % 2 else 78), tt, 0.38 + 0.03 * min(k, 8), pan=(-0.2 if k % 2 else 0.2))
for tt in np.arange(4.8, 7.6, beat / 2):
    add(taiko(0.4, 120), tt, 0.16)
add(boom(1.8), 2.2, 0.55); add(snap(), 2.2, 0.35)          # «…вибачився» + crack
drone = pad([55, 82.4], 7.6, att=0.3, rel=0.6); add(lp(drone, 400), 0, 0.5)
add(riser(1.0), 6.6, 0.25)
add(boom(2.5), 7.6, 0.7)                                    # «Ось чотири задачі»

# --- whooshes on the other cuts ---
for c in CUTS[1:]:
    add(whoosh(), c - 0.35, 0.22, pan=0.3)

# --- bed under the body: Am F C G, 4 beats each ---
chords = [[110, 130.8, 164.8], [87.3, 110, 130.8], [130.8, 164.8, 196], [98, 123.5, 146.8]]
bar = beat * 4; t0 = 7.6; i = 0
while t0 < 41.5:
    L = min(bar, 41.5 - t0) + 0.6
    add(pad(chords[i % 4], L, att=0.5, rel=0.6), t0, 0.40); t0 += bar; i += 1
for tt in np.arange(7.6, 41.5, beat):                       # soft heartbeat pulse
    add(taiko(0.35, 55), tt, 0.16)

# --- ending: resolve to C major, soft hit, fade ---
add(boom(3.0), 41.5, 0.35)
add(pad([130.8, 164.8, 196, 261.6], 6.5, att=0.4, rel=3.0), 41.5, 0.30)

out /= np.max(np.abs(out)) * 1.12
fade = np.ones(N); fade[-int(1.5 * SR):] = np.linspace(1, 0, int(1.5 * SR)); out *= fade[:, None]
pcm = (out * 32767).astype(np.int16)
p = pathlib.Path(__file__).parent / "audio" / "music.wav"
with wave.open(str(p), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("ok", p)
