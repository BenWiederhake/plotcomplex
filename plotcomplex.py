#!/usr/bin/env python3

from PIL import Image
from math import atan2, floor, pi
from colorsys import hsv_to_rgb


def as_col(r, i):
    val = r * r + i * i
    phi = atan2(i, r) / (2 * pi) % 1
    assert phi >= -0.0001, phi
    assert phi <= 1.0001, phi
    if val <= 1.0:
        rgb = hsv_to_rgb(phi, 1, (2 - val) * val)
    else:
        rgb = hsv_to_rgb(phi, 1 / val, 1)
    return tuple([round(c * 255) for c in rgb])


def f(r, i):
    # Identity
    return (r, i)


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
            (r, i) = f(r, i)
            img.putpixel((x, y), as_col(r, i))
    img.show()
    img.save("myimg.png")
