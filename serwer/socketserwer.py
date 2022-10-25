from datetime import date
import gspread
from base64 import decode
import os
import sys
import json
import socket 
from http import client
from email.header import Header
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

today = date.today()


def sheetInsert(json):
    sa = gspread.service_account(filename="googlekey.json")
    sh = sa.open("NetworkTools")

    wks = sh.worksheet("IPdb")
    wks.append_row([json['IP'],
                    json['MAC'],
                    json['Hostname'],
                    str(today.strftime("%d/%m/%Y"))
                    ]
                   )





BUFFER = 1024
from config import socketHost,socketPort

socket = socket.socket(socket.AF_INET  , socket.SOCK_STREAM)
socket.bind((socketHost, socketPort))
socket.listen(2)

while True:
    cliSocket, adress = socket.accept()
    getJSON = json.loads(cliSocket.recv(BUFFER).decode("utf8"))
    sheetInsert(getJSON)
    
