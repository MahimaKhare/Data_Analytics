import numpy as np

#stacking array
a = np.array([1,2,3])
print(a)
b= np.array([4,5,6])
print(b)

print(np.vstack((a,b)))

x = np.array([[1],[2],[3]])
y = np.array([[4],[5],[6]])
print(x)
print(y)
print(np.hstack((x,y)))


#np.stack
print(np.stack((a,b),axis = 0))
print(np.stack((a,b),axis = 1))

#Spliting array
arr = np.array([1,2,3,4,5,6,7,8])
print(np.split(arr,4))

#Append, Insert 
print(np.append(a,[4,5]))

print(np.insert(arr,2,25))

#delete
arrr = np.array([10,20,30,40])
e = np.delete(arrr,2)
print(e)

#Broad Casting
n = 5
print(a+n)

d = np.array([[1,2,3],[4,5,6]])
m = np.array([10,20,30])
print(d+m)

#np.any
arr1 = np.array([10,20,30,0,70])
print(np.any(arr1))

arr2 = np.array([0,0,0,0])
print(np.any(arr2))

#np.all
print(np.all(arr1))

arr3 = np.array([1,2,3,4,5])
print(np.all(arr3))

#Clip
array = ([10,20,30,40,50,60])
print(np.clip(array,20,50))

#Sort
r = np.array([3,8,6,4,9,1,5])
print(np.sort(r))

f = np.array([[3,1,2],[5,6,4]])
print(np.sort(f,axis=1))