import numpy as np
data = np.arange(1,13)
print(data)

#Reshape
print(data.reshape(3,4))

#auto dimension detection
print(data.reshape(2,-1))

#2d to 1d conversion
#flatten(), 
print(data.flatten())

#ravel(), it will change data in both array
print(data.ravel())

#Copy
x = [1,2,3,4,5,6]
print(x.copy())

#View
y = data.view()
y[0] = 10
print(y)


#Airthematic Operators
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,10,11,12])

#addition
print(a + b)

#Substract
print(a - b)

#Multiplication
print(a * b)

#Divide
print(a/b)

#Exponentiation 
print(a ** b)

#Mathematical Operators
y = np.array([1,4,9,16,5,10])

#square root
print(np.sqrt(y))

#
print(np.exp(y))

#log()
print(np.log(y))

#sin()
print(np.sin(y))

#cos()
print(np.cos(y))

#minimum value
print(np.min(y))

#maximum value
print(np.max(y))

#mean
print(np.mean(y))

#median
print(np.median(y))

#variance
print(np.var(y))

#std()
print(np.std(y))


#Q.1 create a array reshape it in 4*4 form than apply all the functions
arr = np.arange(1,17)
print(arr)

#reshape array
print(arr.reshape(4,4))

#2d to 1d conversion
print(arr.flatten())

#size
print(arr.size)

#shape
print(arr.shape)

#ndim
print(arr.ndim)

#data type
print(arr.dtype)

#sqrt
print(np.sqrt(arr))

#exp
print(np.exp(arr))

#log
print(np.log(arr))

#sin
print(np.sin(arr))

#cos
print(np.cos(arr))

#min
print(np.min(arr))

#max
print(np.max(arr))

#mean
print(np.mean(arr))

#median
print(np.median(arr))

#var
print(np.var(arr))

#std
print(np.std(arr))


#Q.2 square of an array than subtract by 10 than calculate mean,median,min,max
r = np.array([[10,20,30],[40,50,60]])

#square of each element
x1 = r**2
print(x1)

#substract by 10
sub = x1 - 10
print(sub)

#min
print(np.min(sub))

#max
print(np.max(sub))

#mean
print(np.mean(sub))

#median
print(np.median(sub))


#Q.3 create an array using using linspace than calculate min,mas,mean,meadian,var,std
n = np.linspace(1,501,100 , dtype=int)
print(n)

#min
print(np.min(n))

#max
print(np.max(n))

#mean
print(np.mean(n))

#median
print(np.median(n))

#var
print(np.var(n))

#std
print(np.std(n))
