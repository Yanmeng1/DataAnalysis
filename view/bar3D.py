import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import



# setup the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = 0.6
depth = 0.6


for xx, yy, zz, dz in zip(x, y, bottom, top):
    color = np.random.random(3)
    ax1.bar3d(xx, yy, zz, width, depth, dz, color=color, shade=True)

# ax11 = ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Shaded')

ax2.bar3d(x, y, bottom, width, depth, top, shade=False, zsort='average')
ax2.set_title('Not Shaded')

plt.show()
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
ListedColormap()


y_ticks=ax1.set_yticks([-80,-60,-40,-20,0])
y_labels=ax1.set_yticklabels(["one","two","three","four","five"])

import math
math.floor( x )