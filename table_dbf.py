from __future__ import print_function
from dbfread import DBF
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker

years = range(2012,2018,1)
def main():
    sum_values = []
    count_values = []
    for year in years:
        file_name = "/Users/yanmeng/Downloads/sum_China/zone_statistic_"+str(year)+"_table.dbf"
        sum = 0
        count = 0
        table = DBF(file_name)
        table
        for record in table.records:
            count += record['COUNT']
            sum += record['SUM']

        sum /= 1
        sum_values.append(sum)
        count_values.append(count)
    print("sum :" +str(sum_values))
    print("count :" +str(count_values))
 

    # first we'll do it the default way, with gaps on weekends
    fig, axes = plt.subplots(ncols=2, figsize=(8, 3))
    ax = axes[0]
    ax.set_ylim([1, 40000000])
    ax.plot(years, sum_values, 'o-')

    ax.set_title("Sum DN values of China")

    # ax = axes[1]
    # ax.plot(years, count_values, 'o-')
    # ax.set_ylim([0,10000000])
    # ax.set_title("The total number of lit pixels")

    plt.show()

main()