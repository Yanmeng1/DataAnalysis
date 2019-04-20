import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft Yahei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

''' 1. 导入数据 '''
simulation = pd.read_csv(open(r'../data/abm_farmer/simulations.csv'))
sim = simulation[['id','mu','learn','sense','radius']]
country = pd.read_csv(r'../data/abm_farmer/country_traces.csv')


''' 2. 清洗数据：根据关键字段连接DataFrame，构造要用的DataFrame'''
country['time'] = country['time'].apply(lambda x: int(x.split('-')[0]))
simCountry = pd.merge(sim, country, how='right', left_on='id', right_on='sim_id')

''' 3. 绘图'''
plt.close('all')
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def showIrrigation(hostAxes, data):
    scale12 = 1. * 1e5
    tempX = data['time'].values
    tempY1 = data['maize_irrigation'].values / scale12
    tempY2 = data['rice_irrigation'].values / scale12
    p1 = hostAxes.bar(tempX, tempY1, width=0.6, color='#996600')
    p2 = hostAxes.bar(tempX, tempY2, bottom=tempY1, width=0.6, color='#669999')
    hostAxes.set_xlabel(u"年 份")
    hostAxes.set_ylabel(u"灌溉量（$10^5m^3$）")
    hostAxes.set_ylim(0, 8)

    parasiteAx = hostAxes.twinx()
    # Offset the right spine of parasiteAx. The ticks and label have already been placed on the right by twinx above.
    parasiteAx.spines["right"].set_position(("axes", 1.02))
    # First, activate the frame but make the patch and spines invisible.
    make_patch_spines_invisible(parasiteAx)
    # Second, show the right spine(spine 边界的轴线，ticks位于轴线上).
    parasiteAx.spines["right"].set_visible(True)
    scale3 = 1. * 1e2
    tempY3 = data['precipitation'].values / scale3
    p3, = parasiteAx.plot(tempX, tempY3, color='#333366', marker='o', linestyle=':')
    parasiteAx.set_ylabel(u"降雨量 ($10^2$mm)")
    parasiteAx.set_ylim(-18, 15)
    # 设置刻度属性：刻度长短粗细，根据p3的值设置刻度颜色，标签颜色
    tkw = dict(size=4, width=1.5)
    parasiteAx.tick_params(axis='y', colors=p3.get_color(), **tkw)
    parasiteAx.yaxis.label.set_color(p3.get_color())

    hostAxes.legend((p1[0], p2[0], p3), (u"玉米", u"水稻", u"降雨"), loc='upper left', ncol=3)


fig, axesArray = plt.subplots(1, 2, figsize=[14, 4], sharey=True)
fig.suptitle(r'$\mu=0.5,\beta=0.8,\gamma=7$', fontsize=14)
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=None)

accuracy = 0.001
slowAgent = (abs(simCountry['sense'] - 0.8) < accuracy) & (abs(simCountry['mu'] - 0.5) < accuracy) & \
            (abs(simCountry['learn'] - 0.8) < accuracy) & (abs(simCountry['radius'] - 7) < accuracy)
showIrrigation(axesArray[0], simCountry[slowAgent])
axesArray[0].set_title('( a )\n'+r'迟钝型$(\alpha=0.8)$')


senseAgent = (abs(simCountry['sense'] - 0.4) < accuracy) & (abs(simCountry['mu'] - 0.5) < accuracy) & \
            (abs(simCountry['learn'] - 0.8) < accuracy) & (abs(simCountry['radius'] - 7) < accuracy)
showIrrigation(axesArray[1], simCountry[senseAgent])
axesArray[1].set_title('( b )\n' + r'敏感型$(\alpha=0.4)$')
plt.show()