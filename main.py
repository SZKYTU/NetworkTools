from this import d
import PySimpleGUI as sg
from pythonping import ping
from config import IP,DNS,mask,getway
# from staticMode import subprocess_cmd_static, staticCommand # UNCOM
# from dynamicMode import subprocess_cmd_dynamic, dynamicComand # UNCOM

layout = [[sg.Button('Static'), sg.Button('Dynamic'), sg.Button("Quit")]]

# window = sg.Window('NETTool', layout) # UNCOM

class DynamicModeInfo:
    def getIp():
        

    def __str__(self):
        return f"{self.IP}"


print(DynamicModeInfo())



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