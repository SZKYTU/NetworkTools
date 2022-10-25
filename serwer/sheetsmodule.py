import os
import sys
import json
import gspread
from datetime import date

def sheetInsert(json):
    sa = gspread.service_account(filename="googlekey.json")
    sh = sa.open("NetworkTools")

    wks = sh.worksheet("IPdb")
    wks.append_row([json['IP'],
                    json['MAC'],
                    json['Hostname'],
                    str(date.today().strftime("%d/%m/%Y"))
                    ]
                   )
