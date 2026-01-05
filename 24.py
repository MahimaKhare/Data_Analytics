import matplotlib.pyplot as plt
import numpy as np 

x = np.array([1,2,3,4,5,6])
y = np.array([7,8,9,10,11,12])

#Lable
plt.plot(x,y,'o')
plt.xlabel("Age")
plt.ylabel("BP")
plt.show()

#Title
plt.plot(x,y,'o')
plt.title("Chart")
plt.show()

#Font
plt.plot(x,y,'o')
Font1 = {'family':'Serif','color':'red','size':20}
Font2 = {'family':'cursive','color':'Green','size':25}
plt.xlabel("Age",fontdict = Font1)
plt.ylabel("BP",fontdict=Font1)
plt.title("Chart",fontdict=Font2)
plt.show()

#Grid
plt.plot(x,y,'o')
plt.grid(color='green',linestyle = '--',linewidth = 0.5)
plt.show()

#subplot
x = [0,1,2,3]
y = [3,8,1,10]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Chart-1")

x =[0,1,2,3]
y = [10,20,30,40]

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Chart-2")

plt.suptitle("Subplots")

plt.show()

#example
x = [0,1,2,3]
y = [3,8,1,10]

plt.subplot(2,1,1)
plt.plot(x,y)
plt.title("Chart-1")

x =[0,1,2,3]
y = [10,20,30,40]

plt.subplot(2,1,2)
plt.plot(x,y)
plt.title("Chart-2")

plt.suptitle("Subplots")

plt.show()

#example 
x = [0,1,2,3]
y = [3,8,1,10]

plt.subplot(3,3,1)
plt.plot(x,y)
plt.title("Chart-1")

x =[1,2,3,4,5,6]
y = [10,20,30,40,50,60]

plt.subplot(3,3,2)
plt.plot(x,y)
plt.title("Chart-2")

x =[0,1,2,4,6,8]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-3")

x=[0,1,2,4,9,6]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-4")

x=[0,1,2,4,9,6]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-5")

x=[0,1,2,4,9,6]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-6")

x=[0,1,2,4,9,6]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-7")

x=[0,1,2,4,9,6]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-8")

x=[0,1,2,4,9,6]
y = [10,20,30,40,60,80]

plt.subplot(3,3,3)
plt.plot(x,y)
plt.title("Chart-9")

plt.suptitle("Subplots")

plt.show()