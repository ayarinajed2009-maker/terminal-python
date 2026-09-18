from  os import system,path
def run(command):
    system(command)
def delete_file(path,name):
    run("cd "+path+" && del "+name)
def exist(file):
    return path.exists(file)
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
    def info(app):
        run("winget show "+app)
    def start_up():
        print("Starting terminal...")
        print("checking for updates...OK")
        print("checking for dependencies...Failed")
        self.self_update()
