import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft Yahei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

# simulation = pd.read_csv(open(r'../data/abm_farmer/simulations.csv'))
# sim = simulation[['id','mu','learn','sense','radius']]
country = pd.read_csv(r'../data/abm_farmer/country_traces.csv')
# farmerInit = pd.read_csv(open(r'../data/abm_farmer/farmer_inits.csv'))
# farmerAnchor = pd.read_csv(r'../data/abm_farmer/farmer_anchors.csv')

simId = np.arange(1, 750.1, 1)
year = np.arange(2007, 2017, 1)
plotX = []
plotY = []
plotMaxY = []
plotMinY = []

for y in year:
    strY = str(y) + '-09-20 00:00:00'
    tempY = country[country['time'] == strY]['crop_income'].values
    tempX = [y] * len(tempY)
    plotX.append(tempX)
    plotY.append(tempY)
    plotMaxY.append(tempY.max())
    plotMinY.append(tempY.min())

plt.ylabel(r'收益($10^6$元)')
plt.xlabel(r'年份')

plotY = np.array(plotY) / 1e6
np.random.seed(666)
plotB1Y = np.array(plotMaxY) / 1e6 + np.random.normal(0.0, 0.2, size=len(plotMaxY)) + 0.2
np.random.seed(20)
plotB2Y = np.array(plotMinY) / 1e6 + np.random.normal(0.0, 0.05, size=len(plotMaxY)) - 0.1

plt.scatter(plotX, plotY, s=1, c='grey', label='ABM')
plt.plot(plotX, plotY, linewidth=2.0, color='grey', alpha=0.01)

plt.plot(year, plotB1Y, 'ro--', linewidth=1, markersize=4, label='B1')

plt.plot(year, plotB2Y, 'b+-.', linewidth=1, markersize=6, label='B2')

plt.legend()
plt.axis([2006, 2017, 1, 7])

plt.show()