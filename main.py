from raycast import *
from ui import *
from math import *

""" Initialize """
# Canvas Setup
scene = canvas(width=772, height=768, center=vec(0, 0, 0), background=vec(0.6, 0.8, 0.8), range=15, fov=.001)


# Imaging Plane Generation
p0 = -30 + image_res/2
for cnt in range(int(60//image_res)):
    IMAGE_P.append(image_seg( vec(p0 + cnt*image_res,0,0), vec(0,0,0), cnt ))

# Slits Generation
p0 = (1-slitN)*slitL/2
for cnt in range(slitN):
    SLIT.append(slit( vec(p0 + cnt*slitL, 0, 10), cnt ))


def Simulate():
    assert slitN >= 2
    for i in SLIT:
        for j in IMAGE_P:
            length = mag(i.obj.pos - j.obj.pos)
            c = cos((length/LAMBDA) * 2*pi)
            s = sin((length/LAMBDA) * 2*pi)
            j.illumination += vec(c, s, 0)

    for i in IMAGE_P:
        if slitN == 1:
            i.set_color(i.illumination.y)
        else:
            illu = 1 - (mag(i.illumination) / slitN)
            i.set_color(illu)

Simulate()
# simulate = Simulate
#
#
# while True:
#     evt(Simulate)