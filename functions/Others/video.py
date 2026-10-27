from Needs.get import get
from Needs.system import run,exist
import subprocess
def Test_Vlc():
    try:
        print("[Info] Attempting to launch VLC...")
        subprocess.run(["vlc"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("[Error] VLC is not installed or couldn't be found.")
        print("[Info] installing vlc ...")
        get.install(get.check,"vlc")
def run_file(file):
    if exist(file):
        run("vlc "+file)
    else:
        print("[ERROR] File Does not Existe")
        
        
