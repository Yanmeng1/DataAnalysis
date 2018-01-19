from dbfread import DBF
import pandas as pd

root_path = '/Users/yanmeng/Downloads/connection/tabledataPro/table'

absent_id = []

def process(year, length):
    path = root_path+str(year)+'_s'+str(length)+'.dbf'
    table = DBF(path)
    fid = []
    sum = []

    for record in table:
        fid.append(record['FID_'])
        sum.append(record['SUM'])
    series = pd.Series(sum, index=fid)
    series.name = 'NTL'+str(year)+'D'+str(length)+'Y'+str(year)
    for id in range(2279):
        if id not in series.index:
            if id not in absent_id:
                absent_id.append(id)
            series[id] = -1
    series.sort_index


    return series
# print(process(12,5)[2278])

print()


def main(years, lenghts):
    list_series = []
    for year in years:
        for lenght in lenghts:
            list_series.append(process(year, lenght))

    result = pd.DataFrame(list_series)
    last = result.T
    # last.to_csv('/Users/yanmeng/Downloads/connection/result.csv')


    print(last)

maxrow = 2279
years = [12,13,14,15,16]
lengths = [5,10,20,50,100,200]

year_length=[]
for year in years:
    for length in lengths:
        year_length.append(['NTL'+str(year)+'D'+str(length)+'Y'+str(year)])
# print(year_length)

main([12], lengths)
absent_id_seriese = pd.Series(absent_id)
absent_id_seriese.name='absent_id'
absent_id_seriese.to_csv('/Users/yanmeng/Downloads/connection/absent_id.csv')
absent_id_seriese.to_csv()



