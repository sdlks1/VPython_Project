from vpython import *
from dataclasses import dataclass
import Constants_
from event import event


class Label:
    def __init__(self, txt):
        self.label = wtext(text=txt)
    def modify(self, txt):
        self.label.text = txt


""" UI Declaration """
wt_status = Label("Simulation Complete")
scene.append_to_caption("\n\n")

wt_slitN = Label("Slit Count")
slider_slitN = slider(min=2, max=10, step=1, length=220, bind=lambda i='N':event.push(i))
wt_slitN_v = Label(f"{slider_slitN.value}")
scene.append_to_caption('\n')

wt_slitL = Label("Slit Spacing")
slider_slitL = slider(min=1, max=10, step=.1, length=220, bind=lambda i='L':event.push(i))
wt_slitL_v = Label(f"{slider_slitL.value}")
scene.append_to_caption("\n\n")

btn_simulate = button(text="Simulate", bind=lambda i="sim":event.push(i))
scene.append_to_caption("\n\n\n")
