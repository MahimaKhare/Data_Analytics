import time
lst = list(range(1_000_000))
start = time.time()
[x*2 for x in lst]
print(time.time()-start)

#
import numpy as np 
arr = np.arange(1_000_000)
start = time.time()
arr*2
print(time.time()-start)

# numpy array
#creating an array
import numpy as np 
x = np.array([1,2,3,4,5,6])
print(x)

# Multi_dimensional array
y =  np.array([[1,2,3],[4,5,6]])
print(y)

#Zero Matrix
print(np.zeros((2,3)))

#Ones Matrix
print(np.ones((2,3)))

#full matrix
print(np.full((2,2),7))

#identity matrix
print(np.eye(3))

#Arange
print(np.arange(2,12,2))

#Linspace
print(np.linspace(0,1,5))

#Random number matrix
print(np.random.randint(1,50,(3,3)))

#
arr = np.array([[1,2,3],[4,5,6]])
#shape of array
print(arr.shape)

#size of array
print(arr.size)

#dimensions number
print(arr.ndim)

#type of array
print(arr.dtype)

#type conversion
arr = np.array([1,2,3],dtype=float)
print(arr)
print(arr.dtype)

#Airthmetic operation
print(arr+5)
print(arr-5)
print(arr*2)
print(arr/2)
print(arr**2)

#Comparision or logical operator
arr_3 = np.array([10,20,30,40,50])
print(arr_3 > 25)
print(arr == 25)

#Question

#Q.1. Create an array of number 1 to 20 using np.arange()

a = np.arange(1,21,)
print(a)

#shape of array
print(a.shape)

#size of array
print(a.size)

#datatype
print(a.dtype)

#Q.2. 3X3 random number 10 to 50 maximum minimum mean
b = np.random.randint(1,51,(3,3))
print(b)

#maximum number
print(b.max())

#minimum number
print(b.min())

#mean number
print(b.mean())

