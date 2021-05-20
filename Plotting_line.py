'''
Matplotlib line

Using linestyle or ls
'''
import matplotlib.pyplot as plt
import numpy as np

#line can be solid can be -
#line can be dotted can be :
#line can be dashed can be --
#line can be dashdot can be -.
#line can be none can be 'or'

#two line using dash,dot, color, linewidth

y1 = np.array([0,7,6,13,10,17])
y2 = np.array([3,8,4,6,15,10])
plt.plot(y1, ls = '--', c = '#4CAF50', linewidth = 5)  
plt.plot(y2, ls = ':', c = 'hotpink', linewidth = 3)
plt.show()