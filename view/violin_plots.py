
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft Yahei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

import numpy as np

sns.set()
# Create a random dataset across several variables
rs = np.random.RandomState(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10

# Use cubehelix to get a custom sequential palette
pal = sns.cubehelix_palette(p, rot=-.5, dark=.3)

print(len(d))

# Show each distribution with both violins and points

# Load the example tips dataset
tips = sns.load_dataset("tips")
print(tips)
g = sns.catplot(x="day", y="total_bill", kind="violin", inner="points", data=tips)
# sns.catplot(x="day", y="total_bill", kind="swarm", color="k", size=1, data=tips, ax=g.ax);
plt.show()


import numpy as np
import seaborn as sns

sns.set()

# Create a random dataset across several variables
rs = np.random.RandomState(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10

# Use cubehelix to get a custom sequential palette
pal = sns.cubehelix_palette(p, rot=-.2, dark=.7)

# Show each distribution with both violins and points
sns.violinplot(data=d, palette=pal, inner="points")

f, axarr = plt.subplots(3, 3, sharex='col', sharey='row')
