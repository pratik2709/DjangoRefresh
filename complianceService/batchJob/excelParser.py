import os
import xlrd

def parse():
    loc = "hello.xlsx"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)

    colidx = dict((sheet.cell(0, i).value, i) for i in range(sheet.ncols))
    print colidx
    return { sheet.cell(1, colidx["First"]).value : sheet.cell(1, colidx["Second"]).value }




