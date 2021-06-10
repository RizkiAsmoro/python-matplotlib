'''
Pie Chart
'''
import matplotlib.pyplot as pl
import numpy as np

x = np.array([35,15,20,20,10])
xlabels = ["ronaldo","neymar","messi","mbape","haland"]
xexplode = [0.2,0.1,0,0,0] #explode one of wedges from the center 
xcolors = ['pink','b','r','g','y'] #coloring the wedges

pl.pie(x, labels = xlabels, explode = xexplode, colors=xcolors)
pl.legend(title="Players") #add list explanation
pl.show()
