import xlwt
import xlrd
from dbfread import DBF
import pandas as pd
from openpyxl import load_workbook
import os
# form unicodedata import unicode
# import unicode


def tolistByName( path, sheet_name ):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows
    list_rows = []
    for row in range(0, nrows):
        row_values = table.row_values(row)
        list_rows.append(row_values)
    return list_rows




def excelYearBuffer(year, buffer):
    list_2d = []
    index = []
    absent = []
    for fid in range(2280):
        fileName = "/Users/yanmeng/Downloads/lightdata/"+str(year)+"buffer"+str(buffer)+"/y"+str(year)+"_d"+str(buffer)+"_fid"+str(fid)+"_table.dbf"
        isExist = os.path.isfile(fileName)
        if isExist:
            table = DBF(fileName, 'latin1')
            for record in table.records:
                # print(record)
                # print(record['SUM'])
                # print(record['VILLAGE'])

                sum = record['SUM']
                # vi = (record['VILLAGE'])
                # print(vi)
                # e = vi.encode()
                # vi = e.decode()
                # print(vi)

                index.append(fid)
                list_2d.append([fid, sum])
        else:
            absent.append(fid)

    value = "ntl"+str(year)+"d"+str(buffer)
    df1 = pd.DataFrame(list_2d, index=index, columns=["fid", value])
    print("year-"+str(year)+" "+"buffer-"+str(buffer)+"   absent:"+str(absent))
    print(absent)
    return df1



def main():
    for y in years:
        writer = pd.ExcelWriter("/Users/yanmeng/Downloads/lightdata/TBData20180104"+str(y)+".xlsx", engine='openpyxl')
        for b in buffers:
            df1 = excelYearBuffer(y,b)
            df1.to_excel(writer,sheet_name=str(b), index=False)
        writer.save()

years = [2013]
buffers = [1]
main()

# def getDataFrame2
# path = "/Users/yanmeng/Downloads/lightdata/TBData20180104.xlsx"
# list_2d = tolistByName(path, "y"+str(year))
# list_2d = list(list_2d)
# index = []
# columns = []
# fid = []
# for row in range(1,list_2d.__len__()):
# 	rowValues = list_2d[row]
# 	index.append(rowValues[0])
#
# df2 = pd.DataFrame(list_2d[1:], index=index, columns=list_2d[0])
#
# result = pd.concat([df1,df2], axis=1)

# print(result["ntl"+str(year)+"d"+str(buffer)].corr(result[u"NTL14D5Y14"]))

# writer = pd.ExcelWriter("/Users/yanmeng/Downloads/lightdata/TBData20180104"+str(year)+str(buffer)+".xlsx", engine='openpyxl')
# print(result)
# df1.to_excel(writer,sheet_name=str(year), index=False)
# writer.save()

'''''''''


# print(df)
sum_values = []
for value in range(2280, 0, -1):
    sum_values.append(value)

name = "ntl2012d5"
df2 = pd.DataFrame(sum_values, index=index, columns=[name])
print(df2)

'''''
