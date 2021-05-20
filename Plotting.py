'''
Matplotlib
Plotting - Basic Pyplot

'''
#Plotting using x and y points
import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0,5,7,12,15,20])
ypoint = np.array([0,7,6,13,10,17])

plt.plot(xpoint, ypoint)
plt.show()


#plotting without line
xp = np.array([0,5,7,12,15,20])
yp = np.array([0,7,6,13,10,17])

plt.plot(xp, yp,'o')
plt.show()

#using only 1 plot
xa = np.array([0,7,6,13,10,17])

plt.plot(xa)
plt.show()

#plotting 2 lines
x1 = np.array([0,5,7,12,15,20])
x2 = np.array([0,7,6,13,10,17])

plt.plot(x1)
plt.plot(x2)
plt.show()


