from vpython import *
from math import *

DT = .01
IMAGE_P = []

class image_seg:
    def __init__(self):
        self.obj = box()
        self.gc = 0 # Grayscale Value
    def set_color(self):
        pass
    def update(self):
        self.obj = box()