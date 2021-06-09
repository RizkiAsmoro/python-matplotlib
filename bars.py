'''
Matplotlib - bars
'''


#vertical bars
import matplotlib.pyplot as pl
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,7,5,10])

pl.bar(x,y, color = "#4CAF50", width=0.2) # .barh() to draw horizontal bars 
pl.show()
