from base64 import decode
from email.header import Header
from http import client
import json
import socket 
import os
import sys
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
    print(cliSocket)
    get = cliSocket.recv(BUFFER).decode("utf8")
    print(get)
