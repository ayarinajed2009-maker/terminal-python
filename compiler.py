from functions.system import *
from functions.video import *
from functions.get import *
from functions.terminal import *
from functions.explorer import *
from functions.updater import *
if exist("code.npx"):
    with open('code.npx', 'r', encoding='utf-8') as file:
        file = file.read()
elif not exist("code.npx"):
    print("no code.npx file to run found !")
    print("opening terminal instead...")
    run("cls")
    print("Terminal v0.1 beta")
    print("Type 'help' to see all commands")
    while True:
        command = input(">>> ")
        start(command)
