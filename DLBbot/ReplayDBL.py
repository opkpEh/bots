import pyautogui as pg
import time

ccX= 1658
ccY= 576
ccR= 0
ccG= 159
ccB= 162

OkSideX= 1749
OkSideY= 777
OkSideR= 229
OkSideG= 171
OkSideB= 28

StartBattleX= 1765
StartBattleY= 734
StartBattleR= 219
StartBattleG= 145
StartBattleB= 34

RematchX= 1567
RematchY= 798
RematchR= 173
RematchG= 173
RematchB= 156

YesX= 1747
YesY= 557
YesR= 219
YesG= 145
YesB= 34


while True:
    pg.click(ccX,ccY)
    if pg.pixel(ccX,ccY)[0]== ccR:
        if pg.pixel(ccX,ccY)[1]== ccG:
            if pg.pixel(ccX,ccY)[2]== ccB:
                pg.click(ccX,ccY)

    if pg.pixel(RematchX,RematchY)[0]== RematchR:
        if pg.pixel(RematchX,RematchY)[1]== RematchG:
            if pg.pixel(RematchX,RematchY)[2]== RematchB:
                pg.click(RematchX,RematchY)

    if pg.pixel(YesX,YesY)[0]==  YesR:
        if pg.pixel(YesX,YesY)[1]== YesG:
            if pg.pixel(YesX,YesY)[2]== YesB:
                pg.click(YesX,YesY)


    time.sleep(4)
    



    
    
