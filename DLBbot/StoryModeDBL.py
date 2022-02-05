# Hello, Change variables according to your screen
# I used bluestacks kept on top right edge to edge
# 1080 by 1920 resolution of my screen ( I had night light on, OS: windows 10)
import keyboard
import pyautogui as pg
import time

#This clicks on the tab that starts the chapter (Eg Part 1, Book 2,chapter 3)
pg.click(1643,369)
time.sleep(4)

demoX= 1715
demoY= 696
demoR=62
demoG=33
demoB=16

StartBattleX= 1765
StartBattleY= 734
StartBattleR= 176
StartBattleG= 117
StartBattleB= 32

FirstslotAdvX = 1538
FirstslotAdvY= 481
FirstslotX= 1561
FirstslotY= 578

SecondslotAdvX= 1635
SecondslotAdvY= 482
SecondslotX= 1656, 525

ThirdslotAdvX= 1732
ThirdslotAdvY= 481
ThirdslotX= 1758
ThirdslotY= 519

FourthslotAdvX= 1538
FourthslotAdvY= 571
FourthslotX= 1559
FourthslotY= 606
FourthsClickCheckX= 1601
FourthsClickCheckY= 594
FourthsClickCheckR= 255
FourthsClickCheckG= 142


FifthslotAdvX= 1635
FifthslotAdvY= 571
FifthslotX= 1666
FifthslotY= 606
FifthsClickCheckX= 1694
FifthsClickCheckY= 594

SixthsAdvX= 1732
SixthsAdvY= 569
SixthslotX= 1756
SixthslotY=606
SixthsClickCheckX= 606
SixthsClickCheckY= 594

SelectedInTeamColorR= 255
SelectedInTeamColorG= 142
SelectedInTeamColorB= 0

ReadyX= 1654
ReadyY= 800
ReadyR= 219
ReadyG= 145
ReadyB= 34

SkipX=1824
SkipY=62
SkipR= 0
SkipG= 70
SkipB= 95

FriendshiplevelX= 1655
FriendshiplevelY= 577
FriendshiplevelR= 0
FriendshiplevelG= 178
FriendshiplevelB= 180

OkMidX= 1654
OkMidY= 778
OkMidR= 229
OkMidG= 171
OkMidB= 28

OkSideX= 1749
OkSideY= 777
OkSideR= 229
OkSideG= 171
OkSideB= 28

YesX= 1747
YesY= 557
YesR= 219
YesG= 145
YesB= 34

while keyboard.read_key() != 'space':
    #click off demo
    if pg.pixel(demoX,demoY)[0]== demoR:
        if pg.pixel(demoX,demoY)[1]== demoG:
            if pg.pixel(demoX,demoY)[2]== demoB:
                pg.click(demoX,demoY)

    time.sleep(1)

     #click on start battle
    if pg.pixel(StartBattleX,StartBattleY)[0]== StartBattleR:
        if pg.pixel(StartBattleX,StartBattleY)[1]== StartBattleG:
            if pg.pixel(StartBattleX,StartBattleY)[2]== StartBattleB:
                pg.click(StartBattleX,StartBattleY)

    time.sleep(4)
    
    #selecting character
    #1
    if pg.pixel(FirstslotAdvX,FirstslotAdvY)[0]== 0:
        if pg.pixel(FirstslotAdvX,FirstslotAdvY)[1]== 145:
            pg.click(FirstslotX,FirstslotY)
            time.sleep(1)
    #2
    if pg.pixel(SecondslotAdvX,SecondslotAdvY)[0]== 0:
        if pg.pixel(SecondslotAdvX,SecondslotAdvY)[1]== 145:
            pg.click(SecondslotX,SecondslotY)
            time.sleep(1)

    #3        
    if pg.pixel(ThirdslotAdvX,ThirdslotAdvY)[0]== 0:
        if pg.pixel(ThirdslotAdvX,ThirdslotAdvY)[1]== 145:
            pg.click(ThirdslotX,ThirdslotY)
            time.sleep(1)

    #4       
    if pg.pixel(FourthslotAdvX,FourthslotAdvY)[0]== 0:
        if pg.pixel(FourthslotAdvX,FourthslotAdvY)[1]== 145:
            pg.click(FourthslotX,FourthslotY)
            time.sleep(1)

    #5        
    if pg.pixel(FifthslotAdvX,FifthslotAdvY)[0]== 0:
        if pg.pixel(FifthslotAdvX,FifthslotAdvY)[1]== 145:
            pg.click(FifthslotX,FifthslotY)
            time.sleep(1)

    #6
    if pg.pixel(SixthsAdvX,SixthsAdvY)[0]== 0:
        if pg.pixel(SixthsAdvX,SixthsAdvY)[1]== 145:
            pg.click(SixthslotX,SixthslotY)
            time.sleep(1)

    #failsafe to get atleast one team out for battle
    if pg.pixel(FourthsClickCheckX,FourthsClickCheckY)[0]!=  SelectedInTeamColorR:
        if pg.pixel(FourthsClickCheckX,FourthsClickCheckY)[1]!= SelectedInTeamColorG:
            if pg.pixel(FourthsClickCheckX,FourthsClickCheckY)[2]!= SelectedInTeamColorB:
                pg.click(FourthslotX,FourthslotY)
                time.sleep(1)

    if pg.pixel(FifthsClickCheckX,FifthsClickCheckY)[0] !=  SelectedInTeamColorR:
        if pg.pixel(FifthsClickCheckX,FifthsClickCheckY)[1] != SelectedInTeamColorG:
            if pg.pixel(FifthsClickCheckX,FifthsClickCheckY)[2] != SelectedInTeamColorB:
                pg.click(FifthslotX,FifthslotY)
                time.sleep(1)

    if pg.pixel(SixthsClickCheckX,SixthsClickCheckY)[0] !=  SelectedInTeamColorR:
        if pg.pixel(SixthsClickCheckX,SixthsClickCheckX)[1] != SelectedInTeamColorG:
            if pg.pixel(SixthsClickCheckX,SixthsClickCheckX)[2] != SelectedInTeamColorB:
                pg.click(SixthslotX,SixthslotY)
                time.sleep(1)

    time.sleep(2)
    
    #clicking on ready button
    if pg.pixel(ReadyX,ReadyY)[0]==  ReadyR:
        if pg.pixel(ReadyX,ReadyY)[1]== ReadyG:
            if pg.pixel(ReadyX,ReadyY)[2]== ReadyB:
                pg.click(ReadyX,ReadyY)

    time.sleep(10)
    
    #checking for skip story button
    if pg.pixel(SkipX,SkipY)[0]==  SkipR:
        if pg.pixel(SkipX,SkipY)[1]== SkipG:
            if pg.pixel(SkipX,SkipY)[2]== SkipB:
                pg.click(SkipX,SkipY)
        
    #waiting for battle for atleast 20 
    time.sleep(20)

    #checking for skip story button
    if pg.pixel(SkipX,SkipY)[0]==  SkipR:
        if pg.pixel(SkipX,SkipY)[1]== SkipG:
            if pg.pixel(SkipX,SkipY)[2]== SkipB:
                pg.click(SkipX,SkipY)
                time.sleep(8)
                

    #checking for friendship levelup thinge
    if pg.pixel(FriendshiplevelX,FriendshiplevelY)[0]==  FriendshiplevelR:
        if pg.pixel(FriendshiplevelX,FriendshiplevelY)[1]== FriendshiplevelG:
            if pg.pixel(FriendshiplevelX,FriendshiplevelY)[2]== FriendshiplevelB:
                pg.click(FriendshiplevelX,FriendshiplevelY)
                time.sleep(1)

    #clicking on the screen once for any anomalie
    pg.click(1600,600)

    #clicking on ok
    if pg.pixel(OkMidX,OkMidY)[0]==  OkMidR:
        if pg.pixel(OkMidX,OkMidY)[1]== OkMidG:
            if pg.pixel(OkMidX,OkMidY)[2]== OkMidB:
                pg.click(OkMidX,OkMidY)
                time.sleep(1)
    
    #again clicking on ok
    if pg.pixel(OkSideX,OkSideY)[0]==  OkSideR:
        if pg.pixel(OkSideX,OkSideY)[1]== OkSideG:
            if pg.pixel(OkSideX,OkSideY)[2]== OkSideB:
                pg.click(OkSideX,OkSideY)
                time.sleep(1)

    #clicking on yes to start next level
    if pg.pixel(YesX,YesY)[0]==  YesR:
        if pg.pixel(YesX,YesY)[1]== YesG:
            if pg.pixel(YesX,YesY)[2]== YesB:
                pg.click(YesX,YesY)
                time.sleep(1)

    time.sleep(8)
    
    #checking for skip story button
    if pg.pixel(SkipX,SkipY)[0]==  SkipR:
        if pg.pixel(SkipX,SkipY)[1]== SkipG:
            if pg.pixel(SkipX,SkipY)[2]== SkipB:
                pg.click(SkipX,SkipY)

                #clicking on yes to start next level
                if pg.pixel(YesX,YesY)[0]==  YesR:
                    if pg.pixel(YesX,YesY)[1]== YesG:
                        if pg.pixel(YesX,YesY)[2]== YesB:
                            pg.click(YesX,YesY)

                            time.sleep(4)

    print("one loop done")

#done!

    
    

