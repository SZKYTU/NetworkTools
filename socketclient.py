from http import client
from re import S
import socket
import json
from config import socketHost,socketPort
from main import UserInfo


UserInfoJS = {
    "IP": UserInfo.getIP(),
    "Hostname": UserInfo.getHostname(),
    "MAC": UserInfo.getMAC()}

json = json.dumps(UserInfoJS)

    
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((socketHost, socketPort))

json = json.encode("utf8")

socket.sendall(json)
