import socket
from config import socketHost,socketPort


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((socketHost, socketPort))


