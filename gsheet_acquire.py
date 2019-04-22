import gspread

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('inspiring-wares-238419-29f9b1ddab99.json', 'scope')

gc = gspread.authorize(credentials)

sheet = gc.open_by_key('1-6utKSkWXI_bKtzsUXz80oSG-9So1h1z3IFvuehKCPE/')

worksheet = sheet.get_worksheet(0)

name_list = worksheet.col_values(1)
email_list = worksheet.col_values(2)

print(name_list[0])
