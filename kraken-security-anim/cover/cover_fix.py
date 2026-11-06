import sys, numpy as np
from PIL import Image, ImageFilter
src,dst=sys.argv[1],sys.argv[2]
im=np.asarray(Image.open(src).convert('RGB')).astype(float)
H,W,_=im.shape
yy,xx=np.mgrid[0:H,0:W]
rects=[(200,545,80,980),(600,1230,200,900),(1220,1345,110,970)]
mask=np.ones((H,W),bool)
for y0,y1,x0,x1 in rects: mask[max(0,y0-80):y1+80,max(0,x0-80):x1+80]=False
ys=yy[mask][::17]; xs=xx[mask][::17]
def feats(y,x):
  y=y/H; x=x/W
  return np.stack([np.ones_like(x),x,y,x*x,x*y,y*y,x**3,x*x*y,x*y*y,y**3,x**4,y**4,x*x*y*y,x**3*y,x*y**3],-1)
A=feats(ys.astype(float),xs.astype(float)); F=feats(yy.ravel().astype(float),xx.ravel().astype(float))
bg=np.zeros_like(im)
for c in range(3):
  coef,*_=np.linalg.lstsq(A,im[...,c][mask][::17],rcond=None)
  bg[...,c]=(F@coef).reshape(H,W)
m=np.zeros((H,W),np.uint8)
for y0,y1,x0,x1 in rects: m[max(0,y0-55):y1+55,max(0,x0-55):min(W,x1+55)]=255
w=np.asarray(Image.fromarray(m).filter(ImageFilter.GaussianBlur(18))).astype(float)[...,None]/255
D=im-bg; d=140
clean=im*(1-w)+bg*w
sh=np.zeros_like(D); sh[d:]=(D*w)[:-d]
Image.fromarray(np.clip(clean+sh,0,255).round().astype(np.uint8)).save(dst)
