import numpy as np, wave
sr=44100; T=8.0; n=int(sr*T); t=np.arange(n)/sr
L=np.zeros(n); R=np.zeros(n); rng=np.random.default_rng(11)
nf=lambda m:440*2**((m-69)/12)
def add(st,sig,pan=0.0,g=1.0):
    i0=int(st*sr); m=min(len(sig),n-i0)
    if m<=0: return
    L[i0:i0+m]+=sig[:m]*g*(1-pan)/1; R[i0:i0+m]+=sig[:m]*g*(1+pan)/1
def lp(x,k): return np.convolve(x,np.ones(k)/k,'same') if k>1 else x
def saw(f,dur): x=np.arange(int(dur*sr))/sr; return 2*((x*f)%1)-1
def env(dur,a,d,s=0.0,r=0.05):
    m=int(dur*sr); x=np.arange(m)/sr; e=np.minimum(x/a,1)*(s+(1-s)*np.exp(-x/d)); rr=int(r*sr)
    if rr and rr<m: e[-rr:]*=np.linspace(1,0,rr)
    return e
DROP=2.9; BEAT=0.5
# --- build: riser noise + rising tone
m=int(DROP*sr); x=np.arange(m)/m; z=rng.standard_normal(m)
riser=(lp(z,int(60-50*x[-1]))*0)+np.concatenate([lp(z[i:i+4410],int(max(2,40*(1-i/m)))) for i in range(0,m,4410)])[:m]
riser*=x**2*0.18; add(0,riser,-0.1); add(0,riser*0.9,0.1)
f0=110*2**(x*2); ph=2*np.pi*np.cumsum(f0)/sr; add(0,0.05*np.sin(ph)*x**1.5)
# ticking hats accelerating
tt=0.0; step=0.25
while tt<DROP-0.05:
    h=lp(rng.standard_normal(int(0.03*sr)),2)*env(0.03,0.001,0.008); h-=lp(h,8)
    add(tt,h,0.3 if int(tt*8)%2 else -0.3,0.12+0.1*tt/DROP); step=max(0.0625,step*0.93); tt+=step
# landing plucks (same timing as animation)
A=[(0.0,1.1,57),(0.1,1.1,64),(0.35,1.0,69),(0.7,1.1,60),(0.85,1.1,67),(1.45,0.9,72),(1.6,0.9,76),(1.75,0.9,79),(1.9,0.9,84)]
for i,(t0,d,mm) in enumerate(A):
    s=lp(saw(nf(mm),0.6),6)*env(0.6,0.002,0.12)
    add(t0+d*0.6,s,(-0.4,0.4)[i%2],0.12)
# silence gap before drop
# --- drop
def kick(g=1.0):
    d=0.45; x=np.arange(int(d*sr))/sr; f=48+110*np.exp(-x*32); ph=2*np.pi*np.cumsum(f)/sr
    return g*np.sin(ph)*np.exp(-x/0.16)
def clap():
    d=0.25; z=rng.standard_normal(int(d*sr)); z=z-lp(z,10); return z*env(d,0.002,0.06)
def hat(): d=0.05; z=rng.standard_normal(int(d*sr)); z=z-lp(z,4); return z*env(d,0.001,0.015)
add(DROP,kick(1.0)); 
imp=lp(rng.standard_normal(int(2.5*sr)),3)*env(2.5,0.002,0.6); add(DROP,imp,-0.2,0.10); add(DROP,imp[::-1][::-1],0.2,0.10)
chords=[(45,[57,60,64,69]),(41,[57,60,65,69]),(48,[55,60,64,67]),(43,[55,59,62,67])]
for b in range(int((T-DROP)/BEAT)+1):
    tb=DROP+b*BEAT
    if b>0: add(tb,kick(0.85))
    if b%2==1: add(tb,clap(),0,0.18)
    add(tb+BEAT/2,hat(),0.35,0.10); add(tb+BEAT/4,hat(),-0.35,0.05); add(tb+3*BEAT/4,hat(),-0.35,0.05)
    root,ch=chords[(b//4)%4]
    # sidechained sub bass offbeat
    bs=np.sin(2*np.pi*nf(root)*np.arange(int(BEAT*sr))/sr)*0.6+0.4*lp(saw(nf(root),BEAT),20)
    add(tb,bs*env(BEAT,0.06,1,0.9,0.05),0,0.22)
    # arp 16ths
    for k in range(4):
        mm=ch[(b*4+k)%4]+12
        s=lp(saw(nf(mm),0.2),5)*env(0.2,0.002,0.07)
        add(tb+k*BEAT/4,s,(-0.5,0.5)[k%2],0.075)
# pad from drop
pad=np.zeros(n)
for i,(root,ch) in enumerate(chords):
    st=DROP+i*4*BEAT; 
    for mm in ch:
        for det in (-0.004,0.004):
            seg=lp(saw(nf(mm)*(1+det),4*BEAT+0.3),40)*env(4*BEAT+0.3,0.25,9,1,0.3)
            add(st,seg,det*100,0.022)
# master: echo + fade
for arr in (L,R):
    e=np.zeros(n); i=int(0.375*sr); e[i:]=arr[:-i]*0.25; arr+=e
fade=np.clip((T-t)/1.0,0,1); L*=fade; R*=fade
mx=max(np.max(np.abs(L)),np.max(np.abs(R))); L/=mx; R/=mx
# soft clip for punch
L=np.tanh(L*1.4)/np.tanh(1.4); R=np.tanh(R*1.4)/np.tanh(1.4)
st=np.stack([L,R],1)*0.9
w=wave.open('story_1_music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
