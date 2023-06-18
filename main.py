from vpython import *
from render import *
from ui import *
import color


# Debug
SHOW_SLIT = False
CAPTURE = False
DEBUG = False
def DBUG(prompt, end='\n'):
    if DEBUG: print(prompt, end=end)

# Render
scene = canvas(width=772, height=768, center=vec(0,0,0), background=vec(.6,.8,.8), range=15, fov=.001)
IMAGE_RES = .01
renderer = Renderer(2, 1, 380, 10, IMAGE_RES)

# UI
wt_status = Label("Simulation Complete")
scene.append_to_caption("\n\n")

wt_slitN = Label("Slit Count")
slider_slitN = Slider(min=2, max=10, step=1, length=220, bind=event.push_N)
wt_slitN_v = Label(f"{slider_slitN.value()}")
scene.append_to_caption('\n')

wt_slitL = Label("Slit Spacing")
slider_slitL = Slider(min=1, max=10, step=.1, length=220, bind=event.push_L)
wt_slitL_v = Label(f"{slider_slitL.value()}")
scene.append_to_caption("\n")

wt_lambda = Label("Lambda")
slider_lambda = Slider(min=380, max=780, step=1, length=220, bind=event.push_Lambda)
wt_lambda_v = Label(f"{slider_lambda.value()}")
scene.append_to_caption('\n')

wt_distance = Label("Distance")
slider_distance = Slider(min=1e+8, max=1e+9, step=1, length=220, bind=event.push_D)
wt_distance_v = Label(f"{slider_distance.value()}")
scene.append_to_caption('\n\n')

btn_simulate = button(text="Simulate", bind=event.push_Sim)
scene.append_to_caption("\n\n\n")


renderer.render()
while True:
    if len(event.events) != 0:
        key = event.events[0]
        if key == 'N':
            txt = slider_slitN.value()
            wt_slitN_v.modify(txt)
            renderer.attributes['N'] = txt
        elif key == 'L':
            txt = slider_slitL.value()
            wt_slitL_v.modify(txt)
            renderer.attributes['L'] = txt
        elif key == "Lambda":
            txt = slider_lambda.value()
            wt_lambda_v.modify(txt)
            renderer.attributes['Lambda'] = txt
        elif key == 'D':
            txt = slider_distance.value()
            wt_distance_v.modify(txt)
            renderer.attributes['D'] = txt
        elif key == "sim":
            wt_status.modify("Simulating")
            renderer.simulate()
            wt_status.modify("Simulation Complete")
        event.pop()
