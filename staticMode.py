import os
import subprocess
import time
from config import IP,DNS,mask,getway

# staticCommand = f'netsh interface ip set dns "Ethernet 2" static {DNS} | netsh interface ip set address name= "Ethernet 2" static {IP} {mask} {getway}'

for ip in IP:
    subprocess.run(f'ping -n 1 {ip}')

ipFree = False

class StaticModeInfo:
    def __init__(self, IP, MAC, HostName):
        self.IP = IP
        self.MAC = MAC
        self.HostName = HostName


def subprocess_cmd_static(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)
