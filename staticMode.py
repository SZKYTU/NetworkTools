import os
import subprocess
import time
from config import IP,DNS,mask,getway

staticCommand = f'netsh interface ip set dns "Ethernet 2" static {DNS} | netsh interface ip set address name= "Ethernet 2" static {IP} {mask} {getway}'

def subprocess_cmd_static(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)
