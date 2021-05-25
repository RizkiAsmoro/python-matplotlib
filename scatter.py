'''
Scatter
It needs two arrays of the same length, 
one for the values of the x-axis, 
and one for values on the y-axis:
'''
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size

#observstion in 13 cars passing 
#seems to be a relationship between speed and age
#the conclusion is the newer the car, the faster it drives.

#day1
xAge = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
ySpeed = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(xAge, ySpeed, s=sizes, alpha=0.5) 
#alpha for adjust transparancy
#s for adjust size dot

#day2
xAge = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7])
ySpeed = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.subplot(1,2,1)
plt.scatter(xAge, ySpeed, c=colors, cmap='viridis')
# set a specific color for each dot by using an array
# specify the colormap with the keyword argument cmap
plt.colorbar()


#combine random color and size
x = np.random.randint(50, size=(50)) #create random array value ,range to 50  for x-axis and size of dots 
y = np.random.randint(50, size=(50)) #create random array value ,range to 50  for y-axis and size of dots
color = np.random.randint(50, size=(50)) #create random array value ,range to 50  for for size
size = 5 * np.random.randint(50, size=(50))
plt.subplot(1,2,2)
plt.scatter(x,y, c=color, s=size, alpha=0.5, cmap="nipy_spectral")
plt.colorbar()
plt.show()