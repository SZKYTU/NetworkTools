from this import d
import PySimpleGUI as sg
from pythonping import ping
from config import IP,DNS,mask,getway
# from staticMode import subprocess_cmd_static, staticCommand # UNCOM
# from dynamicMode import subprocess_cmd_dynamic, dynamicComand # UNCOM

layout = [[sg.Button('Static'), sg.Button('Dynamic'), sg.Button("Quit")]]

# window = sg.Window('NETTool', layout) # UNCOM

def ipCheck():
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            FREEIP = ip
            break
    return FREEIP

class DynamicModeInfo:
    def __init__(self, IP, MAC, HostName):   
        self.IP = IP
        self.MAC = MAC
        self.HostName = HostName

    def __str__(self):
        return f"{self.IP}-{self.MAC}-{self.HostName}"

TESTDOCKER = DynamicModeInfo(ipCheck())
print(TESTDOCKER)

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