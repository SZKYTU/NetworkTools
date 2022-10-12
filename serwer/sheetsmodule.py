import gspread

sa = gspread.service_account(filename="googlekey.json")
sh = sa.open("NetworkTools")

wks = sh.worksheet("IPdb")

wks.update("A2", "TEST")