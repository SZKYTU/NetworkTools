import os
import sys
import json
import socket 
from sheetsmodule import sheetInsert
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


BUFFER = 1024
from config import socketHost,socketPort

socket = socket.socket(socket.AF_INET  , socket.SOCK_STREAM)
socket.bind((socketHost, socketPort))
socket.listen(2)

while True:
    cliSocket, adress = socket.accept()
    getJSON = json.loads(cliSocket.recv(BUFFER).decode("utf8"))
    sheetInsert(getJSON)
    
