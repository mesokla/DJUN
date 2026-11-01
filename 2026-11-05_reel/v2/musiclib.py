import numpy as np, wave
from scipy.signal import fftconvolve, butter, lfilter
sr=44100; T=15.0; n=int(sr*T); t=np.arange(n)/sr
nf=lambda m:440*2**((m-69)/12)
class Mix:
    def __init__(s,seed=1): s.d=np.zeros((n,2)); s.v=np.zeros((n,2)); s.r=np.random.default_rng(seed)
    def add(s,st,sig,pan=0,g=1,send=0):
        i0=int(st*sr); m=min(len(sig),n-i0)
        if m<=0 or i0<0: return
        for c,p in ((0,1-pan*0.7),(1,1+pan*0.7)):
            s.d[i0:i0+m,c]+=sig[:m]*g*p; s.v[i0:i0+m,c]+=sig[:m]*g*p*send
    def out(s,fn,decay=0.6,wet=0.5,drive=1.2):
        L=int(2.5*sr); x=np.arange(L)/sr
        ir=[lpf(s.r.standard_normal(L)*np.exp(-x/decay),6000) for _ in range(2)]; ir=[i/np.sqrt(np.sum(i**2)) for i in ir]
        w=np.stack([fftconvolve(s.v[:,0],ir[0])[:n],fftconvolve(s.v[:,1],ir[1])[:n]],1)
        m=s.d+w*wet; m=np.stack([hpf(m[:,0],28),hpf(m[:,1],28)],1)
        m*=np.clip((T-t)/0.9,0,1)[:,None]; m/=np.max(np.abs(m)); m=np.tanh(m*drive)/np.tanh(drive)*0.9
        f=wave.open(fn,'wb'); f.setnchannels(2); f.setsampwidth(2); f.setframerate(sr); f.writeframes((m*32767).astype(np.int16).tobytes()); f.close()
def lpf(x,fc,o=2): b,a=butter(o,min(0.99,fc/(sr/2))); return lfilter(b,a,x)
def hpf(x,fc,o=2): b,a=butter(o,fc/(sr/2),'high'); return lfilter(b,a,x)
def env(dur,a,d,s=0,r=0.03):
    m=int(dur*sr); x=np.arange(m)/sr; e=np.minimum(x/a,1)*(s+(1-s)*np.exp(-x/d)); rr=int(r*sr)
    if 0<rr<m: e[-rr:]*=np.linspace(1,0,rr)
    return e
def osc(m,dur,kind='saw',det=(0,),rng=None):
    k=int(dur*sr); x=np.arange(k)/sr; s=np.zeros(k)
    for d in det:
        ph=(x*nf(m)*(1+d)+ (rng.random() if rng is not None else 0))%1
        s+= (2*ph-1) if kind=='saw' else (np.sign(np.sin(2*np.pi*ph)) if kind=='sq' else np.sin(2*np.pi*ph))
    return s/len(det)
def kick(dur=0.35,f1=50,f2=160,dec=0.12):
    k=int(dur*sr); x=np.arange(k)/sr; f=f1+f2*np.exp(-x*38); return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-x/dec)
def noise(r,dur,hp,dec): k=int(dur*sr); return hpf(r.standard_normal(k),hp)*env(dur,0.0008,dec)
LAND=[0.66,0.76,0.95,1.36,1.51,1.99,2.14,2.29,2.44]; DROP=2.9
