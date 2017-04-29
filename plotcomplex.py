#!/usr/bin/env python3

from cmath import polar, pi
from colorsys import hsv_to_rgb
from math import sin, cos
from PIL import Image


def as_col(c):
    (val, phi) = polar(c)
    phi = phi / (2 * pi) % 1
    if val <= 1.0:
        rgb = hsv_to_rgb(phi, 1, val)
    else:
        rgb = hsv_to_rgb(phi, 1 / val, 1)
    return tuple([round(c * 255) for c in rgb])


def f(c, B, C):
    return c * c + B * c + C


def plot_into(img, a, b):
    for x in range(W):
        r = (x + OFFSET_X) * SCALE
        for y in range(H):
            i = (y + OFFSET_Y) * SCALE
            c = f(r + i * 1j, a, b)
            img.putpixel((x, y), as_col(c))

def gen_param(t):
    r = (1 - cos(t * 2 * pi)) * 0.6
    phi = t * 2 * pi * 3
    x = +r * sin(phi)
    y = -r * cos(phi)
    return (x, y)


W = 640
H = 480
SCALE = 1 / 150
OFFSET_X = -W / 2
OFFSET_Y = -H / 2
T_MAX = 50
PARAMS = list([gen_param(t / T_MAX) for t in range(T_MAX)])


def plot_all():
    img = Image.new("RGB", (W, H))
    for (n, (a, b)) in enumerate(PARAMS):
        plot_into(img, a, b)
        #img.show()
        filename = "myimg_{:02d}_{:+5.3f}_{:+5.3f}.png".format(n, a, b)
        print("Done with " + filename)
        img.save(filename)


if __name__ == '__main__':
    plot_all()
