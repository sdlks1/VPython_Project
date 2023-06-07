from raycast import *

# Initialize
scene = canvas(width=1024, height=768, center=vec(0,0,0), background=vec(0.6,0.8,0.8), range=15)

for i in range(-30, 31):
    IMAGE_P.append(image_seg(vec(i*.5,0,0), vec(0,0,0)))

t = 0
while True:
    rate(1/DT)

    t += DT