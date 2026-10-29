from musiclib import *
DROP=0.0; LAND=[]
M=Mix(9); r=M.r; BPM=126; B=60/BPM
# intro: pulsing filtered bass arp building
for i in range(int(DROP/(B/4))):
    tb=i*B/4; prog=tb/DROP
    m=[45,57,52,57][i%4]
    s=lpf(osc(m,0.12,'saw',(-.003,.003),r),250+2200*prog**2)*env(0.12,0.002,0.05)
    M.add(tb,s,0,0.3+0.15*prog,0.2)
for i,tl in enumerate(LAND):
    k=int(0.8*sr); x=np.arange(k)/sr; bl=np.sin(2*np.pi*nf(81+[0,3,7,10,12,15,19,22,24][i])*x)*np.exp(-x/0.25)
    M.add(tl,bl,(-.6,.6)[i%2],0.14,0.9)
nb=int((T-DROP)/B)+1
seq=[45,45,57,45,52,45,57,55]
for b in range(nb):
    tb=DROP+b*B
    M.add(tb,kick(0.3,45,170,0.1),0,0.55)
    for j in range(4):
        M.add(tb+j*B/4,noise(r,0.025,10000,0.006),(-.4,.4)[j%2],0.07 if j%2 else 0.04)
    if b%2==1: M.add(tb,noise(r,0.2,2500,0.05),0,0.15,0.5)
    for j in range(4):
        m=seq[(b*4+j)%8]; s=lpf(osc(m,0.11,'saw',(-.004,.004),r),1800)*env(0.11,0.002,0.045)
        M.add(tb+j*B/4,s,0,0.32,0.15)
    if b%4==0:
        k=int(4*B*sr); x=np.arange(k)/sr; pad=sum(np.sin(2*np.pi*nf(m)*x) for m in (69,72,76))*env(4*B,0.5,9,1,0.4)
        M.add(tb,pad,0,0.025,0.9)
M.add(DROP,noise(r,1.8,6000,0.5),0,0.05,0.7)
M.out('music_tech_groove.wav',0.5,0.5,1.4)
