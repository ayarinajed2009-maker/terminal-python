PACKAGE = "SNAKE"
VERSION = 0.1
MADE_BY = "Najed Ayari"
#These Will be Removed When it's Compleated!
import os
import time
from numpy import array
from random import randint
import msvcrt
def run(command):
    os.system(command)
def clear():
    run("cls")
def wait(s):
    time.sleep(s)






#Functions
def Draw_Gui():
    global x,y,pos,Score
    x,y=0,0
    r=0
    Map=array([[0]*6]*28)
    pos="L"
    fps=4
    zx,zy=randint(0,28),randint(0,5)
    Score=0
    while True:
        n=30-2
        i=0
        Controle()
        if x==28 or x==-28:
                            x=0
        elif x==27 or x==-27:
                            x=-1
        elif zx == 28:
                            zx=0
        elif y==6 or y==-6:
                            y=0
        elif zy==6:
                            zy=0
        elif Map[x][y]==Map[zx][zy]:
               Score+=1
               r+=1
               zx,zy=randint(0,28),randint(0,5)
        #Data Updater
        for o in range(28):
            for a in range(6):
                Map[o][a]=0
                Map[x][y]=1
                Map[zx][zy]=2
                for _ in range(1,r):
                    Map[x-_][y]=3
        print("##############################")
        #Drawer
        for d in range(6):
            print("#",end="")
            ok=False
            for j in range(28):
                    if Map[j][d]==0:
                        print("░",end="")
                    elif Map[j][d]==1:
                        Player(pos)
                    elif Map[j][d]==2:
                        point()
                    elif Map[j][d]==3:
                        for _ in range(1,r):
                            tail()
            print("#")
        n-=1
        print("##############################")
        print(Map,end="")
        print("")
        wait(fps)
        clear()
def Controle():
    global x,y,pos,Score
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
            if key == b'K':
                x-=1
                pos="L"
            elif key == b'M':
                x+=1
                pos="R"
            elif key == b'P':
                y+=1
                pos="U"
            elif key == b'H':
                y-=1
                pos="D"
        if key.decode("utf-8").lower() =="q":
            print("This is ur Score "+str(Score))
            exit()
def Player(Pos):
    if Pos=="R":
        print(">",end="")
    elif Pos=="L":
        print("<",end="")
    elif Pos=="D":
        print("↑",end="")
    elif Pos=="U":
        print("↓",end="")
def point():
    print("■",end="")
def tail():
    global pos
    if pos=="R" or pos=="L":
            print("-",end="")
    elif pos=="D" or pos=="U":
            print("|",end="")
            
Draw_Gui()
