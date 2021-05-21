'''
Matplotlib - Labels
'''

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as pl

x = np.array([0,3,4,6,8,10])
y = np.array([0,5,3,7,10,12])

pl.plot(x,y, marker = 'o', mfc = 'red')
pl.title("This is title")
pl.xlabel("lebel x", c = 'red')
pl.ylabel("label y", c = 'yellow')
pl.show()