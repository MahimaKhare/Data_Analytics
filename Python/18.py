#Mathmetical and Statical operation
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#min from row and col
print(np.min(arr,axis=1))
print(np.min(arr,axis=0))

#max from row and col
print(np.max(arr,axis=1))
print(np.max(arr,axis=0))

#mean
print(np.mean(arr,axis=1))
print(np.mean(arr,axis=0))

#sum of row and col
ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar)

print(np.sum(ar,axis=0))
print(np.sum(ar,axis=1))

#Comulative function
#cumsum
print(np.cumsum(ar))

#cumprod
print(np.cumprod(ar))

#Rounding, floor, ceil
x = np.array([1.2437, 5.673256, 6.75355])
print(np.round(x,2))
print(np.floor(x))
print(np.ceil(x))

#concatenate
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print(b)

#Q.1Calculate maths avg num, S1's max, S4's min, avg num per student, avg num per subject
ar1 = np.array([45,78,56,67,82,90,85,65,70,34,55,60,76,88,97])
array = ar1.reshape(5,3)
print(array)

#maths avg number
y = (np.mean(array, axis = 0))
print("Maths_avg:",y[0])

#s1 max
z = (np.max(array,axis=1))
print("S1_max:",z[0])

#s4 min
e = (np.min(array,axis=1))
print("S4_min:",e[3])

#avg num per std
s = (np.mean(array, axis = 1))
print("S1:",s[0])
print("S2:",s[1])
print("S3:",s[2])
print("S4:",s[3])
print("S5:",s[4])

#avg num per subeject
avg = (np.mean(array, axis=0))
print("maths:",avg[0])
print("English:",avg[1])
print("Hindi:",avg[2])