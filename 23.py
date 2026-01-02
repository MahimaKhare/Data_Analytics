import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,2,4,6])
y = np.array([8,10,12,14])

#Markers
plt.plot(x,y,marker = 'o')
plt.show()

# Star
plt.plot(x,y,marker = '*')
plt.show()

#point
plt.plot(x,y, marker = '.')
plt.show()

#pixel
plt.plot(x,y, marker = ',')
plt.show()

#cross
plt.plot(x,y, marker = 'x')
plt.show()

#x filled
plt.plot(x,y, marker = 'X')
plt.show()

#plus
plt.plot(x,y, marker = '+')
plt.show()

#plus filled
plt.plot(x,y, marker = 'P')
plt.show()

#Hexagon
plt.plot(x,y, marker = 'H')
plt.show()

# Hexagon
plt.plot(x,y, marker = 'h')
plt.show()

#Square
plt.plot(x,y, marker = 's')
plt.show()

#
#point
plt.plot(x,y, marker = '.')
plt.show()

#pixel
plt.plot(x,y, marker = ',')
plt.show()

#cross
plt.plot(x,y, marker = 'x')
plt.show()

#Dimond
plt.plot(x,y, marker = 'd')
plt.show()

#Dimond Filled
plt.plot(x,y, marker = 'D')
plt.show()

#pentagon
plt.plot(x,y, marker = 'P')
plt.show()

#Triangle up
plt.plot(x,y, marker = '^')
plt.show()

#Triangle down
plt.plot(x,y, marker = 'v')
plt.show()

#Triangle left
plt.plot(x,y, marker = '<')
plt.show()

#Triangle right
plt.plot(x,y, marker = '>')
plt.show()

#Triangle Down
plt.plot(x,y, marker = '1')
plt.show()

#Triangle Up
plt.plot(x,y, marker = '2')
plt.show()

#Triangle left
plt.plot(x,y, marker = '3')
plt.show()

#Triangle right
plt.plot(x,y, marker = '4')
plt.show()

# vartical line
plt.plot(x,y, marker = '|')
plt.show()

#Format string
plt.plot(x,y, 'o:y')
plt.show()

#solid line
plt.plot(x,y, '*-r')
plt.show()

#dashed line
plt.plot(x,y, '.--b')
plt.show()

#dashed dotted
plt.plot(x,y, '+-.g')
plt.show()

#Increasing marker size
plt.plot(x,y, marker = '*', ms = 20)
plt.show()

# marker border color
plt.plot(x,y, marker = '*', ms = 20, mec = 'r')
plt.show()

#marker face color
plt.plot(x,y, marker = '*', ms = 20, mec = 'r', mfc = 'b')
plt.show()

#line widht
plt.plot(x,y, '.--b', lw = 20)
plt.show()

# line style 
plt.plot(x,y, '.--b', ls = 'solid')
plt.show()

plt.plot(x,y, '.--b', ls = '-')
plt.show()

plt.plot(x,y, '.--b', ls = '-.')
plt.show()

#Line color 
plt.plot(x,y, '.--b', ls = '-', color = 'r')
plt.show()
