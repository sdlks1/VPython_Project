from raycast import *

# Initialize
for i in range(-30, 31):
    IMAGE_P.append(box(color=vec(0.6,0.6,0.6)))

t = 0
while True:
    rate(1/DT)

    t += DT