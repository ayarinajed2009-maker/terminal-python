from functions.system import *
from functions.video import *
from functions.get import *
from functions.explorer import *
def start(command):
    if command == "help":
            print("Commands:")
            print("help - shows this help message")
            print("exit - exits the terminal")
            print("update - updates the terminal")
            print("info <app> - shows information about an app")
    elif command == "exit":
            exit()
    elif command == "update":
            get.self_update()
    elif command.startswith("info "):
            app = command.split(" ")[1]
            get.info(app)
    elif command.startswith("install "):
            app = command.split(" ")[1]
            get.install(app)
    elif command.startswith("update_list"):
            get.update_list(True)
    elif command.startswith("update "):
            app = command.split(" ")[1]
            get.update(app)
    elif command.startswith("uninstall "):
            app = command.split(" ")[1]
            get.uninstall(app)
    elif command.startswith("where"):
            print(where())
    elif command.startswith("who"):
            print(who())
    elif command.startswith("ls"):
            print(ls())
    elif command.startswith("cd "):
            path = command.split(" ")[1]
            cd(path)
    elif command.startswith("mod "):
            file = command.split(" ")[1]
            txt = command.split(" ")[2]
            mod(file,txt)
    elif command.startswith("overwrite "):
            file = command.split(" ")[1]
            txt = command.split(" ")[2]
            overwrite(file,txt)
    elif command.startswith("read "):   
            file = command.split(" ")[1]
            read(file)
    elif command.startswith("pfile "):
            file = command.split(" ")[1]
            pfile(file)
    elif command.startswith("creat_file "):
            path = command.split(" ")[1]
            name = command.split(" ")[2]
            creat_file(path,name)
    elif command.startswith("delete_file "):
            path = command.split(" ")[1]
            name = command.split(" ")[2]
            delete_file(path,name)
    elif command.startswith("mkdir "):
            path = command.split(" ")[1]
            name = command.split(" ")[2]
            mkdir(path,name)
    elif command.startswith("rmdir "):
            path = command.split(" ")[1]
            name = command.split(" ")[2]
            rmdir(path,name)
    elif command.startswith("shutdown "):
            time = command.split(" ")[1]
            shutdown(time)
    elif command.startswith("restart "):
            time = command.split(" ")[1]
            restart(time)
    elif command.startswith("hibernate "):
            time = command.split(" ")[1]
            hibernate(time)
    elif command.startswith("wait "):
            time = command.split(" ")[1]
            wait(time)
    elif command.startswith("clear"):
            run("cls")
    elif command.startswith("notify "):
            title = command.split(" ")[1]
            message = command.split(" ")[2]
            notify(title,message)
    elif command.startswith("play "):
            path = command.split(" ")[1]
            play(path)
    elif command.startswith("vlc "):
            file = command.split(" ")[1]
            play_vlc(file)
    elif command.startswith("rmdir "):
            path = command.split(" ")[1]
            name = command.split(" ")[2]
            rmdir(path,name,False)
    elif command.startswith("help "):
            command = command.split(" ")[1]
            if command == "install":
                print("install <app> - installs an app using winget")
            elif command == "update_list":
                print("update_list - shows a list of apps that can be updated using winget")
            elif command == "update":
                print("update <app> - updates an app using winget")
            elif command == "uninstall":
                print("uninstall <app> - uninstalls an app using winget")
            elif command == "info":
                print("info <app> - shows information about an app using winget")
            elif command == "read":
                print("read <file> - reads the contents of a file")
            elif command == "mod":
                print("mod <file> <text> - modifies the contents of a file with the specified text")
            elif command == "creat_file":
                print("creat_file <path> <name> - creates a new file at the specified path with the specified name")
            elif command == "delete_file":
                print("delete_file <path> <name> - deletes a file at the specified path with the specified name")
            elif command == "cd":
                print("cd <path> - changes the current directory to the specified path")
            elif command == "mkdir":
                print("mkdir <path> <name> - creates a new directory at the specified path with the specified name")
            elif command == "rmdir":
                print("rmdir <path> <name> - removes a directory at the specified path with the specified name")
            elif command == "notify":
                print("notify <title> <message> - sends a notification with the specified title and message")
            elif command == "play":
                print("play <path> - plays a media file at the specified path using the default media player")
            elif command == "vlc":
                print("vlc <file> - plays a media file using VLC media player")
            else:
                print("install <app> - installs an app using winget")
                print("update_list - shows a list of apps that can be updated using winget")
                print("update <app> - updates an app using winget")
                print("uninstall <app> - uninstalls an app using winget")
                print("info <app> - shows information about an app using winget")
                print("read <file> - reads the contents of a file")
                print("mod <file> <text> - modifies the contents of a file with the specified text")
                print("creat_file <path> <name> - creates a new file at the specified path with the specified name")
                print("delete_file <path> <name> - deletes a file at the specified path with the specified name")
                print("cd <path> - changes the current directory to the specified path")
                print("mkdir <path> <name> - creates a new directory at the specified path with the specified name")
                print("rmdir <path> <name> - removes a directory at the specified path with the specified name")
                print("notify <title> <message> - sends a notification with the specified title and message")
                print("play <path> - plays a media file at the specified path using the default media player")
                print("vlc <file> - plays a media file using VLC media player")
    else:
            print("Unknown command: "+command)
            print("Try update the terminal to get the latest commands !")
            print("Type 'help' to see all commands")