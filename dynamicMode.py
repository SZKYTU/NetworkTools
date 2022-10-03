import time
import subprocess
import psutil

InterfaceName= list(psutil.net_if_stats())[0]

dynamicComand = f'netsh interface ip set address "{InterfaceName}" dhcp | netsh interface ip set dns "Ethernet 2" dhcp'


# class StaticModeInfo:
#     def __init__(self, IP, MAC, HostName):   
#         self.IP = IP
#         self.MAC = MAC
#         self.HostName = HostName


def subprocess_cmd_dynamic(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)
        
