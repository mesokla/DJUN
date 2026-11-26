import sys,glob
from PIL import Image
fs=sys.argv[2:]; W=360; H=640
sh=Image.new('RGB',(W*len(fs),H),'white')
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGB').resize((W,H)); sh.paste(im,(i*W,0))
sh.save(sys.argv[1])
