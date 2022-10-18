import socket 

HOST = '192.168.0.188'
PORT = 33001

socket = socket.socket(socket.AF_INET  , socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(2)

while True:
    cliSocket, adress = socket.accept()
    print(f'Connect {adress}')
