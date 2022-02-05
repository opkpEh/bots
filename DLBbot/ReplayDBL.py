#I mostly used it for Part 6 ( marjin buu ) Part 1 , chapter 8 ( ssj 3 goku one for frinedship levels) and for gettings stuff for that white saibamen to get pizzas  
import pyautogui as pg
import time

#chrono crystal as when you play over and over sometimes your friendship levels up this is to click on that cc
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
