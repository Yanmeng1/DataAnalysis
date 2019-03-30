import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#指定默认字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.sans-serif'] = ['Microsoft Yahei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

''' 1. 导入数据 '''
simulation = pd.read_csv(open(r'../data/abm_farmer/simulations.csv'))
sim = simulation[['id','mu','learn','sense','radius']]
country = pd.read_csv(r'../data/abm_farmer/country_traces.csv')

''' 2. 清洗数据：根据关键字段连接DataFrame，构造要用的DataFrame '''
country['time'] = country['time'].apply(lambda x: x.split('-')[0])
simCountry = pd.merge(sim, country, how='right', left_on='id', right_on='sim_id')

''' 3. 构造一个子图显示 axes '''
def showLine(ax, data, paraName, paraLabel, paraList, style, xyLabel=[r'年 份',r'收益($10^6$元)']):
    '''
    display data to axes
    :param ax: axes
    :param data: DataFrame
    :param paraName: DataFrame column name
    :param paraLabel: line label
    :param paraList: DataFrame rows, n = len(rows), n means n lines
    :param style: list - lineStyle
    :param xyLabel:
    :return:
    '''
    scale = 1e6
    ax.set(xlabel=xyLabel[0], ylabel=xyLabel[1])
    for m,s in zip(paraList, style):
        tempParaData = data[abs(data[paraName] - m) < 0.001]
        tempX =tempParaData['time'].map(lambda x: int(x)).values
        tempY = tempParaData['crop_income'].values / scale
        ax.plot(tempX, tempY, s, linewidth=1.6, markersize=4, label= paraLabel + str(m))

''' 4. 在figure对象上显示各个axes '''
# 刻度设置
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
def setTicks(ax):
    xMajorLocator = MultipleLocator(2)          # 将x主刻度标签设置为2的倍数
    xMinorLocator = MultipleLocator(1)          # 将x轴次刻度标签设置为1的倍数
    xMajorFormatter = FormatStrFormatter('%d')  # 设置x轴标签文本的格式
    ax.xaxis.set_major_locator(xMajorLocator)
    ax.xaxis.set_major_formatter(xMajorFormatter)
    ax.xaxis.set_minor_locator(xMinorLocator)
    ax.set_xticklabels(np.arange(2004, 2017, 2))  # 要将所显示的刻度包在其中
#     yMajorLocator   = MultipleLocator(5000000)
#     yMinorLocator   = MultipleLocator(2500000)
#     yMajorFormatter = FormatStrFormatter('%8.1f')
#     ax.yaxis.set_major_locator(yMajorLocator)
#     ax.yaxis.set_major_formatter(yMajorFormatter)
#     ax.yaxis.set_minor_locator(yMinorLocator)
#     ax.axis([2006, 2017, 1800000, 4500000])
#     ax.set_xlim(2005, 2016)
#     ax.set_ylim(1800000, 4500000)
#     ax.set_xticks(np.arange(2005,2016,2))
#     ax.set_xticklabels(np.arange(2005,2016.01,2))
#     ax.set(xlabel=xyLabel[0], ylabel=xyLabel[1])


def displayMu():
    muList = [0.3, 0.5, 0.7]
    muStyle = ['r^--','g+-','bo:']
    se = [0.4, 0.8]
    le = [0.4, 0.8]
    ra = [3, 9]
    plt.close('all')
    fig, axArray = plt.subplots(2, 4, figsize=[14, 6], sharex=True, sharey=True)
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.35)
    axList = axArray.flat
    axNo = [chr(i) for i in range(97, 97+len(axList), 1)]
    axNum = 0
    for s in se:
        for l in le:
            for r in ra:
                ax = axList[axNum]
                no = axNo[axNum]
                axNum += 1
                condition = (simCountry['sense'] == s) & (simCountry['learn'] == l) & (simCountry['radius'] == r)
                data = simCountry[condition]
                showLine(ax, data, paraName='mu', paraLabel=r'$\mu=$', paraList=muList, style=muStyle)
                titleNum = '( ' + no + ' )\n'
                ax.set_title(titleNum + r'$\alpha$=' + str(s) + r', $\beta$=' + str(l) + r', $\gamma$=' + str(r))
                setTicks(ax)
    axArray[0, 0].legend(loc='best')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axArray.flat:
        ax.label_outer()
    plt.show()


def disPlayAlpha():
    senseList = [0.2, 0.4, 0.6, 0.8]
    senseStyle = ['r^:', 'g+-', 'ms-.', 'bo--']
    le = [0.4, 0.8]
    ra = [3, 9]
    accuracy = 0.01
    plt.close('all')
    fig, axesArray = plt.subplots(2, 2, figsize=[9.8, 7], sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0.37)

    axesList = axesArray.flat
    axesNum = 0
    axNo = [chr(i) for i in range(97, 97 + len(axesList), 1)]
    for l in le:
        for r in ra:
            ax = axesList[axesNum]
            no = axNo[axesNum]
            axesNum += 1
            condition = (abs(simCountry['learn'] - l) < accuracy) & \
                        (abs(simCountry['radius'] - r) < accuracy) & \
                        (abs(simCountry['mu'] - 0.5) < accuracy)
            data = simCountry[condition]
            showLine(ax, data, paraName='sense', paraLabel=r'$\alpha=$', paraList=senseList, style=senseStyle)
            titleNum = '( ' + no + ' )\n'
            ax.set_title(titleNum + r'$\beta$=' + str(l) + r', $\gamma$=' + str(r))

    axesArray[0, 0].legend(loc='best')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axesArray.flat:
        ax.label_outer()
    plt.show()


def disPlayBeta():
    learnList = [0.2, 0.4, 0.6, 0.8]
    learnStyle = ['r^:', 'g+-', 'ms-.', 'bo--']
    se = [0.4, 0.8]
    ra = [3, 9]
    accuracy = 0.01
    plt.close('all')
    fig, axesArray = plt.subplots(2, 2, figsize=[9.8, 7], sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0.37)

    axesList = axesArray.flat
    axesNum = 0
    axNo = [chr(i) for i in range(97, 97 + len(axesList), 1)]
    for s in se:
        for r in ra:
            ax = axesList[axesNum]
            no = axNo[axesNum]
            axesNum += 1
            condition = (abs(simCountry['sense'] - s) < accuracy) & \
                        (abs(simCountry['radius'] - r) < accuracy) & \
                        (abs(simCountry['mu'] - 0.5) < accuracy)
            data = simCountry[condition]
            showLine(ax, data, paraName='learn', paraLabel=r'$\beta=$', paraList=learnList, style=learnStyle)
            titleNum = '( ' + no + ' )\n'
            ax.set_title(titleNum + r'$\alpha$=' + str(s) + r', $\gamma$=' + str(r))

    axesArray[0, 0].legend(loc='best')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axesArray.flat:
        ax.label_outer()
    plt.show()


def disPlayGamma():
    radiusList = [3,7,11]
    radiusStyle = ['r^:', 'g+-', 'bo--']
    se = [0.4, 0.8]
    le = [0.4, 0.8]
    accuracy = 0.01
    plt.close('all')
    fig, axesArray = plt.subplots(2, 2, figsize=[9.8, 7], sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0.37)

    axesList = axesArray.flat
    axesNum = 0
    axNo = [chr(i) for i in range(97, 97 + len(axesList), 1)]
    for s in se:
        for l in le:
            ax = axesList[axesNum]
            no = axNo[axesNum]
            axesNum += 1
            condition = (abs(simCountry['sense'] - s) < accuracy) & \
                        (abs(simCountry['learn'] - l) < accuracy) & \
                        (abs(simCountry['mu'] - 0.5) < accuracy)
            data = simCountry[condition]
            showLine(ax, data, paraName='radius', paraLabel=r'$\gamma=$', paraList=radiusList, style=radiusStyle)
            titleNum = '( ' + no + ' )\n'
            ax.set_title(titleNum + r'$\alpha$='+ str(s) + r', $\beta$=' + str(l))

    axesArray[0, 0].legend(loc='best')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axesArray.flat:
        ax.label_outer()
    plt.show()

if __name__ == '__main__':
    disPlayGamma()
