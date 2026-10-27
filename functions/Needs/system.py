from os import system, getcwd,getpass,listdir,chdir,path
from time import sleep
def run(command):
    system(command)
def sudo(command):
    run("sudo "+command)
def shutdown(time):
    run("shutdown " + str(time))
def restart(time):
    run("shutdown /r /t " + str(time))
def hibernate(time):
    run("shutdown /h /t" + str(time))
def wait(time):
    sleep(time)
def echo(*args):
    print(*args)
def where():
    return getcwd()
def who():
    return getpass.getuser()
def ls():
    return listdir()
def cd(path):
    chdir(path)
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
    run("cd "+path+" && rm "+name)
def mkdir(path,*args):
    run("cd "+path)
    run("mkdir "+str(*args))
def rmdir(path,*args):
    run("cd "+path)
    run("rmdir "+str(*args))
def exist(file):
    return path.exists(file)
