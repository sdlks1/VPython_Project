from vpython import *
from math import *

dt = 0.01
slit = []
WV = 0

class ray:
    def __init__(self, index, wavelen):
        self.index = index
        self.wavelen = wavelen
    def project(self, l):
        return vec(cos((l/self.wavelen)*2*pi), sin((l/self.wavelen)*2*pi))

def init(slitn):
    slit.clear()
    for i in range(slitn):
        slit.append(tuple((vec(0,0,0), ray(i, WV))))