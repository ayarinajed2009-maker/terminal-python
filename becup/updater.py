from functions.Base.updater_essencial import *
from pathlib import Path
class curl():
    def get(url,file):
        run("curl -L "+str(url)+" -o"+str(file))
    def see(url):
        return run("curl -L"+str(url))
class Update():
    def database(pkg):
        base=["CRYPT","SYSTEM","TERMINAL_LIBS","TERMINAL","UPDATER_ESSENCIAL","UPDATER"]
        if pkg.upper() in base:
            return "Base"
        else:
            return "Others"
    def get_pkgs(url_pkg,pkg_file_name,url_pkg_key):
        curl.get(url_pkg,pkg_file_name+".py")
        curl.get(url_pkg_key,"key")
    def pkg_url(pkg):
        return "https://raw.githubusercontent.com/ayarinajed2009-maker/python-terminal-libs/refs/heads/main/"+str(pkg)+".py"
    def pkg_key_url(pkg):
        return "https://raw.githubusercontent.com/ayarinajed2009-maker/python-terminal-libs/refs/heads/main/"+str(pkg)+"-Key"
    def rebuild_libs(pkg,type):
        print("Rebuilding Pkgs file ....")
        file=Path("functions/Base/terminal_libs.py")
        lines = file.read_text(encoding='utf-8').splitlines()
        if type == "Base":
            url="functions.Base."
        elif type == "Others":
            url="functions.Others."
        lines.append("from "+str(url)+str(pkg)+" import *")
        for items in lines:
            print(items)
        file.write_text("\n".join(lines), encoding='utf-8')
    def pkg(pkg):
        Update.get_pkgs(Update.pkg_url(pkg),pkg,Update.pkg_key_url(pkg))
        decrypt(pkg+".py",Update.database(pkg),"key")
        Update.rebuild_libs(pkg,Update.database(pkg))
def pfile(file:str,dir:str):
    os.chdir(dir)
    with open(file, "r") as f:
        print(f.read())
class win():
    def install(app:str):
        run("winget install "+app)
    def update(app:str):
        run("winget update "+app)
    def info(app:str):
        run("winget show "+app)
    def remove(app:str):
        run("winget uninstall "+app)
    def updates():
        run("winget upgrade")
    def download(app:str):
        run("winget download "+app)
    def version():
        with open("functions/Addonsupdate_version", 'r', encoding='utf-8') as file:
                local_version = file.read()
        print("win function v"+local_version)
        print("Outils:")
        print("winget"+str(run("winget --version")))
class py():
    def install(pkg:str):
        run("pip install"+pkg)