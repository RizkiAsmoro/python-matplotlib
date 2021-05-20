'''
Matplotlib
Plotting Markers
Marker references :
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
'''
import matplotlib.pyplot as plt
import numpy as np

#Marker stars only 1 plot
yp = np.array([0,7,6,13,10,17])
plt.plot(yp, marker ="*") 
plt.show()

#plotting color and line
yp = np.array([0,7,6,13,10,17])
plt.plot(yp, 'o:r') 
plt.show()
'''
Line references:
'-'	 Solid line	
':'	 Dotted line	
'--' Dashed line	
'-.' Dashed/dotted line

Collor references:
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
'''

#marker size and color
# ms for the size, mfc(markerfacecolor), mec(markeredgecolor)
yp = np.array([0,7,6,13,10,17])
plt.plot(yp, marker = 'o', ms = 20, mfc = 'y', mec = 'r') 
plt.show()

