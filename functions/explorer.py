from functions.system import *
import os
import getpass
def where():
    return os.getcwd()
def who():
    return getpass.getuser()
def ls():
    return os.listdir()
def cd(path):
    os.chdir(path)
def mod(file,*args):
    with open(file, "a") as f:
        f.write(*args)
def overwrite(file,*args):
    with open(file, "w") as f:
        f.write(*args)
def read(file):
    with open(file, "r") as f:
        return f.read()
def pfile(file):
    with open(file, "r") as f:
        print(f.read())
def creat_file(path,name):
    run("cd "+path)
    run("echo "+" >"+name)
    overwrite(name," ")
def delete_file(path,name):
    run("cd "+path+" && del "+name)
def mkdir(path,*args):
    run("cd "+path)
    run("mkdir "+*args)
def rmdir(path,*args):
    run("cd "+path)
    run("rmdir "+*args)
def exist(file):
    return os.path.exists(file)
