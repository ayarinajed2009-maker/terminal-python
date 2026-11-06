lazy import os
lazy import time as time
lazy import shutil
lazy import getpass
def run(command):
    os.system(command)
def shutdown(time):
    run("shutdown /s /t " + str(time))
def restart(time):
    run("shutdown /r /t " + str(time))
def hibernate(time):
    run("shutdown /h /t" + str(time))
def wait(time):
    time.sleep(time)
def echo(*args):
    print(*args)
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
    run("mkdir "+str(*args))
def rmdir(path,*args):
    run("cd "+path)
    run("rmdir "+args)
def exist(file):
    return os.path.exists(file)
def cp(file,new_path):
    shutil.copyfile(file,new_path)