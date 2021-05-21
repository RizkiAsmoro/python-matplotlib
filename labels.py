'''
Matplotlib - Labels
'''

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as pl

x = np.array([0,3,4,6,8,10])
y = np.array([0,5,3,7,10,12])

pl.plot(x,y, marker = 'o', mfc = 'red')
pl.title("This is title", loc = 'left') # loc for positioning the title, the dafault is center
pl.xlabel("lebel x", c = 'red') #another attribute can be added
pl.ylabel("label y", c = 'yellow') #another attribute can be added
pl.grid() #adding grid (grid can be specify line x or y)
pl.show()

pl.plot(x,y, marker = 'o', mfc = 'red')
pl.title("This is title", loc = 'left') # loc for positioning the title, the dafault is center
pl.xlabel("lebel x", c = 'red') #another attribute can be added
pl.ylabel("label y", c = 'yellow') #another attribute can be added
pl.grid(axis= 'y') #adding grid (grid can be specify line x or y)
pl.show()