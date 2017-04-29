#!/usr/bin/env python3

from cmath import polar, pi, exp
from colorsys import hsv_to_rgb
from math import sin, cos
from PIL import Image, ImageDraw


def as_col(c):
    (val, phi) = polar(c)
    phi = phi / (2 * pi) % 1
    if val <= 1.0:
        rgb = hsv_to_rgb(phi, 1, val)
    else:
        rgb = hsv_to_rgb(phi, 1 / val, 1)
    return tuple([round(c * 255) for c in rgb])


def f(c, B, C):
#    return c  # id
#    return exp(c.real + c.imag * 3j)  # complex exponentiation, with scaled imaginary part
#    return c * (B + C * 1j)  # complex multiplication
    return c * c + B * c + C  # General quadratic


def plot_into(img, a, b):
    for x in range(W):
        r = (x + OFFSET_X) * SCALE
        for y in range(H):
            i = (y + OFFSET_Y) * SCALE
            c = f(r + i * 1j, a, b)
            img.putpixel((x, y), as_col(c))
    draw = ImageDraw.Draw(img)
    draw_x = a / SCALE - OFFSET_X
    draw_y = b / SCALE - OFFSET_Y
    draw.line((draw_x, 0, draw_x, H), fill=(255, 255, 255))
    draw.line((0, draw_y, W, draw_y), fill=(255, 255, 255))
    del draw

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


def gen_filename(n, total):
    return "img_{:05d}.png".format(n)


def plot_single(n, total):
    assert 0 <= n and n < total, (n, total)
    (a, b) = gen_param(n / total)
    img = Image.new("RGB", (W, H))
    plot_into(img, a, b)
    filename = gen_filename(n, total)
    print("Done with " + filename)
    img.save(filename)


USAGE = """"Usage: {name} {--enumerate | <I> } <N>
<I> is the frame number.
<N> is the total amount of frames.
Examples:
$ {name} 29 30
Plots the last frame into file img_30.
$ {name} 0 30
Plots the first frame into file img_01."""

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 3:
        total = int(argv[2])
        if argv[1] == "--enumerate":
            for n in range(total):
                print(gen_filename(n, total))
        else:
            plot_single(int(argv[1]), total)
    else:
        print(USAGE.format(name=argv[0]))
        exit(1)
