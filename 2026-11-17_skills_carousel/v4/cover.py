import numpy as np
from PIL import Image, ImageFilter, ImageDraw
ph=Image.open('laptop_photo1.jpg').convert('RGB')
quad=[(142,454),(1017,448),(1019,1001),(146,1006)]  # TL TR BR BL in photo px
sc=Image.open('screen.png').convert('RGB'); sw,sh=sc.size
def coeffs(dst,src):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A+=[[x,y,1,0,0,0,-u*x,-u*y],[0,0,0,x,y,1,-v*x,-v*y]];B+=[u,v]
    return np.linalg.solve(np.array(A,float),np.array(B,float)).tolist()
c=coeffs(quad,[(0,0),(sw,0),(sw,sh),(0,sh)])
warped=sc.transform(ph.size,Image.PERSPECTIVE,c,Image.BICUBIC)
mask=Image.new('L',ph.size,0); ImageDraw.Draw(mask).polygon(quad,fill=255); mask=mask.filter(ImageFilter.GaussianBlur(1.2))
# slight screen glow toning to match photo
warped=Image.blend(warped,Image.new('RGB',ph.size,(20,10,4)),0.12)
out=ph.copy(); out.paste(warped,(0,0),mask)
out=out.crop((95,250,1095,1500)).resize((1080,1350),Image.LANCZOS)
out.save('cover_bg.png')
