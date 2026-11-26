"""Split a sticker sheet (objects on a flat light background) into separate transparent PNGs.
Background = light pixels connected to the image border, so white areas inside an object survive."""
import sys, numpy as np
from PIL import Image
from scipy import ndimage
src, prefix, thr = sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 28
im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(float)
h, w, _ = a.shape
corners = np.array([a[2, 2], a[2, w-3], a[h-3, 2], a[h-3, w-3]]); bg = corners[corners.sum(1).argmax()]  # brightest corner: objects may touch the edge
near = np.sqrt(((a - bg) ** 2).sum(2)) < thr
lab, n = ndimage.label(near)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
bgmask = np.isin(lab, list(border))
fg = ~bgmask
fg = ndimage.binary_opening(fg, iterations=1)
objs, m = ndimage.label(ndimage.binary_dilation(fg, iterations=4))
k = 0
for i, sl in enumerate(ndimage.find_objects(objs)):
    ys, xs = sl
    if (ys.stop - ys.start) * (xs.stop - xs.start) < 0.004 * h * w: continue
    region = (objs[sl] == i + 1) & fg[sl]
    alpha = ndimage.gaussian_filter(region.astype(float), 0.7)
    rgba = np.dstack([a[sl], np.clip(alpha, 0, 1) * 255]).astype(np.uint8)
    Image.fromarray(rgba, 'RGBA').save(f'{prefix}_{k:02d}.png'); k += 1
print(src, '->', k, 'pieces')
