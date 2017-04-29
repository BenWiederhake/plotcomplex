#!/usr/bin/env python3

from PIL import Image
from cmath import polar, pi
from colorsys import hsv_to_rgb


def as_col(c):
    (val, phi) = polar(c)
    phi = phi / (2 * pi) % 1
    if val <= 1.0:
        rgb = hsv_to_rgb(phi, 1, val)
    else:
        rgb = hsv_to_rgb(phi, 1 / val, 1)
    return tuple([round(c * 255) for c in rgb])



def f(c):
    # Identity
    return c


W = 640
H = 480
SCALE = 1 / 200
OFFSET_X = -W / 2
OFFSET_Y = -H / 2

if __name__ == '__main__':
    img = Image.new("RGB", (W, H))
    for x in range(W):
        r = (x + OFFSET_X) * SCALE
        for y in range(H):
            i = (y + OFFSET_Y) * SCALE
            c = f(r + i * 1j)
            img.putpixel((x, y), as_col(c))
    img.show()
    img.save("myimg.png")
