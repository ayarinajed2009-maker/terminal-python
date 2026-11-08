from pygame import mixer
from functions.Base.system import clear,wait
def play_music_file(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(100)
    mixer.music.play()
    mixer.music.get_pos
    while mixer.music.get_busy():
        UI()
def UI():
    global d
    a=10
    for i in range(a):
        print("-",end="")
    print("")
    while mixer.music.get_busy():
        clear()
        time = mixer.music.get_pos()
        time= int((time//1000))*-1
        d=0
        ch=""
        
        for _ in range((time*-1)):
            print("||",end="")
            d+=1
            ch=ch+"-"
            print(ch,end="")
            code()
            #
            
            if len(ch)==15:
                ch=""
            
        S=time
        m=0
        if S==60:
            m+=1
            S=S-60*d
        print("||",end="")
        print(str(time*-1//60),"m:"+str(S*-1)+"s",end="")
        for _ in range(2):
            print(" ",end="")
        print("||")
        print("==MUSIC PLAYER==")
        wait(1)
        clear()
        print('')
def code():
    global d
    clear()
    
    if d==1:
        temp=f'\\ '
        print(temp,end="")
    elif d==2:
        temp='|'
        print(temp,end="")
    elif d==3:
        temp='/'
        print(temp,end="")
    elif d==4:
        temp='|'
        print(temp,end="")
    elif d==5:
        d=1
        code()
    print('||')
def play_music_file_without_UI(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(100)
    mixer.music.play()
    mixer.music.get_pos
    while mixer.music.get_busy():
        wait(1)