import os
import sys
import json
import gspread
from datetime import date
from socketserwer import get #<-- right data from serwer 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
today = date.today()

def sheetInsert(json):
    sa = gspread.service_account(filename="googlekey2.json")
    sh = sa.open("NetworkTools")

    wks = sh.worksheet("IPdb")
    wks.append_row([get['IP'], 
                    # UserInfo.getMAC(),
                    # UserInfo.getHostname(),
                    # str(today.strftime("%d/%m/%Y"))
                    ]
                    )
