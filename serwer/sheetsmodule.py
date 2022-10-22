import os
import sys
import json
import gspread
from datetime import date
# from socketserwer import get #<-- right data from serwer 
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)
today = date.today()

get = '{"IP": "10.10.10.10", "hostname": "hOSTNAME", "mac": "1asdasdasd0.10"}'

get = str(get)
print(type(get))
temp = json.loads(get)
print(f"this temp {temp}")


# sa = gspread.service_account(filename="googlekey2.json")
# sh = sa.open("NetworkTools")

# wks = sh.worksheet("IPdb")

# wks.append_row([UserInfo.getIP(), 
#                 UserInfo.getMAC(),
#                 UserInfo.getHostname(),
#                 str(today.strftime("%d/%m/%Y"))])
