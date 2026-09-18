from needs import *
import os
def where():
    return os.getcwd()
def who():
    return getpass.getuser()
def ls():
    return os.listdir()
def cd(path):
    os.chdir(path)
def mod(file,txt):
    with open(file, "a") as f:
        f.write(txt)
def overwrite(file,txt):
    with open(file, "w") as f:
        f.write(txt)
def read(file):
    with open(file, "r") as f:
        return f.read()
def pfile(file):
    with open(file, "r") as f:
        print(f.read())
def creat_file(path,name):
    run("cd "+path)
    run("echo "+" >"+name)
def delete_file(path,name):
    run("cd "+path)
    run("del "+name)
def mkdir(path,name):
    run("cd "+path)
    run("mkdir "+name)
def rmdir(path,name):
    run("cd "+path)
    run("rmdir "+name)
