# py 对excel进行操作

import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# print(tolistByName( r"/Users/yanmeng/Desktop/TBData20180201最终版.xlsx", "y2012" ))
# temp = tolistByName(r"/Users/yanmeng/Desktop/TBData20180201最终版.xlsx", "y"+str(2012) )
# year_pandas = pd.DataFrame(temp[1:], columns=temp[0])
# print(year_pandas)

year = np.arange(2012,2017,1)
distance = [10,20,50,100,200]

year_value = []

for y in year:
    temp = tolistByName(r"/Users/yanmeng/Desktop/TBData20180503.xlsx", "y"+str(y) )
    year_pandas = pd.DataFrame(temp[1:], columns=temp[0])
    distance_value = []
    for d in distance:
        field = "ntl"+str(y)+"d"+str(d)
        distance_value.append(year_pandas[field].sum())
    year_value.append(distance_value)

result_pandas = pd.DataFrame(year_value,index = year, columns=distance)

print(result_pandas)

N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.12       # the width of the bars


fig, ax = plt.subplots()

rects1 = ax.bar(ind, result_pandas.loc[2012], width, label='2012')

rects2 = ax.bar(ind + width, result_pandas.loc[2013], width, label='2013')

rects3 = ax.bar(ind + 2*width, result_pandas.loc[2014], width, label='2014')

rects4 = ax.bar(ind + 3*width, result_pandas.loc[2015], width, label='2015')

rects5 = ax.bar(ind + 4*width, result_pandas.loc[2016], width, label='2016')

# rects6 = ax.bar(ind + 5*width, result_pandas.loc[2017], width, label='2017')



# add some text for labels, title and axes ticks
ax.set_ylabel('DN')
ax.set_xlabel('buffer')
# ax.set_title('Scores by group and gender')


ax.set_xticks(ind)
ax.set_xticklabels(distance)
ax.legend()
# ax.set_xticklabels(('2-10Km radius', '10-20Km radius', '20-50Km radius', '50-100Km radius', '100-200Km radius'))

# ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                 '%d' % int(height),
#                 ha='center', va='bottom')
#
# autolabel(rects1)
# autolabel(rects2)

plt.show()