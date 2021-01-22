import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet']
cell = sheet['a1']
cell = sheet.cell(1, 1)