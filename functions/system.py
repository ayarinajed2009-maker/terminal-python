import os
from time import sleep
def run(command):
    os.system(command)
def shutdown(time):
    run("shutdown /s /t " + str(time))
def restart(time):
    run("shutdown /r /t " + str(time))
def hibernate(time):
    run("shutdown /h /t" + str(time))
def wait(time):
    sleep(time)
def notify(title, message):
    toast(title, message)