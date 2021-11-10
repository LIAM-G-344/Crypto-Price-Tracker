import sys
import subprocess

#Crypto-Price-Tracker
#Copyright (C) 2021  LIAM-G-344
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see https://github.com/LIAM-G-344/Crypto-Price-Tracker/blob/main/LICENSE.

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
