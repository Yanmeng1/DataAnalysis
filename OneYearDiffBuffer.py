import numpy as np
import matplotlib.pyplot as plt
import xlrd
import pandas as pd

def tolistByName( path, sheet_name ):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows
    list_rows = []
    for row in range(0, nrows):
        row_values = table.row_values(row)
        list_rows.append(row_values)
    return list_rows

def convertToDataFrame(lsit2D):
    list_2d = list(lsit2D)
    index = []
    for row in range(1,list_2d.__len__()):
        rowValues = list_2d[row]
        index.append(rowValues[0])
    df = pd.DataFrame(list_2d[1:], index=index, columns=list_2d[0])
    return df


year = 2012
path = "/Users/yanmeng/Downloads/lightdata/TBData20180104.xlsx"
list_2d = tolistByName(path, "y"+str(2012))
df = convertToDataFrame(list_2d)

t = np.arange(0,2280,1)
buffers = [5,10,20,50,100,200]
# names = []
values = []
for b in buffers:
    columnName = "ntl"+str(2012)+"d"+str(b)
    # names.append(columnName)
    values.append(df[columnName])

# print(values)
# print(names)
# print(values)
# exit(0)

fig, ax = plt.subplots()
ax.set_title('Year : '+str(2012)+'')
lines = []
for i in range(0, len(buffers)):
    columnName = "ntl" + str(2012) + "d" + str(buffers[i])
    lines[i] = ax.plot(t, df[columnName], lw=1, label=columnName)

leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.9)


# we will set up a dict mapping legend line to orig line, and enable
# picking on the legend line
lined = dict()
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(5)  # 5 pts tolerance
    lined[legline] = origline


def onpick(event):
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
    legline = event.artist
    origline = lined[legline]
    vis = not origline.get_visible()
    origline.set_visible(vis)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()