from base64 import decode
import os
import sys
import json
import socket 
from http import client
from email.header import Header
current = os.path.dirname(os.path.realpath(__file__));parent = os.path.dirname(current);sys.path.append(parent)

BUFFER = 1024
from config import socketHost,socketPort

socket = socket.socket(socket.AF_INET  , socket.SOCK_STREAM)
socket.bind(("192.168.0.188", 3300))
socket.listen(2)

while True:
    cliSocket, adress = socket.accept()
    get = cliSocket.recv(BUFFER).decode("utf8")
    print(get)
