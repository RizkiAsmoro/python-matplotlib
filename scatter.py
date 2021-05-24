'''
Scatter
It needs two arrays of the same length, 
one for the values of the x-axis, 
and one for values on the y-axis:
'''
import matplotlib.pyplot as plt
import numpy as np

#observstion in 13 cars passing 
#seems to be a relationship between speed and age
#the conclusion is the newer the car, the faster it drives.

#day1
xAge = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
ySpeed = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(xAge,ySpeed, alpha=0.5) #alpha for adjust transparancy

#day2
xAge = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
ySpeed = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(xAge, ySpeed,color = '#88c999')


plt.colorbar()
plt.show()