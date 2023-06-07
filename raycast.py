from vpython import *
from math import *

DT = .01
IMAGE_P = []

class image_seg:
    def __init__(self, pos, c):
        self.obj = box(color=c, pos=pos, height=10, width=.5, length=.5)
        self.gc = 0 # Grayscale Value
    def set_color(self):
        self.obj.color = vec(self.gc, self.gc, self.gc)
    def update(self):
        pass

class ray:
    def __init__(self, pos, v, theta):
        self.obj = sphere(color=vec(1,1,1), pos=pos, size=.25)
        self.obj.v = vec(v*cos(theta), 0, -v*sin(theta))
    def collision(self) -> (bool,int):
        if self.obj.pos.z <= .75:
            # Collided
            return True, -1
        else:
            return False, -1
    def update(self):
        self.obj.pos += self.obj.v*DT
        self.collision()