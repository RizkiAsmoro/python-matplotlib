'''
Matplotlib
Plotting - Basic Pyplot and subplots

'''
#Plotting using x and y points
import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0,5,7,12,15,20])
ypoint = np.array([0,7,6,13,10,17])
plt.subplot(2,2,1) # display has 2 row, 2 columns, and this plot is the first plot.
plt.plot(xpoint, ypoint)


#plotting without line
xp = np.array([0,5,7,12,15,20])
yp = np.array([0,7,6,13,10,17])
plt.subplot(2,2,2) # display has 2 row, 2 columns, and this plot is the second plot.
plt.plot(xp, yp,'o')

#using only 1 plot
xa = np.array([0,7,6,13,10,17])
plt.subplot(2,2,3) # display has 2 row, 2 columns, and this plot is the third plot.
plt.plot(xa)

#plotting 2 lines
x1 = np.array([0,5,7,12,15,20])
x2 = np.array([0,7,6,13,10,17])
plt.subplot(2,2,4) # display has 2 row, 2 columns, and this plot is the fourth plot.
plt.plot(x1)
plt.plot(x2)
plt.show()


