from vpython import *
from color import *


class Pixel:
    def __init__(self, pos, image_res):
        self.pixel = box(color=color.black, pos=pos, height=10, width=.5, length=image_res)
        self.illumination = vec(0, 0, 0)
    def set_color(self, cl):
        self.pixel.color = vec(cl, cl, cl)
class Slit:
    def __init__(self, pos):
        self.slit = sphere(radius=.5, pos=pos, color=color.red, visible=False)

class Renderer:  # Calculations are included in the renderer.
    def __init__(self, slitN, slitL, lambda_, distance, image_res):
        self.attributes = {
            'N':slitN,
            'L':slitL,
            "Lambda":lambda_,
            "D":distance
        }
        self.image_res = image_res
        self.pixels = []
        self.slits = []
    def modify(self, attr, value):
        self.attributes[attr] = value
    def change_distance(self):
        for slit in self.slits:
            slit.slit.pos.z = self.attributes['D']
    def render(self):  # Canvas Initial
        self.pixels.clear()
        p0 = -30 + self.image_res / 2
        for cnt in range(int(60 // self.image_res)):
            self.pixels.append(Pixel(vec(p0 + cnt * self.image_res, 0, 0), self.image_res))

        self.slits.clear()
        p0 = (1 - self.attributes['N']) * self.attributes['L'] / 2
        for cnt in range(self.attributes['N']):
            self.slits.append(Slit(vec(p0 + cnt * self.attributes['L'], 0, self.attributes['D'])))
    def simulate(self):
        self.render()

        for slit in self.slits:
            for pixel in self.pixels:
                length = mag(slit.slit.pos - pixel.pixel.pos)
                c = cos((length / self.attributes["Lambda"]) * 2 * pi)
                s = sin((length / self.attributes["Lambda"]) * 2 * pi)
                pixel.illumination += vec(c, s, 0)

        for pixel in self.pixels:
            illumination = mag(pixel.illumination) / self.attributes['N']
            pixel.set_color(illumination)
