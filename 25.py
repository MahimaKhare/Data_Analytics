import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

#scatter
plt.scatter(x,y)
plt.show()

#compare plot
x = np.array([1,2,3])
y = np.array([4,5,6])
plt.scatter(x,y)

x = np.array([1,2,3])
y = np.array([7,8,9])
plt.scatter(x,y)

plt.show()

#Color change
plt.scatter(x,y,color='green')
plt.show()

#
color =["red","green","yellow"]
plt.scatter(x,y,c = color)
plt.show()

#Size
size =[20,10,40]
plt.scatter(x,y,c = color,s = size )
plt.show()

#alpha
plt.scatter(x,y,alpha=1)
plt.show()

#bars
x =['a','b','c','d']
y =[70,80,90,60]
plt.bar(x,y,width=0.3)
plt.show()

#barh
x =['a','b','c','d']
y =[70,80,90,60]
plt.barh(x,y,height=0.3,color = color)
plt.show()

#histogram
x = np.random.normal(100,10,10)
plt.hist(x)
plt.show()

#Pie
y =[35,25,25,15]
plt.pie(y)
plt.show()

#Label
l = ['Apple','Banana','Mango','Grapes']
plt.pie(y,labels= l )
plt.show()

#startangle
plt.pie(y,labels= l,startangle=100)
plt.show()

#explode
e =[0.1,0.1,0.1,0.1]
plt.pie(y,labels= l,explode=e)
plt.show()

#shadow
plt.pie(y,labels= l,explode=e,shadow=True)
plt.show()

#legend
plt.pie(y,labels= l,explode=e,shadow=True)
plt.legend(title = "fruits")
plt.show()


