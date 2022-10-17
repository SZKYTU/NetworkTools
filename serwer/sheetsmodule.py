import gspread
import sys
sys.path.insert(1, 'C:/Users/czupyk_p/Documents/Python/NetworkTools') # FIX THIS BUUBLE
from main import UserInfo

sa = gspread.service_account(filename="googlekey.json")
sh = sa.open("NetworkTools")

wks = sh.worksheet("IPdb")

wks.update("A", UserInfo.getIP())