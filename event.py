from vpython import *
from dataclasses import dataclass
from Constants_ import *
import ui
import render


global slitN, slitL


class Event:
    def __init__(self):
        self.events = []
        self.keys = {
            'N': lambda: (globals().update(slitN=ui.slider_slitN.value), ui.wt_slitN_v.modify(ui.slider_slitN.value)),
            'L': lambda: (globals().update(slitN=ui.slider_slitL.value), ui.wt_slitL_v.modify(ui.slider_slitL.value)),
            "sim": render.renderer.simulate
        }
    def push(self, key):
        self.events.append(key)
    def pop(self):
        del self.events[0]
    def update(self):
        key = self.events[0]
        self.keys[key]()
        self.pop()

event = Event()
