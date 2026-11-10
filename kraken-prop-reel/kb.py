import sys
from PIL import Image
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB'); W,H=im.size; print(W,H)
# remove mouse cursor (copy clean patch from above)
im.paste(im.crop((1862,780,1912,830)),(1862,860)); im.paste(im.crop((1862,780,1912,830)),(1862,900))
ar=563/1000
K=[(0.0,(1440,697,2478)),(0.4,(1440,697,2478)),(0.95,(592,880,1180)),(2.0,(592,880,1180)),
   (2.55,(1440,880,1180)),(3.55,(1440,880,1180)),(4.1,(2288,880,1180)),(5.45,(2288,880,1180))]
def ease(u): return u*u*(3-2*u)
fps=30; n=int(5.45*fps)
for i in range(n):
    t=i/fps
    for (t0,a),(t1,b) in zip(K,K[1:]):
        if t0<=t<=t1: break
    u=ease((t-t0)/(t1-t0)) if t1>t0 else 0
    cx,cy,w=[a[j]+(b[j]-a[j])*u for j in range(3)]
    h=w*ar; x0=max(0,min(W-w,cx-w/2)); y0=max(0,min(H-h,cy-h/2))
    im.crop((x0,y0,x0+w,y0+h)).resize((1000,563),Image.LANCZOS).save(f'{out}/f{i:04d}.png')
