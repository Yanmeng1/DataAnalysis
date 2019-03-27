# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.cm import ScalarMappable
import matplotlib
fig, ax = plt.subplots()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# norm = mpl.colors.Normalize()
# norm = mpl.colors.Normalize(-5,5,clip=False)
# norm = mpl.colors.Normalize(1,5,clip=False)
# norm = mpl.colors.Normalize(0,5,clip=False)
norm = mpl.colors.Normalize(2,5,clip=True)
# norm = mpl.colors.Normalize(2,5,clip=False)


print('autoscale', norm.autoscale(data))



print ('scaled', norm.scaled())

sm = (ScalarMappable(norm=norm))
print (sm.get_clim())

print (sm.get_array())

print (sm.to_rgba(2))
print(sm.to_rgba(data))

print (norm.scaled())

print (sm.get_clim())

# print matplotlib.__version__
sm.set_array(data)

print (sm.get_array())