#some functions nessary for system to work
#needs add-on v0.2 alpha
import os
from random import randint
from win11toast import toast
def run(command):
    os.system(command)
def exist(file):
    os.path.exists(file)
def generate_code(long):
    code=""
    for i in range(long):
        code+=str(randint(0,999999999))
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
class get():
    def install(app):
        run("winget install "+app)
    def update(app):
        run("winget update "+app)
    def update_list():
        run("winget upgrade >temp.txt")
        test=exist("temp.txt")
        if test:
                run("type temp.txt")
        else:
            print("ERROR 305 : fail to get informations !")
    def uninstall(app):
        run("winget uninstall "+app)