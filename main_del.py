from raycast import *
from math import *
from ui import *


""" Globals """
slitN = 2
slitL = 1
LAMBDA = 1


if __name__ == "__main__":
    while True:
        # wt_slitN_v.text = f"{slider_slitN.value}"
        # wt_slitL_v.text = f"{slider_slitL.value}"
        if len(events.events) != 0:
            event = events.events[0]
            if event == "N":
                slitN = wt_slitN_v.text = slider_slitN.value
            elif event == "L":
                slitL = wt_slitL_v.text = slider_slitL.value
            elif event == "sim" and not is_simulating:
                wt_status.text = "Simulating"
                Simulate()
                wt_status.text = "Simulation Complete"
            del events.events[0]