from musiclib import *
M=Mix(4); r=M.r; BPM=84; B=60/BPM
def epiano(m,dur,v=1):
    k=int(dur*sr); x=np.arange(k)/sr; f=nf(m)
    s=np.sin(2*np.pi*f*x+1.2*np.exp(-x/0.4)*np.sin(2*np.pi*f*x))*np.exp(-x/1.2)+0.2*np.sin(2*np.pi*2*f*x)*np.exp(-x/0.5)
    return v*s*np.minimum(x/0.003,1)*(1+0.15*np.sin(2*np.pi*4.5*x))
ch=[[53,57,60,64,67],[52,55,59,62],[50,53,57,60,64],[55,59,62,65]]  # Fmaj9 Em7 Dm9 G7
# vinyl crackle bed
cr=np.zeros(n); idx=r.integers(0,n,600); cr[idx]=r.standard_normal(600)*0.6; cr=hpf(cr,1500)+hpf(r.standard_normal(n),3000)*0.01
M.add(0,cr,0,0.15)
for j,m in enumerate(ch[0]): M.add(0.3+j*0.06,epiano(m,2.6,0.5),(j-2)/4,0.12,0.6)
for i,tl in enumerate(LAND): M.add(tl,epiano([72,76,79,81,84,86,88,91,93][i],1.2,0.35),(-.5,.5)[i%2],0.12,0.7)
nb=int((T-DROP)/B)+1
for b in range(nb):
    tb=DROP+b*B; c=(b//2)%4
    sw=B*0.08 if b%2 else 0
    if b%2==0: M.add(tb,kick(0.4,45,110,0.15),0,0.6)
    else: M.add(tb,lpf(noise(r,0.25,900,0.08),5000),0,0.3,0.3)
    for j in range(2): M.add(tb+j*B/2+(B*0.06 if j else 0),lpf(noise(r,0.05,6000,0.015),9000),0.3,0.07)
    if b%2==0:
        for j,m in enumerate(ch[c]): M.add(tb+j*0.02,epiano(m,2*B+0.3,0.45),(j-2)/4,0.1,0.5)
        bs=np.sin(2*np.pi*nf(ch[c][0]-24)*np.arange(int(1.5*B*sr))/sr)*env(1.5*B,0.01,0.5,0.4)
        M.add(tb,bs,0,0.3)
M.out('music_lofi.wav',0.8,0.55,1.15)
