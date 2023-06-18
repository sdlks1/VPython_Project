import sys
import os
import traceback
import optparse
import time
import logging
from vpython import *


def wavelength_to_rgb(wave, gamma=0.8):
    intensity_max = 1

    if wave < 380:
        red, green, blue = 0, 0, 0
    elif wave < 440:
        red = -(wave - 440) / (440 - 380)
        green, blue = 0, 1
    elif wave < 490:
        red = 0
        green = (wave - 440) / (490 - 440)
        blue = 1
    elif wave < 510:
        red, green = 0, 1
        blue = -(wave - 510) / (510 - 490)
    elif wave < 580:
        red = (wave - 510) / (580 - 510)
        green, blue = 1, 0
    elif wave < 645:
        red = 1
        green = -(wave - 645) / (645 - 580)
        blue = 0
    elif wave <= 780:
        red, green, blue = 1, 0, 0
    else:
        red, green, blue = 0, 0, 0

    # let the intensity fall of near the vision limits
    if wave < 380:
        factor = 0
    elif wave < 420:
        factor = 0.3 + 0.7 * (wave - 380) / (420 - 380)
    elif wave < 700:
        factor = 1
    elif wave <= 780:
        factor = 0.3 + 0.7 * (780 - wave) / (780 - 700)
    else:
        factor = 0

    def f(c):
        if c == 0:
            return 0
        else:
            return intensity_max * pow(c * factor, gamma)

    return f(red), f(green), f(blue)

# scene = canvas(width=772, height=768, center=vec(0,0,0), background=vec(.6,.8,.8), range=15, fov=.001)
#
# Box = box(color=color.red, pos=vec(0,0,0))
# Box2 = box(color=color.red, pos=vec(10,0,0))
#
# wv = 380
#
# evt = []
# def push_evt():
#     evt.append("modify")
#
# S = slider(min=380, max=780, step=1, bind=push_evt)
# L = wtext(text="380")
# L2 = wtext(text="( , , )")
#
# while True:
#     if len(evt) != 0:
#         L.text = str(S.value)
#         wv = S.value
#         RGB = wavelength_to_rgb(wv)
#         L2.text = f"({RGB[0]},{RGB[1]},{RGB[2]})"
#         Box.color = vec(RGB[0], RGB[1], RGB[2])
#         Box2.color = vec(RGB[0]/2, RGB[1]/2, RGB[2]/2)
#         del evt[0]