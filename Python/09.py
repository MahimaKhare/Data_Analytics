#List functions

#insert()
a = ["ravi","ramesh","suresh","riya"]
a.insert(2,"priya")
print(a)

#append
fruits = ["Mango","Apple","Grapes"]
fruits.append("Papaya")
print(fruits)

#Update value
x = ["ravi","ramesh","suresh","riya"]
x[2] = "Mahesh"
print(x)

#extend()
a = ["ravi","ramesh","suresh","riya"]
fruits = ["Mango","Apple","Grapes",]
a.extend(fruits)
print(a)

#pop()
a = ["ravi","ramesh","suresh","riya"]
a.pop()
print(a)

#remove()
a = ["ravi","ramesh","suresh","riya"]
a.remove("ravi")
print(a)

#clear()
a = ["ravi","ramesh","suresh","riya"]
a.clear()
print(a)

#01 list with loop
my_list = ["Mango","Grapes","Apple","Banana","Orange"]
for i in my_list:
    print(i)

#2.
list=[]
while True:
    if len(list) == 5:
        break
    else:
        x = int(input("enter a number"))
        list.append(x)
print(list)   

#03. Print all the even numbers from the list
num = []
for i in range(1,51):
    if i % 2 == 0:
        num.append(i)
print(num) 

#04.add 10 to every elments in list
x = [5,10,15,20,25,30]
for i in range(0,len(x)):
    x[i]= x[i]+10
print(x)    

#05.add 10 to even numbers and add 5 to odd numbers
y = [5,10,15,20,25,30]
for i in range(0, len(y)):
    if y[i] % 2 == 0:
        y[i] = y[i] + 10
    else:
        y[i] = y[i] + 5  
print(y)          
