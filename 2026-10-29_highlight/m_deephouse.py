from musiclib import *
M=Mix(3); r=M.r; BPM=122; B=60/BPM
ch=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[50,53,57,60]]  # Am7 Fmaj7 Cmaj7 Dm7
bass=[33,29,36,38]
# intro: filtered chord swell (sidechain-free), opening filter
k=int(DROP*sr); x=np.arange(k)/k
sw=sum(osc(m,DROP,'saw',(-.004,0,.004),r) for m in ch[0]); 
sw=np.concatenate([lpf(sw[i:i+2205],300+2500*(i/k)**2) for i in range(0,k,2205)])[:k]*x**1.5
M.add(0,sw,0,0.16,0.4)
for i,tl in enumerate(LAND): 
    s=lpf(osc(ch[0][i%4]+12,0.3,'saw',(-.006,.006),r),2500)*env(0.3,0.002,0.09); M.add(tl,s,(-.5,.5)[i%2],0.22,0.6)
# drop groove
nb=int((T-DROP)/B)+1
for b in range(nb):
    tb=DROP+b*B; c=(b//4)%4
    M.add(tb,kick(),0,0.55)
    M.add(tb+B/2,noise(r,0.12,6000,0.035),0.2,0.16,0.1)          # open-ish offbeat hat
    M.add(tb+B/4,noise(r,0.03,9000,0.008),-0.3,0.06); M.add(tb+3*B/4,noise(r,0.03,9000,0.008),-0.3,0.06)
    if b%2==1: M.add(tb,noise(r,0.25,1500,0.07),0,0.18,0.4)      # clap
    # deep chord stab on offbeat (classic house)
    if b%2==0:
        st=sum(osc(m,0.45,'saw',(-.005,.005),r) for m in ch[c]); st=lpf(st,1400)*env(0.45,0.004,0.16)
        M.add(tb+B*1.5,st,0,0.08,0.7)
    # bass: offbeat sub
    bs=np.sin(2*np.pi*nf(bass[c])*np.arange(int(B*0.45*sr))/sr)*env(B*0.45,0.004,0.2,0.6)
    M.add(tb+B/2,bs,0,0.32)
M.add(DROP,noise(r,2.2,4000,0.6),0,0.05,0.6)
M.out('music_deephouse.wav',0.55,0.45,1.3)
