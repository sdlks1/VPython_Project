from vpython import *


# Canvas Setup :
#   width=772 是為了讓畫面的左右邊界剛好切齊成像屏幕
#   fov=.001 是拿來模擬平行投影
scene = canvas(width=772, height=768, center=vec(0,0,0), background=vec(0.6, 0.8, 0.8), range=15, fov=0.001)


""" Globals """
slitN = 2
slitL = 1
LAMBDA = 1


""" Event Setup """
class Event:
    def __init__(self):
        global slitN, slitL

        self.events = []
        self.key = {
            'N': lambda: (
                globals().update(slitN=slider_slitN.value),
                wt_slitN_v.text := 
            )
        }
    def push(self, item):
        self.events.append(item)
    def pop(self):
        del self.events[0]
    # def update(self):
    #     key = self.events[0]
    #     if

events = Event()

""" UI """
wt_status = wtext(text="Simulation Complete")
scene.append_to_caption("\n\n")

wt_slitN = wtext(text="Slit Count")
slider_slitN = slider(min=2, max=10, step=1, length=220, bind=lambda i='N':events.push(i))
wt_slitN_v = wtext(text=f"{slider_slitN.value}")
scene.append_to_caption('\n')

wt_slitL = wtext(text="Slit Spacing")
slider_slitL = slider(min=1, max=10, step=.1, length=220, bind=lambda i='L':events.push(i))
wt_slitL_v = wtext(text=f"{slider_slitL.value}")
scene.append_to_caption("\n\n")

btn_simulate = button(text="Simulate", bind=lambda i="sim":events.push(i))
scene.append_to_caption("\n\n\n")