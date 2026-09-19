#libs calls#
from functions.system import *
from functions.video import *
from functions.terminal import *
from functions.explorer import *
from functions.crypt import *
from functions.updater import *
if exist("main.npx"):
    with open('main.npx', 'r', encoding='utf-8') as file:
        file = file.readlines()
    for i in range(len(file)):
        start(file[i])
elif not exist("main.npx"):
    print("no main.npx file to run found !")
    print("opening terminal instead...")
    wait(3)
    run("cls")
    print("Terminal v0.1 beta")
    print("Type 'help' to see all commands")
    while True:
        command = input(">>> ")
        start(command)
