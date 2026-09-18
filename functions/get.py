from functions.system import *
class get():
    def install(app):
        run("winget install "+app)
    def update(app):
        run("winget update "+app)
    def update_list(pas):
        run("winget upgrade >temp.txt")
        if pas:
            test=True
        elif not pas:
            test=exist("temp.txt")
        if test:
                run("type temp.txt")
        else:
            print("ERROR 305 : fail to get informations !")
    def uninstall(app):
        run("winget uninstall "+app)
    def self_update():
        run("mkdir temps && cd temps && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/version -O version")
        with open('functions/version', 'r', encoding='utf-8') as file:
            local_update = file.read()
        with open('temps/version', 'r', encoding='utf-8') as file:
            server_update = file.read()
        if local_update == server_update:
            run("rmdir /s /q temps")
            print("No update available !")
        elif local_update != server_update:
            run("rmdir /s /q temps && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/needs.py -O functions/needs.py && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/system.py -O functions/system.py && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/video.py -O functions/video.py && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/version -O functions/version && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/compiler.py -O compiler.py && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/get.py -O functions/get.py && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/functions/terminal.py -O functions/terminal.py && wget https://raw.githubusercontent.com/ayarinajed2009-maker/terminal-python/refs/heads/main/run.bat -O run.bat")
    def info(app):
        run("winget show "+app)
            