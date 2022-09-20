import subprocess
from pythonping import ping
from config import IP,DNS,mask,getway

def ipCheck():
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            FREEIP = ip
            print("-->",FREEIP) #scc!!
            break
    return FREEIP
    


def ethernetAdapterCheck():
    ipcfgCommandout = str(subprocess.check_output("ipconfig /all" )) #<-- static work 
    if "Ethernet 3" in ipcfgCommandout:
        print("done") 
    else:
        print("miss")


ethernetAdapterCheck()

# staticCommand = f'netsh interface ip set dns "Ethernet 2" static {DNS} | netsh interface ip set address name= "Ethernet 2" static {ipCheck()} {mask} {getway}'


def subprocess_cmd_static(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)


# class StaticModeInfo:
#     def __init__(self, IP, MAC, HostName):    <-- to dynamic mode
#         self.IP = IP
#         self.MAC = MAC
#         self.HostName = HostName






