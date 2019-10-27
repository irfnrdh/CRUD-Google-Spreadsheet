pip3 install gspread oauth2client

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = client.open('name file').sheet1

pp = pprint.PrettyPrinter()
# sheet.row_values(6)
# sheet.cell(1,1).value
# sheet.update(1,1,'text update')
# sheet.cell(1,1).value
result = sheet.get_all_records()
pp.print(result)


row = ['satu','dua','tiga']
index = 3
sheet.insert_row(row,index)
sheet.delete_row(row,index)

print(sheet.row_count)




