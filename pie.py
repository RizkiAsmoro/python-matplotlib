'''
Pie Chart
'''
import matplotlib.pyplot as pl
import numpy as np

x = np.array([35,15,20,20,10])
xlabels = ["ronaldo","neymar","messi","mbape","haland"]

pl.pie(x, labels = xlabels )
pl.show()
