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
slider_slitL = Slider(min=1, max=1000, step=1, length=220, bind=event.push_L)
scene.append_to_caption('\t')
input_slitL = winput(bind=event.push_L_input)
wt_slitL_v = Label("倍波長")
scene.append_to_caption('\n')

wt_lambda = Label("Lambda")
slider_lambda = Slider(min=380, max=780, step=1, length=220, bind=event.push_Lambda)
wt_lambda_v = Label(f"{slider_lambda.value()} (nm)")
scene.append_to_caption('\n')

wt_distance = Label("Distance")
slider_distance = Slider(min=1, max=1000, step=1, length=220, bind=event.push_D)
scene.append_to_caption('\t')
input_distance = winput(bind=event.push_D_input)
# input_distance = winput(bind=db)
wt_distance_v = Label("倍波長")
scene.append_to_caption('\n\n')

btn_simulate = button(text="Simulate", bind=event.push_Sim)
scene.append_to_caption("\n\n\n")

wt_events = Label(f"{event.buffer}")


renderer.render()
while True:
    wt_events.modify(f"{event.buffer}")
    if len(event.events) != 0:
        key = event.events[0]
        if key == 'N':
            txt = slider_slitN.value()
            wt_slitN_v.modify(txt)
            renderer.attributes['N'] = txt
        elif key == 'L':
            txt = slider_slitL.value()
            input_slitL.text = txt
            renderer.attributes['L'] = txt * renderer.attributes["Lambda"]
        elif key == "L in":
            slider_slitL.modify(int(input_slitL.text))
            renderer.attributes['L'] = int(input_slitL.text)
        elif key == "Lambda":
            txt = slider_lambda.value()
            v = (txt-380) * (9/400) + 1
            wt_lambda_v.modify(f"{txt} (nm)")
            renderer.attributes['Lambda'] = v * renderer.attributes["Lambda"]
        elif key == 'D':
            txt = slider_distance.value()
            input_distance.text = txt
            renderer.attributes['D'] = txt * renderer.attributes["Lambda"]
        elif key == "D in":
            slider_distance.modify(int(input_distance.text))
            renderer.attributes['D'] = int(input_distance.text) * renderer.attributes["Lambda"]
        elif key == "sim":
            wt_status.modify("Simulating")
            renderer.simulate()
            wt_status.modify("Simulation Complete")
        event.pop()
