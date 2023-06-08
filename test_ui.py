"""
To do list:
1. Slits number button
3. Slits distance button
"""
from vpython import *

angle_v = 0.01
pos, axis = vec(0, 0, 0), vec(0, 1, 0)

col = color.cyan
welcome = text(text="Hello World",align="center", color=col)
scene = canvas(width=1000, height=600, center=vec(0,0,0),background=vec(0.6,0.8,0.8)) #設定畫面

spinning = False

def SPIN(word):
    global spinning
    spinning = not spinning
    if spinning: word.text = "Stop"
    else: word.text = "Spin"

spin_button = button(text="Spin", pos=scene.title_anchor, bind=SPIN)

def cc(c):
    global col
    if col.equals(color.cyan): # change to magenta:
        col = color.magenta
        welcome.color = color.magenta
        print(welcome.color, color.cyan)
        cbutton.text = "<b>Cyan</b>"
        cbutton.color = color.cyan
        cbutton.background = color.magenta
    else:                      # change to cyan
        col = welcome.color = color.cyan
        cbutton.text = "<b>Magenta</b>"
        cbutton.color = color.magenta
        cbutton.background = color.cyan
        
cbutton = button(text='<b>Magenta</b>', color=color.magenta, background=color.cyan, pos=scene.title_anchor, bind=cc, name=None)

while True:
    rate(100)
    if spinning: welcome.rotate(angle=angle_v, axis=axis)

    


