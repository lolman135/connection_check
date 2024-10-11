import subprocess
from datetime import datetime
from tkinter import messagebox as ms
from time import sleep
from playsound import playsound
import error_warning as ew
import os

def connect(os_info):
    try:
        result = subprocess.run(["ping", os_info, "1", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode
    except Exception as e:
        return 1

def check_connection(os_info):
    counter = 0
    while counter < 2:
        return_value = connect(os_info)
        sleep(2)
        if return_value != 0:
            counter += 1
            sleep(2)
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Error: connetcion failed [{current_time}]!!")
        else:
            counter = 0
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"connected [{current_time}]...")
    sleep(2)
    # here you can modify code to automatic reboot system if you want to solve connection problem
    
    playsound("warning.mp3")
    answear  = ew.Error.throw_error()
    return answear

if os.name == "nt":
    os_info = "-n"
    shutdown = "shutdown /r /t 0"
else:
    os_info = "-c"
    shutdown = "sudo "

while True:
    answear = check_connection(os_info=os_info)
    sleep(2)

    if answear == "y":
        break
    elif answear =="r":
        os.system(shutdown)