import uuid
import socket


class UserInfo():  # wrap
    def getIP():
        IP = socket.gethostbyname(socket.gethostname())
        return IP

    def getHostname():
        Hostname = socket.gethostname()
        return Hostname

    def getMAC():
        MAC = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                        for ele in range(0, 8*6, 8)][::-1])
        return MAC
