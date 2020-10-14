import openpyxl

def read_excel(filename, sheet):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.get_sheet_by_name(sheet)
    max_row=worksheet.max_row
    dirt = {}
    for i in range(max_row):
        dirt[i] = [item.value for item in list(worksheet.rows)[i]]
    return dirt, max_row