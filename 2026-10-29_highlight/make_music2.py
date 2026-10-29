import numpy as np, wave
from scipy.signal import fftconvolve, butter, lfilter
sr=44100; T=8.0; n=int(sr*T); t=np.arange(n)/sr; rng=np.random.default_rng(5)
nf=lambda m:440*2**((m-69)/12)
dry=np.zeros((n,2))
def add(st,sig,pan=0.0,g=1.0):
    i0=int(st*sr); m=min(len(sig),n-i0)
    if m>0: dry[i0:i0+m,0]+=sig[:m]*g*(1-pan*0.6); dry[i0:i0+m,1]+=sig[:m]*g*(1+pan*0.6)
def piano(m,dur=3.5,vel=1.0):
    f=nf(m); x=np.arange(int(dur*sr))/sr; s=np.zeros_like(x)
    B=0.0004
    for k in range(1,9):
        fk=f*k*np.sqrt(1+B*k*k); amp=vel*(0.9**(k-1))/k**0.6
        dec=1.8/(1+0.45*(k-1))*(440/f)**0.25
        s+=amp*np.sin(2*np.pi*fk*x+rng.uniform(0,6.28))*np.exp(-x/dec)
    att=np.minimum(x/0.004,1); ham=np.exp(-x/0.02)*rng.standard_normal(len(x))*0.02
    b,a=butter(2,min(0.99,f*6/(sr/2)))
    return lfilter(b,a,(s+ham)*att)
def pad(ms,dur,g):
    x=np.arange(int(dur*sr))/sr; s=np.zeros_like(x)
    for m in ms:
        for d in (-0.003,0,0.003):
            s+=np.sin(2*np.pi*nf(m)*(1+d)*x)+0.2*np.sin(2*np.pi*2*nf(m)*(1+d)*x)
    e=np.minimum(x/1.2,1)*np.clip((dur-x)/1.5,0,1)
    return g*s*e
# gentle intro pad (Fmaj9 colour), swelling
add(0.0,pad([41,48,57,64],8.0,0.006),0)
# melody on landings: ascending, airy (C major pentatonic over F)
A=[(0.0,1.1,69),(0.1,1.1,72),(0.35,1.0,76),(0.7,1.1,79),(0.85,1.1,81),(1.45,0.9,84),(1.6,0.9,88),(1.75,0.9,91),(1.9,0.9,93)]
for i,(t0,d,m) in enumerate(A):
    add(t0+d*0.6,piano(m,3.0,0.5 if i<5 else 0.4),(-0.5,0.5)[i%2])
# resolve chord at assembly: low F + Fmaj9 voicing, rolled
st=2.9
for j,m in enumerate([29,41,48,57,60,64,67,72]):
    add(st+j*0.025,piano(m,5.0,0.85 if m<45 else 0.55),(j-4)/6)
# soft closing motif
for k,(dt,m) in enumerate([(4.4,76),(4.9,79),(5.4,84)]):
    add(dt,piano(m,2.8,0.35),(-0.3,0.3,0)[k])
# reverb: synthetic stereo IR
L=int(2.8*sr); x=np.arange(L)/sr
irL=rng.standard_normal(L)*np.exp(-x/0.75); irR=rng.standard_normal(L)*np.exp(-x/0.75)
b,a=butter(1,6000/(sr/2)); irL=lfilter(b,a,irL); irR=lfilter(b,a,irR)
irL/=np.sqrt(np.sum(irL**2)); irR/=np.sqrt(np.sum(irR**2))
wet=np.stack([fftconvolve(dry[:,0],irL)[:n],fftconvolve(dry[:,1],irR)[:n]],1)
mix=dry*0.75+wet*0.55
mix*=np.clip((T-t)/1.2,0,1)[:,None]
mix/=np.max(np.abs(mix)); mix*=0.9
w=wave.open('story_1_music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close()
