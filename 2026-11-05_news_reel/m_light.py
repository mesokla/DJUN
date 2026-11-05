from musiclib_l import *
M=Mix(31); r=M.r; BPM=96; B=60/BPM
def keys(m,dur,v=1):
    k=int(dur*sr); x=np.arange(k)/sr; f=nf(m)
    s=np.sin(2*np.pi*f*x+0.8*np.exp(-x/0.3)*np.sin(2*np.pi*f*x))*np.exp(-x/1.6)+0.18*np.sin(2*np.pi*2*f*x)*np.exp(-x/0.5)
    return v*s*np.minimum(x/0.006,1)
def bell(m,v=1):
    k=int(1.4*sr);x=np.arange(k)/sr;f=nf(m)
    return v*(np.sin(2*np.pi*f*x)+0.25*np.sin(2*np.pi*3.01*f*x)*np.exp(-x/0.2))*np.exp(-x/0.45)*np.minimum(x/0.002,1)
ch=[[65,69,72,76],[64,67,71,74],[62,65,69,72],[60,64,67,71]]  # Fmaj7 Em7 Dm7 Cmaj7 (mid register, no bass)
mel=[84,81,79,76, 83,79,76,74, 81,77,74,72, 79,76,72,71]
nb=int(T/B)+1
for b in range(nb):
    tb=b*B; c=(b//4)%4
    if b%4==0:
        for j,m in enumerate(ch[c]): M.add(tb+j*0.03,keys(m,4*B+0.4,0.4),(j-1.5)/3,0.10,0.6)
    # soft arpeggio on 8ths
    for h in range(2):
        m=mel[(b*2+h)%16]
        M.add(tb+h*B/2,bell(m,0.5),(-.4,.4)[(b+h)%2],0.055,0.8)
    # very soft shaker on offbeats
    M.add(tb+B/2,noise(r,0.06,7000,0.02),0.3,0.025)
M.out('light_music.wav',1.0,0.6,1.05)
