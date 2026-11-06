lazy import os
lazy import functions.Base.crypt as crypt
lazy import shutil
from pathlib import Path
def run(command):
    os.system(command)
def rmdir(path,name):
    run("cd "+path)
    run("rmdir "+name)
def cp(file,new_path):
    shutil.move(file,new_path)
def mkdir(path,*args):
    run("cd "+path)
    run("mkdir "+str(*args))
def exist(file):
    return os.path.exists(file)
def delete_file(path,name):
    run("cd "+path+" && del "+name)
def getinfo(name):
    run("mkdir temps && cd temps && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/"+name+" -O version")
def decrypt(file,type,key):
    crypt.generate_crypt.run(file,False)
    if type == "Base":
        url="functions/Base/"
    elif type == "Others":
        url="functions/Others/"
    src = Path(file)
    dst = Path(url+file)
    src.replace(dst)
