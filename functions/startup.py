from function.system import run
from functions.get import *
from functions.explorer import *
def first_start():
    a=read("first_start.txt")
    if exist("first_start.txt"):
        if a=="True":
            get.start_up()
        elif a=="False":
            pass
    elif not exist("first_start.txt"):
        run("echo True >first_start.txt")
        get.start_up()