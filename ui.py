from vpython import *

# winput N & L
def set_N():
    print
wi_N = winput(bind=set_N)

def set_L():
    pass
wi_L = winput(bind=set_L)

# Simulate button
btndown = False
def simulating():
    global btndown
    if _____:
        btndown = True
    else:
        btndown = False
sim_btn = button(text="Simulate", )

# Is Simulating

def evt(func):
    if btndown:
        func(N,L)