import sys
import subprocess
print("Setup may install as many as 8 packages. If setup.py was not ran with administartor privlages the instalation will fail.")
inp_1 = input("To contine press y/n: ")

if inp_1 == "y":
    print("Installing")
    
elif inp_1 == "Y":
    print("Installing")
    
elif inp_1 == "yes":
    print("Installing")

elif inp_1 == "Yes":
    print("Installing")

elif inp_1 == "n":
    quit()

elif inp_1 == "N":
    quit()

elif inp_1 == "no":
    quit()

elif inp_1 == "No":
    quit()

def install(package):
    try:
        __import__(package)
    except:
        subprocess.call([sys.executable, "-m", "pip", "install", package])

install("requests")
install("json")
install("time")
install("win10toast")
install("datetime")
install("sys")
install("string")
install("os")
install("PySimpleGUI")
install("subprocess")
install("shutil")

import requests
import json
from time import sleep
from win10toast import ToastNotifier
from datetime import datetime
import sys
import string
import os
import PySimpleGUI as sg
import subprocess
import shutil

shutil.move('custom.ico', 'C:\Program Files')

rando = input("Finished, press enter to close out of this windows and open up Crypto-Price-Tracker.pyw")
