import sys, string, os
import PySimpleGUI as sg
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
    
layout=[[sg.Text("Choose crypto coin to track")], [sg.Button("ETH")], [sg.Button("BTC")], [sg.Button("XRP")], [sg.Button("LTC")], [sg.Button("Close Program")]]
window = sg.Window("Menu",layout)

while True:
    event, values = window.read()
    if event == "ETH":
        from notifyx import eth as apte
        exit()
        break
    if event == "BTC":
        from notifyx import btc as apte
        exit()
        break
    if event == "XRP":
        from notifyx import xrp as apte
        exit()
        break
    if event == "LTC":
        from notifyx import ltc as apte
        exit()
        break
    if event == "Close Program":
        exit()
        break
    if event == WIN_CLOSED:
        exit()
        break

window.close()
