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

def dbfToList(path):
    table = DBF(path)
    tableBody = []
    for item in table.records:
        record = []
        record.append(item['ENTIID'])
        record.append(item['VALUE_1'])
        record.append(item['VALUE_2'])
        record.append(item['VALUE_3'])
        record.append(item['VALUE_4'])
        record.append(item['VALUE_5'])
        record.append(item['VALUE_6'])
        tableBody.append(record)
    return table.field_names,tableBody


codeToLand = {}
target = tolistByNo("/Users/yanmeng/Downloads/landstatics.xlsx",0)
lines = target[1:]
for line in lines:
    codeToLand[line[1]]=line[2]

def resultList(path):
    file = path
    header, body = dbfToList(file)
    body1 = np.array(body)
    df = pd.DataFrame(body, index=body1[:,0], columns=['ENTIID','耕地','林地','草地','水体','城乡建设用地','未利用土地'])
    result = []
    for key in codeToLand.keys():
        matchKey = '1CHN'+str(key)+'000'
        record = []
        if matchKey in df['ENTIID']:
            record.append(str(key))
            record.append(codeToLand[key])
            record.append(df['耕地'][matchKey])
            record.append(df['林地'][matchKey])
            record.append(df['草地'][matchKey])
            record.append(df['水体'][matchKey])
            record.append(df['城乡建设用地'][matchKey])
            record.append(df['未利用土地'][matchKey])
            result.append(record)

    return result


def main(lands, years):
    for  land in lands:
        writer = pd.ExcelWriter("/Users/yanmeng/Downloads/lands/land"+land+".xlsx", engine='openpyxl')
        for year in years:
            file = "/Users/yanmeng/Downloads/lands/countylands_table/"+land+"_"+year+"_six.dbf"
            result = resultList(file)
            df1 = pd.DataFrame(result, columns=['地区编码','地区名', '耕地', '林地', '草地', '水体', '城乡建设用地', '未利用土地'])
            df1.to_excel(writer, sheet_name=year, index=False)
            print("land :"+land+" year :"+year+" number :"+str(df1.__len__()))
        writer.save()


lands = ['county','20','50','100']
years = ['95','2000','05','10','15']
main(lands, years)