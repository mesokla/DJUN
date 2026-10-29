import numpy as np, wave
sr=44100; T=8.0; n=int(sr*T); t=np.arange(n)/sr
out=np.zeros(n); rng=np.random.default_rng(7)
nf=lambda m:440*2**((m-69)/12)
def add(start,sig):
    i0=int(start*sr); L=min(len(sig),n-i0)
    if L>0: out[i0:i0+L]+=sig[:L]
def tone(m,dur,a,d,amp,harm=(1,.35,.12)):
    x=np.arange(int(dur*sr))/sr; e=np.minimum(x/a,1)*np.exp(-x/d); f=nf(m)
    return amp*e*sum(h*np.sin(2*np.pi*f*(k+1)*x*(1+0.0007*k)) for k,h in enumerate(harm))
def lp(x,k): return np.convolve(x,np.ones(k)/k,'same')
def whoosh(dur,amp):
    L=int(dur*sr); x=np.arange(L)/L; z=rng.standard_normal(L)
    return amp*(lp(z,40)*(1-x)+lp(z,10)*x)*np.sin(np.pi*x)**2
def thud(amp):
    x=np.arange(int(0.5*sr))/sr; f=45+70*np.exp(-x*25); ph=2*np.pi*np.cumsum(f)/sr
    return amp*np.sin(ph)*np.exp(-x/0.09)
# pad
pad=sum(np.sin(2*np.pi*nf(m)*t*(1+d)) for m in (45,52,57,59,64) for d in (-0.0012,0.0012))
pad=lp(pad,60)*np.clip(t/2.0,0,1)*np.clip((T-t)/1.5,0,1)
out+=0.012*pad
A={'shL':(0.0,1.1,57),'shR':(0.1,1.1,64),'bar':(0.35,1.0,69),'inkTR':(0.7,1.1,60),'inkBL':(0.85,1.1,67),'brace':(1.45,0.9,72),'O':(1.6,0.9,76),'hash':(1.75,0.9,79),'chev':(1.9,0.9,84)}
for k,(t0,d,m) in A.items():
    big=k[:2] in ('sh','in','ba')
    add(t0,whoosh(d*0.65,0.035 if big else 0.02))
    land=t0+d*0.6
    add(land,tone(m,1.5,0.003,0.28,0.16 if big else 0.13))
    if big: add(land,thud(0.22))
# completion
add(2.9,thud(0.5))
for m in (69,76,81,88): add(2.9,tone(m,4.5,0.008,1.3,0.07,(1,.3,.1,.05)))
add(3.6,tone(88,1,0.002,0.12,0.06)); add(4.2,tone(93,1,0.002,0.12,0.05))
out*=np.clip((T-t)/0.8,0,1)
rev=np.zeros(n)
for dl,g in ((0.09,0.35),(0.19,0.25),(0.31,0.17),(0.47,0.1)):
    i=int(dl*sr); rev[i:]+=g*out[:-i]
L=out+0.7*rev; R=out+0.7*np.roll(rev,int(0.017*sr))
st=np.stack([L,R],1); st=st/np.max(np.abs(st))*0.89
w=wave.open('story_1_sound.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
