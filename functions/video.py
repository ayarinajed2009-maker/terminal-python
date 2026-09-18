from functions.needs import *
def play(path):
    run("cd "+path)
    run("start "+path)
def play_vlc(file):
    print("WARNING : VLC MUST BE INSTALLED OTHERWISE RUN VLC_PREPARE")
    run("cd functions && vlc.lnk "+file)