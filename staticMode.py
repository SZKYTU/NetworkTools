import os
import subprocess
from pythonping import ping
import time
import re
from config import IP,DNS,mask,getway

# staticCommand = f'netsh interface ip set dns "Ethernet 2" static {DNS} | netsh interface ip set address name= "Ethernet 2" static {IP} {mask} {getway}'

# class StaticModeInfo:
#     def __init__(self, IP, MAC, HostName):    <-- to dynamic mode
#         self.IP = IP
#         self.MAC = MAC
#         self.HostName = HostName



for ip in IP:
    temp = ping(ip, count=1,verbose=True)
    print(type(temp))     #---> go to string 
    if "out" in temp:
        print("FREE")
    else:
        print("NF")


# def subprocess_cmd_static(command):
#     process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
#     proc_stdout = process.communicate()[0].strip()
#     for line in proc_stdout.decode().split('\n'):
#         print (line)
