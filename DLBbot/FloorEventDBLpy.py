import pyautogui as pg
import time

X1= 1746
Y1= 791
R1= 223
G1= 141
B1= 37


X2= 1750
Y2= 539
R2= 229
G2= 171
B2= 28

tapButtonX1= 1840
tapButtonY1= 802
tapButtonRGB1= 255

while True:

#tap button
        if pg.pixel(tapButtonX1,tapButtonY1)[0]== tapButtonRGB1:
                if pg.pixel (tapButtonX1,tapButtonY1)[1]== tapButtonRGB1:
                        if pg.pixel(tapButtonX1,tapButtonY1) [2]== tapButtonRGB1:
                                 pg.click(x=tapButtonX1,y=tapButtonY1)
        time.sleep(1)

        if pg.pixel(X1,Y1)[0]== R1:
                if pg.pixel (X1,Y1)[1]== G1:
                        if pg.pixel(X1,Y1) [2]== B1:
                                 pg.click(x=X1,y=Y1)

        time.sleep(0.4)

        if pg.pixel (X2,Y2)[0]== R2:
                if pg.pixel (X2,Y2)[1]== G2:
                        if pg.pixel (X2,Y2) [2]== B2:
                                pg.click(x=X2,y=Y2)
	

