from musiclib import *
M=Mix(17); r=M.r; BPM=100; B=60/BPM; DROP=6.8
def rhodes(m,dur,v=1):
    k=int(dur*sr); x=np.arange(k)/sr; f=nf(m)
    s=np.sin(2*np.pi*f*x+1.0*np.exp(-x/0.35)*np.sin(2*np.pi*f*x))*np.exp(-x/1.4)+0.25*np.sin(2*np.pi*2*f*x)*np.exp(-x/0.4)
    return v*s*np.minimum(x/0.004,1)*(1+0.12*np.sin(2*np.pi*5*x))
def ping(m,v=1):
    k=int(0.9*sr); x=np.arange(k)/sr; f=nf(m)
    return v*(np.sin(2*np.pi*f*x)+0.4*np.sin(2*np.pi*2*f*x)*np.exp(-x/0.08))*np.exp(-x/0.18)*np.minimum(x/0.002,1)
# pre-drop: clock tick on 8ths, getting faster/louder
tt=0.0
while tt<DROP-0.1:
    p=tt/DROP; M.add(tt,lpf(noise(r,0.02,5000,0.004),12000),(-.3,.3)[int(tt*4)%2],0.10+0.12*p)
    tt+= B/2 if tt<4.5 else B/4
# notification pings synced with visuals
NT=[0.35,1.0,1.6,2.15,2.65,3.1,3.5,3.85]; ms=[76,79,77,81,79,83,82,86]
for t0,m in zip(NT,ms): M.add(t0,ping(m,0.9),0,0.14,0.5)
# low tension pad
k=int(DROP*sr); x=np.arange(k)/k
pad=sum(osc(m,DROP,'saw',(-.004,0,.004),r) for m in (45,52,57,60))
pad=np.concatenate([lpf(pad[i:i+2205],200+1800*(i/k)**2) for i in range(0,k,2205)])[:k]*(0.3+0.7*x)
M.add(0,pad,0,0.07,0.4)
# riser 5.0 -> drop
k=int(1.8*sr); x=np.arange(k)/k; z=r.standard_normal(k)
ris=np.concatenate([hpf(z[i:i+2205],300+6000*(i/k)) for i in range(0,k,2205)])[:k]*x**2
M.add(DROP-1.8,ris,0,0.06,0.5)
# drop groove
ch=[[57,60,64,67,71],[53,57,60,64],[48,52,55,59],[55,59,62,64]]
bs=[33,29,36,31]
nb=int((T-DROP)/B)+1
for b in range(nb):
    tb=DROP+b*B; c=(b//4)%4
    M.add(tb,kick(0.35,48,120,0.14),0,0.5 if b%2==0 else 0.35)
    if b%2==1: M.add(tb,noise(r,0.22,1800,0.06),0,0.16,0.5)
    M.add(tb+B*0.58,noise(r,0.04,8000,0.012),0.3,0.08)
    M.add(tb+B*0.25,noise(r,0.02,9000,0.006),-0.3,0.04)
    if b%4==0:
        for j,m in enumerate(ch[c]): M.add(tb+j*0.015,rhodes(m,4*B+0.3,0.5),(j-2)/4,0.09,0.6)
        sb=np.sin(2*np.pi*nf(bs[c])*np.arange(int(4*B*sr))/sr)*env(4*B,0.02,9,0.8,0.1)
        M.add(tb,sb,0,0.22)
# AI chime + check chimes
M.add(DROP+0.6,ping(88,1),0,0.13,0.7)
for i,m in enumerate([81,84,88,91]): M.add(DROP+1.3+i*0.55,ping(m,0.8),(-.3,.3)[i%2],0.12,0.7)
# end chord
for j,m in enumerate([45,57,64,67,71,76]): M.add(11.6+j*0.02,rhodes(m,3.4,0.6),(j-3)/5,0.1,0.8)
M.add(11.6,kick(0.5,40,90,0.3),0,0.5)
M.out('reel_music_v2.wav',0.7,0.5,1.25)
