from datetime import date
import gspread
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
today = date.today()

from main import UserInfo

sa = gspread.service_account(filename="googlekey2.json")
sh = sa.open("NetworkTools")

wks = sh.worksheet("IPdb")

wks.append_row([UserInfo.getIP(), 
                UserInfo.getMAC(),
                UserInfo.getHostname(),
                str(today.strftime("%d/%m/%Y"))])
