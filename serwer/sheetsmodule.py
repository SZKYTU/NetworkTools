import gspread
import sys
import os
# sys.path.insert(1, 'C:/Users/czupyk_p/Documents/Python/NetworkTools') # FIX THIS BUUBLE

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main import UserInfo

sa = gspread.service_account(filename="googlekey.json")
sh = sa.open("NetworkTools")

wks = sh.worksheet("IPdb")

wks.append_row([UserInfo.getIP()])
