import os
import subprocess

out = subprocess.run('cmd /k netsh interface ip set address "Ethernet 2" dhcp', shell=True)

print(out)
