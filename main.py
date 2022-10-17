from socket import socket
from this import d
import socket
# import PySimpleGUI as sg
from pythonping import ping
from config import IP,DNS,mask,getway
from uuid import getnode as get_mac
import uuid
# from staticMode import subprocess_cmd_static, staticCommand # UNCOM
# from dynamicMode import subprocess_cmd_dynamic, dynamicComand # UNCOM

# layout = [[sg.Button('Static'), sg.Button('Dynamic'), sg.Button("Quit")]] # UNCOM

# window = sg.Window('NETTool', layout) # UNCOM

class UserInfo(): #wrap
    def getIP():
        IP = socket.gethostbyname(socket.gethostname()) 
        return IP

    def getHostname():
        Hostname = socket.gethostname()
        return Hostname

    def getMAC():
        MAC = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1])
        return MAC

    



"""
#UNCOM

def popupAlert(message):
    sg.Popup(message, keep_on_top=True)

while True:
    event, values = window.read()
    if event == "Static":
        subprocess_cmd_static(staticCommand)
        
    elif event == "Dynamic":                  #UNCOM
        subprocess_cmd_dynamic(dynamicComand)
        popupAlert("Dynamic mode Enable")
    elif event == sg.WINDOW_CLOSED or event == "Quit":
        break



window.close()
"""