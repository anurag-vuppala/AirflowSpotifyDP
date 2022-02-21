# from pydoc import cli
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# # import google.oauth2.service_account as gs
# from pprint import pprint

# scope = ['https://www.googleapis.com/auth/drive',
#            'https://www.googleapis.com/auth/drive.file',
#            'https://www.googleapis.com/auth/drive.readonly',
#            'https://www.googleapis.com/auth/spreadsheets',
#            'https://www.googleapis.com/auth/spreadsheets.readonly',
#            ]

# creds = ServiceAccountCredentials.from_json_keyfile_name('sheet_creds.json',scope)

# client = gspread.authorize(creds) 

# sheet = client.open("api").sheet1

# data = sheet.get_all_records()

# insertRow = ["2","anurag","vuppala"]

# sheet.insert_rows(insertRow, 2)

# pprint(data)




from curses import raw
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

from numpy import insert


key = 'sheet_creds.json'

scope = ['https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive.readonly',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/spreadsheets.readonly',
            ]

creds = None
creds = service_account.Credentials.from_service_account_file(key,scopes=scope)

sheetid = '1bdPEicAieaus4AWU92_Ry11f4XMiYJSncJiWh42bd28'

service = build('sheets','v4',credentials=creds)

sheet = service.spreadsheets()
# this is to get the values from the sheet
result = sheet.values().get(spreadsheetId=sheetid, range="sheet1!A1:C5").execute()


# this is to update values in the sheet

input_value = [[1,"anurag", "vuppala"],[2,"anushike","biskit"]]

result = sheet.values().update(spreadsheetId=sheetid, range="sheet1!A1", valueInputOption='USER_ENTERED', body = {"values": input_value}).execute()
print(result)

########################

#to append values to sheet
append_data = [[3,"venkataswaramma","vuppla"]]

apnd = sheet.values().append(spreadsheetId=sheetid, range="sheet1!A1",valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body = {"values": append_data}).execute()


print(result)
#####################



