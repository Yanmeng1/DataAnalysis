import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft Yahei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

simulation = pd.read_csv(open(r'../data/abm_farmer/simulations.csv'))
sim = simulation[['id','mu','learn','sense','radius']]
country = pd.read_csv(r'../data/abm_farmer/country_traces.csv')
country['time'] = country['time'].apply(lambda x: int(x.split('-')[0]))
simCountry = pd.merge(sim, country, how='right', left_on='id', right_on='sim_id')


def plot3DBar(axes, filteredData, xyDict={'sense': [0.2, 0.4, 0.6, 0.8], 'learn': [0.2, 0.4, 0.6, 0.8]},
              dx=0.12, dy=0.12, zMinMax=[0, 1], title='tile', labels=['xLabel', 'yLabel', 'xLabel'],
              colorAxis='x', colorInverse=False):
    '''
        ax:  the current axes to plot
        filteredData: data
        xyDict: x axis and y axis
        dx: width
        dy: depth
        zMinMax: there are a lot of axes to plot in a figure, get the range of the z axis to make the z ticks same scale
        colorAxis: color gradient with which axis
        colorInverse: bool to present different direction
    '''
    keys = list(xyDict.keys())
    values = list(xyDict.values())
    xName = keys[0]
    yName = keys[1]
    xx, yy = np.meshgrid(values[0], values[1])
    xFlat, yFlat = xx.ravel(), yy.ravel()
    zFlat = np.zeros_like(xFlat)
    #     zFlat = np.full(xFlat.shape, -0.5)

    scale = 1e6
    zMin = zMinMax[0] / scale
    zMax = zMinMax[1] / scale

    viridisBig = cm.get_cmap('viridis', 512)                            # 将viridis色域分为512段
    newColorMap = ListedColormap(viridisBig(np.linspace(0.4, 1, 256)))  # 取出viridisBig中0.4~1段

    for x, y, z in zip(xFlat, yFlat, zFlat):
        cdt = (abs(filteredData[xName] - x) < 0.01) & (abs(filteredData[yName] - y) < 0.01)
        zData = filteredData[cdt]['crop_income']
        #         dz = data['crop_income'].values[0] / scale - zMin

        zMinWeight = 0.7
        dz = (zData.values[0] / scale) - (zMin * zMinWeight)

        colorValue = 0
        if colorAxis == 'x':
            colorValue = (x - np.min(xFlat)) / (np.max(xFlat) - np.min(xFlat))
        elif colorAxis == 'y':
            colorValue = (y - np.min(yFlat)) / (np.max(yFlat) - np.min(yFlat))
        else:
            colorValue = (dz - zMin) / (zMax - zMin)
        if colorInverse:
            colorValue = 1 - colorValue
        color = newColorMap(colorValue)

        axes.bar3d(x, y, z, dx, dy, dz, color=color, shade=True, zsort=True)

        axes.set_zlim([0.0, 3.0])
        axes.set_xticks(values[0])
        axes.set_yticks(values[1])
        #         axes.set_zticks([0.0, 1.0, 2.0, 3.0])

        zticklabels = map(lambda a: ("%.1f" % (a + (zMin * zMinWeight))), axes.get_zticks())
        axes.set_zticklabels(zticklabels)

    axes.set_title(title)
    axes.set_xlabel(labels[0])
    axes.set_ylabel(labels[1])
    axes.set_zlabel(labels[2])

def subplots_3d(simCountry):
    filters = {'mu': 0.5, 'time': 2016}
    filterKeys = filters.keys()
    filterValues = filters.values()
    condition = True
    for key, value in zip(filterKeys, filterValues):
        condition = condition & (abs(simCountry[key] - value) < 0.001)
    simCountry = simCountry[condition]
    temp = simCountry['crop_income']
    zMin = np.min(temp)
    zMax = np.max(temp)

    plt.close('all')
    fig = plt.figure(figsize=(11.5, 9.5))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.15, hspace=0.20)
    axCount = 1
    axNo = [chr(i) for i in range(97, 97 + 9, 1)]

    ra = [3, 7, 11]
    xyDict = {'sense': [0.2, 0.4, 0.6, 0.8, 1.0], 'learn': [0.2, 0.4, 0.6, 0.8]}
    for r in ra:
        axes = fig.add_subplot(3, 3, axCount, projection='3d')
        axCount += 1
        tempData = simCountry[(abs(simCountry['radius'] - r) < 0.001)]
        titleNum = '( ' + axNo[axCount - 2] + ' ) '
        title = titleNum + r'$\gamma=$' + str(r)
        labels = [r'$\alpha$', r'$\beta$', r'收益($10^6$元)']
        plot3DBar(axes, filteredData=tempData, xyDict=xyDict, zMinMax=[zMin, zMax],
                  title=title, labels=labels, colorAxis='y', colorInverse=True)

    le = [0.2, 0.6, 0.8]
    xyDict = {'sense': [0.2, 0.4, 0.6, 0.8, 1.0], 'radius': [3, 5, 7, 9, 11]}
    for l in le:
        axes = fig.add_subplot(3, 3, axCount, projection='3d')
        axCount += 1
        tempData = simCountry[(abs(simCountry['learn'] - l) < 0.001)]
        titleNum = '( ' + axNo[axCount - 2] + ' ) '
        title = titleNum + r'$\beta=$' + str(l)
        labels = [r'$\alpha$', r'$\gamma$', r'收益($10^6$元)']
        plot3DBar(axes, filteredData=tempData, xyDict=xyDict, dy=1.2, zMinMax=[zMin, zMax],
                  title=title, labels=labels, colorAxis='x', colorInverse=False)

    se = [0.2, 0.6, 0.8]
    xyDict = {'radius': [3, 5, 7, 9, 11], 'learn': [0.2, 0.4, 0.6, 0.8]}
    for s in se:
        axes = fig.add_subplot(3, 3, axCount, projection='3d')
        axCount += 1
        tempData = simCountry[(abs(simCountry['sense'] - s) < 0.001)]
        titleNum = '( ' + axNo[axCount - 2] + ' ) '
        title = titleNum + r'$\alpha=$' + str(s)
        labels = [r'$\gamma$', r'$\beta$', r'收益($10^6$元)']
        plot3DBar(axes, filteredData=tempData, xyDict=xyDict, dx=1.2, zMinMax=[zMin, zMax],
                  title=title, labels=labels, colorAxis='y', colorInverse=True)

    plt.show()
    fig.savefig('subplots_3d.png', dpi=300)

if __name__ == '__main__':
    subplots_3d(simCountry)