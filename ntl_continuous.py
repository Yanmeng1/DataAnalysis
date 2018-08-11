# py 对excel进行操作
import xlrd
import numpy as np
import pandas as pd
import copy
from copy import deepcopy
from sklearn.linear_model import LinearRegression

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


buffers = [1,2,3,4,5,10,20,50,100,200]
years = np.arange(2015,2011,-1)

# 创建excel
writer = pd.ExcelWriter(r"/Users/yanmeng/Desktop/TBData20180503V3.xlsx", engine='openpyxl')

before_year = 2016
before_temp = tolistByName(r"/Users/yanmeng/Desktop/TBData20180503V2.xlsx", "y" + str(before_year))
before = pd.DataFrame(before_temp[1:], columns=before_temp[0])

# 逐年校准
for year in years:

    current_year = year
    # 将初始年份放在before中

    print(" >> processing : "+str(current_year))
    current_temp = tolistByName(r"/Users/yanmeng/Desktop/TBData20180503V2.xlsx", "y" + str(current_year))
    current = pd.DataFrame(current_temp[1:], columns=current_temp[0])

    for buffer in buffers:

        # 拼接字段
        current_field = "ntl" + str(current_year) + "d" + str(buffer)
        before_field = "ntl" + str(before_year) + "d" + str(buffer)
        print("  >"+str(current_field))

        # 找出当前年分中较大的字段，将去年的值赋给当前年份
        for i in range(current[current_field].__len__()):
            if (current[current_field][i]>before[before_field][i]):
                print("  ---  "+str(current[current_field][i])+" < "+str(before[before_field][i]))
                current[current_field][i] = deepcopy(before[before_field][i])

        # for i in range(current[current_field].__len__()):
        #     current.loc[i, current_field] = int(current.loc[i, current_field])
        #     before[before_field][i] = int(before[before_field][i])

        # current.loc[(current[current_field]-before[before_field])>0, current_field] = before.loc[(current[current_field]-before[before_field])>0, before_field]

    # 将矫正年份写入excel中
    current.to_excel(writer, sheet_name=str(current_year), index=False)
    before_year = current_year
    before = current

writer.save()