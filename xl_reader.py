# py 对excel进行操作

import xlrd


'''根据sheet编号读取Excel中的数据'''
def tolistByNo( path, sheet_no ):
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet_no]
    nrows = table.nrows
    list_rows=[]
    for row in range(0, nrows):
        row_values = table.row_values(row)
        list_rows.append(row_values)
    return list_rows

'''根据sheet名称读取Excel中的数据'''
def tolistByName( path, sheet_name ):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows
    list_rows = []
    for row in range(0, nrows):
        row_values = table.row_values(row)
        list_rows.append(row_values)
    return list_rows

# print(tolist_sheetname(r"/Users/yanmeng/Downloads/connection/TBData20171228.xlsx", "y2012"))

