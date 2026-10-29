import numpy as np, wave
from scipy.signal import fftconvolve, butter, lfilter
sr=44100; T=8.0; n=int(sr*T); t=np.arange(n)/sr; rng=np.random.default_rng(21)
nf=lambda m:440*2**((m-69)/12)
dry=np.zeros((n,2)); verb=np.zeros((n,2))
def add(st,sig,pan=0.0,g=1.0,send=0.0):
    i0=int(st*sr); m=min(len(sig),n-i0)
    if m<=0: return
    for c,p in ((0,1-pan*0.7),(1,1+pan*0.7)):
        dry[i0:i0+m,c]+=sig[:m]*g*p; verb[i0:i0+m,c]+=sig[:m]*g*p*send
def lpf(x,fc,o=2): b,a=butter(o,min(0.99,fc/(sr/2))); return lfilter(b,a,x)
def hpf(x,fc,o=2): b,a=butter(o,fc/(sr/2),'high'); return lfilter(b,a,x)
def envl(m,a,d,s=0,r=0.05):
    x=np.arange(m)/sr; e=np.minimum(x/a,1)*(s+(1-s)*np.exp(-x/d)); rr=int(r*sr)
    if 0<rr<m: e[-rr:]*=np.linspace(1,0,rr)
    return e
def supersaw(m,dur,cut,g=1):
    k=int(dur*sr); x=np.arange(k)/sr; s=np.zeros(k)
    for d in (-0.012,-0.006,0,0.006,0.012): s+=2*((x*nf(m)*(1+d/2)+rng.random())%1)-1
    return g*lpf(s/5,cut)
BPM=144; B=60/BPM  # half-time trap feel
DROP=2.9
chords=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]  # Am F C G (moody)
roots=[33,29,36,31]
# intro: filtered dark pad swelling + piano-ish bell melody on landings
for i in range(2):
    ch=chords[i]; st=i*1.45
    for m in ch: add(st,supersaw(m,1.6,500+1200*i,0.05)*envl(int(1.6*sr),0.4,9,1,0.4),0,1,0.6)
A=[(0.0,1.1,76),(0.1,1.1,72),(0.35,1.0,69),(0.7,1.1,76),(0.85,1.1,79),(1.45,0.9,81),(1.6,0.9,79),(1.75,0.9,76),(1.9,0.9,84)]
for i,(t0,d,m) in enumerate(A):
    k=int(1.2*sr); x=np.arange(k)/sr
    bell=(np.sin(2*np.pi*nf(m)*x)+0.3*np.sin(2*np.pi*nf(m)*2*x)+0.15*np.sin(2*np.pi*nf(m)*3.01*x))*np.exp(-x/0.35)*np.minimum(x/0.003,1)
    add(t0+d*0.6,bell,(-0.5,0.5)[i%2],0.09,0.8)
# riser: reverse swell of chord into drop (no noise)
k=int(1.0*sr); x=np.arange(k)/sr
sw=sum(np.sin(2*np.pi*nf(m+12)*x) for m in chords[0])*(x/x[-1])**3
add(DROP-1.0,sw,0,0.05,0.7)
# drums
def kick808(m,dur):
    k=int(dur*sr); x=np.arange(k)/sr; f=nf(m)+nf(m)*3*np.exp(-x*40); ph=2*np.pi*np.cumsum(f)/sr
    s=np.sin(ph)*envl(k,0.002,0.7,0.35,0.1); return np.tanh(1.8*s)/np.tanh(1.8)
def snare():
    k=int(0.3*sr); z=hpf(rng.standard_normal(k),1200)*envl(k,0.001,0.09); x=np.arange(k)/sr
    return z*0.8+0.4*np.sin(2*np.pi*190*x)*np.exp(-x/0.05)
def hat(): k=int(0.04*sr); return hpf(rng.standard_normal(k),7000)*envl(k,0.0005,0.012)
add(DROP,kick808(33,4*B),0,0.32)
crash=hpf(rng.standard_normal(int(2.5*sr)),5000)*envl(int(2.5*sr),0.002,0.7); add(DROP,crash,0,0.05,0.5)
bar=4*B
beats=int((T-DROP)/B)+1
for b in range(beats):
    tb=DROP+b*B; ci=(b//4)%4
    if b%4==2: add(tb,snare(),0,0.42,0.35)
    if b>0 and b%4==0: add(tb,kick808(roots[ci],min(4*B,T-tb)),0,0.3)
    if b%2==0:
        k=int(0.18*sr); x=np.arange(k)/sr; add(tb,np.sin(2*np.pi*np.cumsum(55+140*np.exp(-x*45))/sr)*np.exp(-x/0.06),0,0.35)
    if b%4==3 and b%8==7: add(tb+B/2,kick808(roots[ci]+2,0.4),0,0.22)
    # hats: 8ths with 32nd rolls at bar ends
    roll = (b%4==3)
    sub=8 if roll else 2
    for j in range(sub): add(tb+j*B/sub,hat(),0.25*((-1)**j),0.09 if j%2==0 else 0.06)
# moody chords + lead after drop
for i in range(int((T-DROP)/bar)+1):
    st=DROP+i*bar; ch=chords[i%4]
    for m in ch: add(st,supersaw(m,bar+0.2,1800,0.06)*envl(int((bar+0.2)*sr),0.15,9,1,0.15),0,1,0.5)
lead=[(0,81),(1.5,79),(2,76),(3,84),(4,81),(5.5,79),(6,76),(7,72)]
for dt,m in lead:
    st=DROP+dt*B
    if st>=T-0.3: break
    k=int(0.55*sr); x=np.arange(k)/sr
    s=(np.sin(2*np.pi*nf(m)*x+0.6*np.sin(2*np.pi*nf(m)*2*x)))*envl(k,0.01,0.3,0.3,0.1)
    add(st,lpf(s,3500),0.2,0.07,0.9)
# reverb
L=int(2.4*sr); x=np.arange(L)/sr
ir=[lpf(rng.standard_normal(L)*np.exp(-x/0.6),5000) for _ in range(2)]; ir=[i/np.sqrt(np.sum(i**2)) for i in ir]
wet=np.stack([fftconvolve(verb[:,0],ir[0])[:n],fftconvolve(verb[:,1],ir[1])[:n]],1)
mix=dry+wet*0.6
mix=np.stack([hpf(mix[:,0],25),hpf(mix[:,1],25)],1)
mix*=np.clip((T-t)/0.9,0,1)[:,None]
mix/=np.max(np.abs(mix)); mix=np.tanh(mix*1.3)/np.tanh(1.3)*0.9
w=wave.open('story_1_music_rnb.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close()
