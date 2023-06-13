from vpython import *
from dataclasses import dataclass


SHOW_SLIT = False
DEBUG = False

def DBUG(prompt, end='\n'):
    if DEBUG: print(prompt, end=end)


image_res = .01  # Image Pixel "Length"
IMAGE_P = []
slitN = 2
slitL = 2
SLIT = []
LAMBDA = 1


class image_seg:
    def __init__(self, pos, c, index):
        self.obj = box(color=c, pos=pos, height=10, width=.5, length=image_res)
        self.index = index
        self.illumination = vec(0, 0, 0)
    def set_color(self, gc):
        self.obj.color = vec(gc, gc, gc)

class slit:
    def __init__(self, pos, index):
        self.obj = sphere(radius=.5, pos=pos, color=color.red, visible=SHOW_SLIT)
        self.index = index
