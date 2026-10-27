from system import run,sudo,cd
import platform
class pacman():  
    def install(app):
        run(sudo("pacman -S --needed "+str(app)))
    def update():
        run(sudo("pacman -Syu"))
    def uninstall(app):
        run(sudo("sudo pacman -Rs "+app))
    def clear_cache():
        run(sudo("sudo pacman -Scc"))
class yay():
    def install(app):
        run(sudo("yay -S "+str(app)+" --noconfirm"))
    def update(app):
        run(sudo("yay"))
class git():
    def clone(url):
        run("git clone "+url)
    def init():
        run("git init")
    def status():
        run("git status")
    def add():
        run("git add --all")
    def msg(msg:str):
        run("git commit --message"+msg)
    def push():
        run("git push")
    def pull():
        run("git pull")
    def reset_all():
        run("git reset --hard; git clean --force")
class get():
    def check():
        try:
            info = platform.freedesktop_os_release()
            Distro_Name=info.get("NAME")
            Family_Name = info.get("ID_LIKE", "Independent")
            print(Family_Name+str("     ")+Distro_Name)
            
        except AttributeError:
            print("This method requires Python 3.10 or newer.")
        except OSError:
            print("Not running on a Linux system.")
        return Distro_Name
    def nesseaire(OS):
        if OS == "Arch Linux":
            a=str(input("Did u wanna to Install Essenction like (AUR..)(Y or n): "))
            if a=="Y":
                pacman.update()
                pacman.install("base-devel git")
                git.clone("https://aur.archlinux.org/yay.git")
                cd("yay")
                run("makepkg -si")
            else:
                pass
    def install(OS,app):
        if OS == "Arch Linux":
            pacman.update()
            pacman.install(app)
    def update(OS):
        if OS == "Arch Linux":
            pacman.update()
    def uninstall(OS,app):
        if OS == "Arch Linux":
            pacman.uninstall(app)
    def clear(OS):
        if OS == "Arch Linux":
            pacman.clear_cache()
class Python():
    def install(pak):
        run("pip install "+pak)
            