from raycast import *
# from ui import *
from math import *


""" Event Setup """
class Event: # 建立event這個class
    def __init__(self): # 物件屬性：是個空空的 list
        self.events = []
    def prompt_slitN(self):
        self.events.append("N")
        # 因為bind不能讀取變數，因此將"讀取狹縫數的函式"寫在 class Event 裡面
    def prompt_slitL(self):
        self.events.append("L")
        # 因為bind不能讀取變數，因此將"讀取狹縫間距的函式"寫在 class Event 裡面
    def prompt_sim(self):
        self.events.append("sim")
        # 因為bind不能讀取變數，因此將"判斷是否模擬的函式"寫在 class Event 裡面

events = Event() # events 是 class Event 的物件


""" Initialize """
is_simulating = False # 布林值，判斷是否正在運行

# Canvas Setup :
#   width=772 是為了讓畫面的左右邊界剛好切齊成像屏幕
#   fov=.001 是拿來模擬平行投影
scene = canvas(width=772, height=768, center=vec(0,0,0), background=vec(0.6, 0.8, 0.8), range=15, fov=0.001)

def init():
    # Imaging Plane Generation :
    #   p0 是最左邊屏幕像素的x座標
    #   p0 + cnt*image_res 計算每個像素的座標
    #   注意，像素中心點都在x軸上，所以y、z都是0
    #   cnt 是計數器
    IMAGE_P.clear()
    p0 = -30 + image_res/2
    for cnt in range(int(60//image_res)):
        IMAGE_P.append(image_seg( vec( p0 + cnt*image_res, 0, 0 ), vec(0,0,0),cnt))

    # Slits Generation
    #   p0 是最左邊狹縫的x座標
    #   p0 + cnt*slitL 計算每個狹縫的座標
    #   cnt是= 是計數器
    SLIT.clear()
    p0 = (1-slitN)*slitL/2
    for cnt in range(slitN):
        SLIT.append(slit( vec(p0 + cnt*slitL, 0, 10), cnt ))


# 最主要的模擬函式
def Simulate():
    assert slitN >= 2, "Slit Count Should be Greater or Equal to 2" # 防呆（單狹縫屬於例外，不討論）

    is_simulating = True

    init()

    # 巢狀迴圈（Nested Loop），分別迭代狹縫以及屏幕像素，使其一一對應
    for i in SLIT:
        for j in IMAGE_P:
            length = mag(i.obj.pos - j.obj.pos) # 成像屏幕像素到狹縫的距離
            # 計算公式
            #   設像素到狹縫的距離為l，光的波長為λ
            #   則可得該光波在第 l/λ 個週期，由狹縫抵達屏幕
            #   又光波在傳遞時，我們所看到的簡諧波動，是「虛數空間中旋轉向量在實部的投影」（可以想像成是三維圓周投影到二維簡諧）
            #   所以這裡可以代入一個單位圓，用三角函數以及週期計算出光波在抵達屏幕時的向量值，也是此投影的「強度向量」
            c = cos((length/LAMBDA) * 2*pi)
            s = sin((length/LAMBDA) * 2*pi)
            #   計算完成後，再將方向向量累加
            j.illumination += vec(c, s, 0)

    for i in IMAGE_P:
        # 取累加後的強度和向量取其長度，得到強度量值。
        # 這時，強度量值會介於0～N(slitN)之間（最大值發生在每個狹縫所發出的光波在抵達屏幕時洽都是波峰，最小值則發生在洽都為波谷時）
        # 所以需要除以N，使強度量值控制在0～1之間（vpython RGB參數吃的是0～1）
        # 這時計算出來的量值恰好明暗相反，所以用1減
        illu = (mag(i.illumination) / slitN)
        # 最後再將像素的RGB值改為 vec(illu, illu, illu)
        # 註：RGB值，當R=G=B，則為灰階色彩（彩度=0  吧）
        i.set_color(illu)
    
    is_simulating = False



""" UI """
wt_slitN = wtext(text="Slit Count")
slider_slitN = slider(min=2, max=10, step=1, length=220, bind=events.prompt_slitN)
wt_slitN_v = wtext(text=f"{slider_slitN.value}")
scene.append_to_caption('\n')

wt_slitL = wtext(text="Slit Spacing")
slider_slitL = slider(min=1, max=10, step=.1, length=220, bind=events.prompt_slitL)
wt_slitL_v = wtext(text=f"{slider_slitL.value}")
scene.append_to_caption('\n')

btn_simulate = button(text="Simulate", bind=events.prompt_sim)


""" Running Program """
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
            Simulate()
        del events.events[0]