#main file for system functions
#system v0.1 beta
import os
from functions.needs import run
from functions.needs import exist
def read(file,is_exsiste):
    if is_exsiste:
            test=exist(file)
    else:
            test=True
    if test:
        run("type "+file)
    else:
        print("ERROR 505 : "+file+" Dosnt exist !")
def mod(file,txt,is_exsiste):
    if is_exsiste:
        test=exist(file)
    else:
        test=True
    if test:
        run("echo "+txt+" >"+file)
    else:
        print("ERROR 505 :"+file+"Dosnt exist !")
def creat_file(path,name,is_exsiste):
    if is_exsiste:
        test=exist(path)
    else:
        test=True
        pass
    if test:
        run("cd "+path)
        run("echo "+" >"+name)
    else:
        print("ERROR 404 : "+path+" Doesnt exist !")
def delete_file(path,name,is_exsiste):
    if is_exsiste:
        test=exist(path)
    else:
        test=True
        pass
    if test:
        run("cd "+path)
        run("del "+name)
    else:
        print("ERROR 404 : "+path+" Doesnt exist !")
def cd(path,is_exsiste):
    if is_exsiste:
        test=exist(path)
    else:
        test=True
        pass
    if test:
        run("cd "+path)
    else:
        print("ERROR 404 : "+path+" Doesnt exist !")
def mkdir(path,name,is_exsiste):
    if is_exsiste:
        test=exist(path)
    else:
        test=True
        pass
    if test:
        run("cd "+path)
        run("mkdir "+name)
    else:
        print("ERROR 404 : "+path+" Doesnt exist !")
def rmdir(path,name,is_exsiste):
    if is_exsiste:
        test=exist(path)
    else:
        test=True
        pass
    if test:
        run("cd "+path)
        run("rmdir "+name)
    else:
        print("ERROR 404 : "+path+" Doesnt exist !")

