from os import system,path
def run(command):
    system(command)
def rmdir(path,name):
    run("cd "+path)
    run("rmdir "+name)
def exist(file):
    return path.exists(file)
def delete_file(path,name):
    run("cd "+path+" && del "+name)
def getinfo(name):
    run("mkdir temps && cd temps && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/"+name+" -O version")
def clean():
    delete_file("temps","version")
    rmdir(' ','temps')
def getupdate():
    getinfo("get_version")
    with open("functions/get_version", 'r', encoding='utf-8') as file:
        local_version = file.read()
    with open('temps/version', 'r', encoding='utf-8') as file:
        server_version = file.read()
    if server_version==local_version:
        print("They are no get updates !")
        pass
    elif server_version!=local_version:
        print("Updated found v"+server_version)
        choix=str(input("Do u want to update?:(Y or n)"))
        if choix=="Y" or choix=="y":
            delete_file("functions","get.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/get.py -O functions/get.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/get_version -O functions/get_version")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/updater.py -O functions/updater.py")
        else:
            pass
    clean()
def Addonsupdate():
    getinfo("Addonsupdate_version")
    with open("functions/Addonsupdate_version", 'r', encoding='utf-8') as file:
        local_version = file.read()
    with open('temps/version', 'r', encoding='utf-8') as file:
        server_version = file.read()
    if server_version==local_version:
        print("They are no Add-on updates !")
        pass
    elif server_version!=local_version:
        print("Updated found v"+server_version)
        choix=str(input("Do u want to update?:(Y or n)"))
        if choix=="Y" or choix=="y":
            delete_file("functions","gener.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/video.py -O functions/video.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/image.py -O functions/image.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/Addonsupdate_version -O functions/Addonsupdate_version")
        else:
            pass
    clean()
def coreupdate():
    getinfo("core_version")
    with open("functions/core_version", 'r', encoding='utf-8') as file:
        local_version = file.read()
    with open('temps/version', 'r', encoding='utf-8') as file:
        server_version = file.read()
    if server_version==local_version:
        print("They are no Core updates !")
        pass
    elif server_version!=local_version:
        print("Updated found v"+server_version)
        choix=str(input("Do u want to update?:(Y or n)"))
        if choix=="Y" or choix=="y":
            delete_file("functions","gener.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/terminal.py -O functions/terminal.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/crypt.py -O functions/crypt.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/system.py -O functions/system.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/explorer.py -O functions/explorer.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/updater.py -O functions/updater.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/compiler.py -O compiler.py")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/run.bat -O run.bat")
            run("wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/core_version -O functions/core_version")
        else:
            pass
    clean()
def allupdate():
    coreupdate()
    getupdate()
    Addonsupdate()
class win():
    def install(app):
        run("winget install "+app)
    def update(app):
        run("winget update "+app)
    def info(app):
        run("winget show "+app)
    def remove(app):
        run("winget uninstall "+app)
    def updates():
        run("winget upgrade")
    def download(app):
        run("winget download "+app)
    def version():
        with open("functions/Addonsupdate_version", 'r', encoding='utf-8') as file:
                local_version = file.read()
        print("win function v"+local_version)
        print("Outils:")
        print("winget"+str(run("winget --version")))
