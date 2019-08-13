import openpyxl

zichan = openpyxl.load_workbook("zichan.xlsx")

print(zichan.get_sheet_names())

