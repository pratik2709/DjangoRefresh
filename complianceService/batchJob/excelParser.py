import os
import xlrd

def parse():
    loc = "hello.xlsx"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)

    col_vals = []
    for i in range(sheet.ncols):
        col_vals.append(sheet.cell_value(0, i))
    print col_vals


