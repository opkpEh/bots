#Hello, do read the comments ( the lines with #)

#piano tiles webiste that i used to play ( in full screen, on a 1080 by 1920 screen ig )
#https://www.pianotiles.org/

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Enter the location a single pixle from each tile
#to get the location of each pixles, use pyautogui
#pyautogui.displayMousePosition()
#press ctrl + c to stop the stop ( first open something else than piano tiles by alt+tab)
X1= 756
Y1= 676
X2= 880
Y2= 673
X3= 1011
Y3= 666
X4= 1132
Y4= 673

#color of black
color= 17
#mentioned besides the location from pyautogui

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(4)

while True:
    
    if pyautogui.pixel(X1, Y1)[0] == color:
                click(X1, Y1)
                #time.sleep(0.1)
                #uncomment these if the bot is going too fast
                #this command ( time.sleep() ) stops the bot for given amount of seconds
        
    if pyautogui.pixel(X2, Y2)[0] == color:
                click(X2, Y2)
                #time.sleep(0.1)
        
    if pyautogui.pixel(X3, Y3)[0] == color:
                click(X3, Y3)
                #time.sleep(0.1)
        
    if pyautogui.pixel(X4, Y4)[0] == color:
                click(X4, Y4)
                #time.sleep(0.1)

    #if you really need help contact me at : harshpandeykp20@gmail.com
