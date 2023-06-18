from vpython import *


class Label:
    def __init__(self, txt):
        self.label = wtext(text=txt)
    def modify(self, txt):
        self.label.text = txt

class Slider:
    def __init__(self, min, max, step, length, bind):
        self.slider_ = slider(min=min, max=max, step=step, length=length, bind=bind)
    def value(self):
        return self.slider_.value

class Event:
    def __init__(self):
        self.events = []
    def push_N(self):
        self.events.append('N')
    def push_L(self):
        self.events.append('L')
    def push_Lambda(self):
        self.events.append("Lambda")
    def push_D(self):
        self.events.append('D')
    def push_Sim(self):
        self.events.append("sim")
    def pop(self):
        del self.events[0]

event = Event()




