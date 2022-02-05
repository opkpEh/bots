import pyautogui as pg
import time

YesX1= 1746
YesY1= 791
R1= 219
G1= 145
B1= 34


YesX2= 1750
YesY2= 539
R2= 229
G2= 171
B2= 28

tapButtonX1= 1840
tapButtonY1= 802
tapButtonRGB1= 255

while True:

        #to click off any anomlie
        pg.click(x=1652,y=791)


        #tap button
        if pg.pixel(tapButtonX1,tapButtonY1)[0]== tapButtonRGB1:
                if pg.pixel (tapButtonX1,tapButtonY1)[1]== tapButtonRGB1:
                        if pg.pixel(tapButtonX1,tapButtonY1) [2]== tapButtonRGB1:
                                 pg.click(x=tapButtonX1,y=tapButtonY1)
        time.sleep(1)

        if pg.pixel(YesX1,YesY1)[0]== R1:
                if pg.pixel (YesX1,YesY1)[1]== G1:
                        if pg.pixel(YesX1,YesY1) [2]== B1:
                                 pg.click(x=YesX1,y=YesY1)

        time.sleep(0.4)

        if pg.pixel (YesX2,YesY2)[0]== R2:
                if pg.pixel (YesX2,YesY2)[1]== G2:
                        if pg.pixel (YesX2,YesY2) [2]== B2:
                                pg.click(x=YesX2,y=YesY2)
	

