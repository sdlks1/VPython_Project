from raycast import *

# Initialize
scene = canvas(width=1024, height=768, center=vec(0,0,0), background=vec(0.6,0.8,0.8), range=15)
print("[{} slits\t{} pixels]\n".format(slitN, int(30/image_res)))

print("Rendering\n")
for i in range(int(-30/image_res*.5), int(30/image_res*.5+1)):
    IMAGE_P.append(image_seg(vec(i*image_res,0,0), vec(0,0,0), i-int(-30/image_res*.5)))  # Normal
    # IMAGE_P.append(image_seg(vec(i*image_res,0,0), vec(.3*i,.59*i,.11*i)))  # Colored Debug
for i in range(slitN):
    SLIT.append(slit( vec( -30 + (60-(slitN-1)*slitL)/2 + slitL*i ,0,10), i ))

for i in SLIT:
    for j in IMAGE_P:
        c = cos( mag( i.obj.pos-j.obj.pos )/LAMBDA * 2 * pi )
        s = sin( mag( i.obj.pos-j.obj.pos )/LAMBDA * 2 * pi )
        j.illumination += vec(c,s,0)
for i in IMAGE_P:
    # print("Set Pixel["+str(i.index)+"] illumination : "+str(mag(i.illumination)))
    DBUG("Pixel["+str(i.index)+"] illumination vector "+str(i.illumination.x), str(i.illumination.y))
    illu = 1 - (mag(i.illumination)/slitN)
    i.set_color(illu)
print("Done Rendering\n")

# t = 0
# while True:
#     rate(1/DT)
#
#     t += DT