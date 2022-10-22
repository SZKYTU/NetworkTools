import json
import socket
from re import S
from http import client
from main import UserInfo
from config import socketHost,socketPort


UserInfoJS = {
    # "IP": UserInfo.getIP(),
    "IP": "10.10.10.10",
    # "Hostname": UserInfo.getHostname(),
    "Hostname": "hostname",
    # "MAC": UserInfo.getMAC()}
    "MAC": "ASDASDASDASDASDAS"}

json = json.dumps(UserInfoJS)

    
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("192.168.0.188", 3300))

json = json.encode("utf8")

socket.sendall(json)
