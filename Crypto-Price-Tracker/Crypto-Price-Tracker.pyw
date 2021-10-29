import sys, string, os
import PySimpleGUI as sg
import subprocess

layout=[[sg.Text("Choose crypto coin to track")], [sg.Button("ETH")], [sg.Button("BTC")], [sg.Button("XRP")], [sg.Button("XMR")], [sg.Button("Close Program")]]
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
    if event == "XMR":
        from notifyx import xmr as apte
        exit()
        break
    if event == "Close Program":
        exit()
        break
    if event == WIN_CLOSED:
        exit()
        break

window.close()
