
import csv

import numpy as np

count = []
area = []
sum = []


with open(r'/Users/yanmeng/Downloads/123.csv') as f:
    datareader = csv.reader(f); # 将其读为新的
    header = next(datareader)
    for row in datareader:
        count.append(float(row[2]))
        area.append(float(row[3]))
        sum.append(float(row[4]))
# 用list构造Series
# countS = pd.Series(count)
# countS.name = header[2]
# countS.index.name = "索引名称"
# print(countS)

# 用dict构造DataFrame
dl = {header[2]:count,header[3]:area,header[4]:sum}
df = pd.DataFrame(dl)
print(df.describe())
print(df['AREA'].corr(df['SUM']))