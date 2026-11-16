import numpy as np, subprocess, math, os, sys
os.environ['NOCAR']='1'
import pano
from PIL import Image
W,H=1080,1350; FPS=30; T=float(sys.argv[1]) if len(sys.argv)>1 else 4
P=np.array(pano.pts); seg=np.hypot(*np.diff(P,axis=0).T); S=np.concatenate([[0],np.cumsum(seg)])
def s_at_x(b): return S[np.argmax(P[:,0]>=b)]
SEND=S[-1]
def at(s):
    s=min(max(s,0),SEND); f=lambda v,c: np.interp(v,S,P[:,c])
    a=math.degrees(math.atan2(f(min(s+6,SEND),1)-f(max(s-6,0),1), f(min(s+6,SEND),0)-f(max(s-6,0),0)))
    return f(s,0),f(s,1),a
bg=Image.open('bg.png').convert('RGB'); fg=Image.open('fg.png').convert('RGBA')
C=1000; bases={}
for nm in ('car4x.png','car4x_light.png'):
    b0=Image.new('RGBA',(C,C)); b0.paste(Image.open(nm).convert('RGBA'),(C//2-312,C//2-280)); bases[nm]=b0
cache={}
def carimg(a,nm='car4x.png'):
    k=(round(a*2)/2,nm)
    if k not in cache: cache[k]=bases[nm].rotate(-k[0],resample=Image.BICUBIC).resize((C//4,C//4),Image.LANCZOS)
    return cache[k]
NF=int(T*FPS)
def ease(u): return u*u*(3-2*u)
small=[[None]*NF for _ in range(7)]
for i in range(7):
    s0 = s_at_x(i*W)-100
    s1 = SEND if i==6 else s_at_x((i+1)*W)+100
    bgs=bg.crop((i*W,0,(i+1)*W,H)); fgs=fg.crop((i*W,0,(i+1)*W,H))
    pp=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-movflags','+faststart',f'skills_{i+1}.mp4'],stdin=subprocess.PIPE)
    for f in range(NF):
        u=f/(NF-1)
        if i==6: u=ease(u)            # last slide: glide in and stop at the dot
        
        x,y,a=at(s0+u*(s1-s0)); im=carimg(a,'car4x_light.png' if i==0 else 'car4x.png')
        fr=bgs.copy(); fr.paste(im,(int(round(x-i*W))-C//8,int(round(y))-C//8),im); fr.paste(fgs,(0,0),fgs)
        pp.stdin.write(fr.tobytes()); small[i][f]=fr.resize((540,675))
        if (f==NF//2 and i<6) or (i==6 and f==NF-1): fr.save(f'skills_{i+1}.png')
    pp.stdin.close(); pp.wait()
# swipe preview: each slide plays its full clip, then swipe
sw=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','540x675','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-vf','pad=540:676','preview_swipe.mp4'],stdin=subprocess.PIPE)
SWF=int(.4*FPS)
for i in range(7):
    for f in range(NF): sw.stdin.write(small[i][f].tobytes())
    if i<6:
        for j in range(SWF):
            u=ease((j+1)/SWF); off=int(u*540); c=Image.new('RGB',(1080,675)); c.paste(small[i][-1],(0,0)); c.paste(small[i+1][0],(540,0))
            sw.stdin.write(c.crop((off,0,off+540,675)).tobytes())
sw.stdin.close(); sw.wait(); print('done')
