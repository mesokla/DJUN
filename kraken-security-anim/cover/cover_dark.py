import sys, numpy as np
from PIL import Image, ImageFilter
src,dst,d=sys.argv[1],sys.argv[2],int(sys.argv[3])
im=np.asarray(Image.open(src).convert('RGB')).astype(float)
H,W,_=im.shape
yy,xx=np.mgrid[0:H,0:W]
vl=(xx%120==0)&(xx>0); hl=(yy%120==119)
line=vl|hl
rects=[(235,760,70,900),(690,1480,60,1020)]
rects_w=[(175,800,15,960),(650,1540,0,1080)]
content=np.zeros((H,W),bool)
for y0,y1,x0,x1 in rects: content[y0:y1,x0:x1]=True
bgmask=~content&~line
def feats(y,x):
  y=y/H; x=x/W; f=[]
  for i in range(6):
    for j in range(6-i): f.append(x**i*y**j)
  return np.stack(f,-1)
F=feats(yy.ravel().astype(float),xx.ravel().astype(float))
idx=np.flatnonzero(bgmask.ravel())[::11]
bg=np.zeros_like(im)
for c in range(3):
  coef,*_=np.linalg.lstsq(F[idx],im[...,c].ravel()[idx],rcond=None)
  bg[...,c]=(F@coef).reshape(H,W)
print('bg err',np.abs(im-bg)[bgmask].mean())
# grid delta map
nb=np.zeros_like(im)
nb[:,2:-2]=(im[:,:-4]+im[:,4:])/2
nbh=np.zeros_like(im); nbh[2:-2]=(im[:-4]+im[4:])/2
delta=np.where(vl[...,None],im-nb,0)+np.where((hl&~vl)[...,None],im-nbh,0)
lm=line&~content
idx=np.flatnonzero(lm.ravel())[::3]
grid=np.zeros_like(im)
for c in range(3):
  coef,*_=np.linalg.lstsq(F[idx],delta[...,c].ravel()[idx],rcond=None)
  grid[...,c]=np.where(line,(F@coef).reshape(H,W),0)
base=bg+grid
E=im-base
m=np.zeros((H,W),np.uint8)
for y0,y1,x0,x1 in rects_w: m[y0:y1,x0:x1]=255
w=np.asarray(Image.fromarray(m).filter(ImageFilter.GaussianBlur(20))).astype(float)[...,None]/255
sh=np.zeros_like(E); sh[d:]=(E*w)[:-d]
out=im*(1-w)+base*w   # remove content at original place
# where shifted content lands, replace with base+content (avoid doubling grid)
ws=np.zeros_like(w); ws[d:]=w[:-d]
out=out*(1-ws)+base*ws+sh
Image.fromarray(np.clip(out,0,255).round().astype(np.uint8)).save(dst)
