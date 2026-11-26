"""Cut collage elements out of old Djun posts (flat backgrounds) by keying the background colour."""
import numpy as np
from PIL import Image
from scipy import ndimage
SRC = '/tmp/claude-0/-home-user-DJUN/6ab990f8-5082-5cf5-9cbe-35b07b2afc34/images/'
def keyed(a, kind):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    if kind == 'green':          # dark teal background: key on chroma, so neutral greys/blacks survive
        score = np.minimum(g - r - 18, b - r - 14) / 14
        dark = np.clip((95 - (r + g + b) / 3) / 20, 0, 1)
        return 1 - np.clip(score, 0, 1) * dark
    d = np.sqrt(((a - np.array((239, 232, 223))) ** 2).sum(2))
    return np.clip((d - 14) / 22, 0, 1)
def cut(src, box, kind, out, holes=(), kill_ochre=False):
    im = Image.open(SRC + src).convert('RGB')
    a = np.asarray(im).astype(float)
    alpha = keyed(a, kind)
    for (x0, y0, x1, y1) in holes: alpha[y0:y1, x0:x1] = 0
    if kill_ochre:               # drop golden collage leaves (keep the grey figure)
        r, g, b = a[..., 0], a[..., 1], a[..., 2]
        sat = (np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b))
        alpha[(r > g + 8) & (g > b + 4) & (sat > 28)] = 0
    x0, y0, x1, y1 = box; a = a[y0:y1, x0:x1]; alpha = alpha[y0:y1, x0:x1]
    lab, n = ndimage.label(alpha > 0.5)
    if n:
        sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
        keep = [i + 1 for i, s in enumerate(sizes) if s > 0.05 * sizes.max()]
        alpha = alpha * ndimage.binary_dilation(np.isin(lab, keep), iterations=2)
    img = Image.fromarray(np.dstack([a, alpha * 255]).astype(np.uint8), 'RGBA')
    img = img.crop(img.getbbox()); img.save(out); print(out, img.size)
cut('16.webp', (330, 380, 900, 1282), 'green', 'assets/cutouts/tiger.png', holes=[(672, 300, 1200, 560), (870, 300, 1200, 930), (650, 1080, 1000, 1282)], kill_ochre=True)
cut('17.webp', (1505, 60, 1985, 555), 'beige', 'assets/cutouts/bulb_man.png')
cut('19.webp', (1150, 770, 1480, 1300), 'beige', 'assets/cutouts/monitor_kid.png')
cut('19.webp', (562, 185, 1080, 706), 'green', 'assets/cutouts/newspaper.png')
cut('17.webp', (120, 120, 495, 600), 'green', 'assets/cutouts/typewriter.png')
