import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('inspiring-wares-238419-29f9b1ddab99.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open_by_key('1-6utKSkWXI_bKtzsUXz80oSG-9So1h1z3IFvuehKCPE')

wks = sheet.get_worksheet(0)

name_list = wks.col_values(1)
email_list = wks.col_values(2)

print(f"{wks.cell(1,1).value}, {wks.cell(1,2).value}")

"""
for i in wks.range('A1:A5'):
    for j in wks.range('B1:B5'):
        print(f"{wks.cell(i,j).value}, {wks.cell(i,j+1).value}")
"""
