import time
import subprocess

dynamicComand = 'netsh interface ip set address "Ethernet 2" dhcp | netsh interface ip set dns "Ethernet 2" dhcp'

def subprocess_cmd_dynamic(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)
