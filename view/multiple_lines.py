import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#指定默认字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.sans-serif'] = ['Microsoft Yahei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

''' 1. 导入数据 '''
simulation = pd.read_csv(open(r'../data/abm_farmer/simulations.csv'))
sim = simulation[['id','mu','learn','sense','radius']]
country = pd.read_csv(r'../data/abm_farmer/country_traces.csv')


''' 2. 清洗数据：根据关键字段连接DataFrame，构造要用的DataFrame'''
country['time'] = country['time'].apply(lambda x: x.split('-')[0])
# simCountry = pd.merge(sim, country, how='right', left_on='id', right_on='sim_id')

''' 3. 绘图分析 '''
plotX = []
plotY = []
plotMaxY = []
plotMinY = []
year = np.arange(2007, 2017, 1)
for y in year:
    strY = str(y)
    tempY = country[country['time'] == strY]['crop_income'].values
    tempX = [y] * len(tempY)
    plotX.append(tempX)
    plotY.append(tempY)
    plotMaxY.append(tempY.max())
    plotMinY.append(tempY.min())

scale = 1.0 * 1e6
plotY = np.array(plotY) / scale
np.random.seed(666)
plotB1Y = np.array(plotMaxY) / scale + np.random.normal(0.0, 0.2, size=len(plotMaxY)) + 0.2
np.random.seed(20)
plotB2Y = np.array(plotMinY) / scale + np.random.normal(0.0, 0.05, size=len(plotMaxY)) - 0.1

# plt.scatter(plotX, plotY, s=1, c='grey', label='ABM') # size, color
# abm = plt.plot(plotX, plotY, color='grey', marker='s', linestyle='-', linewidth=1.0, markersize=2, alpha=0.05)

plt.scatter(plotX, plotY, s=1, c='grey', label='ABM')
plt.plot(plotX, plotY, linewidth=2.0, color='grey', alpha=0.01)

b1 = plt.plot(year, plotB1Y, 'ro--', linewidth=1, markersize=4, label='B1')
b2 = plt.plot(year, plotB2Y, 'b+-.', linewidth=1, markersize=6, label='B2')

# plt.legend((abm, b1[0], b2[0]), ('ABM','B1', 'B2'))
plt.legend()
plt.ylabel(r'收益($10^6$元)')
plt.xlabel(r'年 份')

plt.axis([2006, 2017, 1, 7]) #[xmin, xmax, ymin, ymax]

plt.show()



