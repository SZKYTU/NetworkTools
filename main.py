import PySimpleGUI as sg
from staticMode import subprocess_cmd_static, staticCommand
from dynamicMode import subprocess_cmd_dynamic, dynamicComand

layout = [[sg.Button('Static'), sg.Button('Dynamic'), sg.Button("Quit")]]

window = sg.Window('Window Title', layout)


while True:
    event, values = window.read()
    if event == "Static":
        subprocess_cmd_static(staticCommand)
    elif event == "Dynamic":
        subprocess_cmd_dynamic(dynamicComand)
    elif event == sg.WINDOW_CLOSED or event == "Quit":
        break

window.close()
