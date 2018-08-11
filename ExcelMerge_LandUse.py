import xlwt
import xlrd
from dbfread import DBF
import pandas as pd
from openpyxl import load_workbook
import os
import numpy as np


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


codeMap = {}
target = tolistByNo("/Users/yanmeng/Downloads/landstatics.xlsx",0)
lines = target[1:]
for line in lines:
    codeMap[line[1]]=line[2]

# 将dbf数据合并成一个excel
def excelYearBuffer(fromdir, year, buffer):
    filePath = fromdir+str(year)+'/'+str(buffer)
    list_2d = []
    absent = []
    count = 0
    for key in codeMap.keys():
        count += 1
        # print (str(count))
        file = filePath+'/'+'1CHN'+str(key)+'000.dbf'
        isExist = os.path.exists(file)
        item = []
        if isExist:
            table = DBF(file)

            for record in table.records:
                if year is '95':
                    item.append('1995')
                if year is '2000':
                    item.append('2000')
                if year is '05':
                    item.append('2005')
                if year is '10':
                    item.append('2010')
                if year is '15':
                    item.append('2015')
                item.append(str(key))
                item.append(str(codeMap[key]))
                try:
                    item.append(record['VALUE_1'])
                except:
                    item.append(0.0)
                try:
                    item.append(record['VALUE_2'])
                except:
                    item.append(0.0)
                try:
                    item.append(record['VALUE_3'])
                except:
                    item.append(0.0)
                try:
                    item.append(record['VALUE_4'])
                except:
                    item.append(0.0)
                try:
                    item.append(record['VALUE_5'])
                except:
                    item.append(0.0)
                try:
                    item.append(record['VALUE_6'])
                except:
                    item.append(0.0)

                recordSum = 0.0
                for i in range(6):
                    recordSum += float(item[i+3])
                for i in range(6):
                    item[i + 3] = item[i+3] / recordSum

            list_2d.append(item)
        else:
            absent.append(str(key))
            item.append(str(key))
            item.append(str(codeMap[key]))
            for i in range(6):
                item.append(str(-1))
        # list_2d.append(item)
    df = pd.DataFrame(list_2d, columns=['年份', '地区编码','地区名', '耕地', '林地', '草地', '水体', '城乡建设用地', '未利用土地'])
    print (">> year : "+str(year) +"  buffer : "+str(buffer))
    print (">> land count "+ str(df.__len__()))
    print (">> absent count "+ str(len(absent)))
    print (">> ... ...")
    return df



def main(fromdir, todir, years, buffers):
    for y in years:
        writer = pd.ExcelWriter(todir+"LLUC_"+str(y)+".xlsx", engine='openpyxl')
        for b in buffers:
            df = excelYearBuffer(fromdir, y, b)
            df.to_excel(writer, sheet_name=str(b), index=False)
        writer.save()


fromdir = "/Users/yanmeng/Downloads/workerdir/"
todir = "/Users/yanmeng/Downloads/workerdir/"
years = ['95','2000','05','10','15']
buffers = ['20','50','100']

# table = DBF(fromdir+'05/'+'20/'+'1CHN610404000.dbf')
# print(str(table.field_names))
# for record in table:
#     print(str(record))

main(fromdir, todir, years, buffers)

