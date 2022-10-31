# from socket import socket
# import uuid
from unittest import result
from pcinfomodule import UserInfo
import PySimpleGUI as sg
from socketclient import clientJsonSend
from staticMode import subprocess_cmd_static, staticCommand # UNCOM
from dynamicMode import subprocess_cmd_dynamic, dynamicComand # UNCOM

layout = [[sg.Button('Static'), sg.Button('Dynamic'), sg.Button("Quit")]] # UNCOM

window = sg.Window('NETTool', layout) # UNCOM

while True:
    event, values = window.read()
    if event == "Static":
        subprocess_cmd_static(staticCommand)
        
    elif event == "Dynamic":                  #UNCOM
        subprocess_cmd_dynamic(dynamicComand)
        result = sg.popup_yes_no(f"Przydzielone IP -> {UserInfo.getIP()} \n"
                        f"Przydzielony MAC -> {UserInfo.getMAC()} \n"
                        f"Nazwa Komputera -> {UserInfo.getHostname()} \n \n"
                        "Czy wyslac dane do arkusza?")
        print(result)
        if result == "Yes":
            clientJsonSend()
            print("wykonujes")
            break
        
    elif event == sg.WINDOW_CLOSED or event == "Quit":
        break



