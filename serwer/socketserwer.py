import socket 
from config import socketHost,socketPort


socket = socket.socket(socket.AF_INET  , socket.SOCK_STREAM)
socket.bind((socketHost, socketPort))
socket.listen(2)

while True:
    cliSocket, adress = socket.accept()
    print(f'Connect {adress}')
