import numpy as np, subprocess, math, os, sys
os.environ['NOCAR']='1'
import pano
from PIL import Image
W,H=1080,1350; FPS=30; T=float(sys.argv[1]) if len(sys.argv)>1 else 6
P=np.array(pano.pts); seg=np.hypot(*np.diff(P,axis=0).T); S=np.concatenate([[0],np.cumsum(seg)])
def s_at_x(b):  # first crossing of x=b
    i=np.argmax(P[:,0]>=b); return S[i]
SB=[s_at_x(i*W) for i in range(-1,7)]  # boundaries for slides -1..6
SEND=S[-1]
def at(s):
    s=min(max(s,0),SEND); x=np.interp(s,S,P[:,0]); y=np.interp(s,S,P[:,1])
    x2=np.interp(min(s+6,SEND),S,P[:,0]); y2=np.interp(min(s+6,SEND),S,P[:,1]); x1=np.interp(max(s-6,0),S,P[:,0]); y1=np.interp(max(s-6,0),S,P[:,1])
    return x,y,math.degrees(math.atan2(y2-y1,x2-x1))
bg=Image.open('bg.png').convert('RGB'); fg=Image.open('fg.png').convert('RGBA')
frames_small=[]
car4=Image.open('car4x.png').convert('RGBA')
# pivot (78,70) at 1x -> (312,280) at 4x; build pivot-centered canvas
C=1000; base=Image.new('RGBA',(C,C)); base.paste(car4,(C//2-312,C//2-280))
cache={}
def carimg(a):
    k=round(a*2)/2
    if k not in cache:
        r=base.rotate(-k,resample=Image.BICUBIC); cache[k]=r.resize((C//4,C//4),Image.LANCZOS)
    return cache[k]
p0=300/1080
pipes=[subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','medium','-movflags','+faststart',f'skills_{i+1}.mp4'],stdin=subprocess.PIPE) for i in range(7)]
prev=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1890x338','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-vf','pad=1890:340','pano_preview.mp4'],stdin=subprocess.PIPE)
NF=int(T*FPS)
for f in range(NF):
    p=(p0+f/NF)%1
    fr=bg.copy()
    for k in range(-1,7):
        lo=SB[k+1]
        if k<6: s=lo+p*(SB[k+2]-lo)
        else: s=lo+p*(SB[6]-SB[5])
        if s>SEND+1: s=SEND
        x,y,a=at(s)
        im=carimg(a)
        if k==6:
            fade=1.0
            if p>0.9: fade=max(0,1-(p-0.9)/0.07)
            if fade<1: im=im.copy(); im.putalpha(im.getchannel('A').point(lambda v:int(v*fade)))
        fr.paste(im,(int(round(x))-C//8,int(round(y))-C//8),im)
    fr.paste(fg,(0,0),fg)
    for i in range(7): pipes[i].stdin.write(fr.crop((i*W,0,(i+1)*W,H)).tobytes())
    prev.stdin.write(fr.resize((1890,338)).tobytes())
    if f==0:
        for i in range(7): fr.crop((i*W,0,(i+1)*W,H)).save(f'skills_{i+1}.png')
        fr.resize((1890,338)).save('pano_small.png')
    frames_small.append(fr.resize((3780,675)))
for pp in pipes+[prev]: pp.stdin.close(); pp.wait()
# swipe preview 540x675: hold 2.6s, swipe .4s
sw=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','540x675','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-vf','pad=540:676','preview_swipe.mp4'],stdin=subprocess.PIPE)
HOLD,SW=int(2.6*FPS),int(.4*FPS); g=0
for i in range(7):
    for j in range(HOLD+(SW if i<6 else 0)):
        if j<HOLD: off=i*540
        else:
            u=(j-HOLD)/SW; u=u*u*(3-2*u); off=int(i*540+u*540)
        sw.stdin.write(frames_small[g%NF].crop((off,0,off+540,675)).tobytes()); g+=1
sw.stdin.close(); sw.wait()
print('done',NF)
