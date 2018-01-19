
# py 对excel进行操作

import xl_reader
import xl_writer
import xlrd

contents = []

list_2d = xl_reader.tolistByName(r"/Users/yanmeng/Downloads/connection/TBData20171228.xlsx", "y2012")
list_2d = list(list_2d)

contents.append(list_2d[0])

for row in range(list_2d.__len__()):
    row_values = list(list_2d[row])
    print(row_values[16])

    if -1.0 == row_values[16]:
        contents.append(row_values)

xl_writer.saveExcel(r"/Users/yanmeng/Downloads/connection/AbsentPoint.xls", "y2012", contents)