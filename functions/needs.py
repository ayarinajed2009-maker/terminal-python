import os
from random import randint
from win11toast import toast
def run(command):
    os.system(command)
def exist(file):
    return os.path.exists(file)
def generate_code(long):
    code=""
    for i in range(long):
        code+=str(randint(0,9))
    return code
def generate_chaine(long):
    chaine=""
    min=randint(0,1)
    for i in range(long):
        if min==1:
            chaine+=chr(randint(ord('A'),ord('Z')))
        else:
            chaine+=chr(randint(ord('a'),ord('z')))
    return chaine
def notify(title, message):
    toast(title, message)
