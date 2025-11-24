#three ways to add two list

#01. extend()
l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10,11]
l1.extend(l2)
print(l1)

#02. addition
l3 = [2,3,4,5]
l4 = [6,7,34,5]
li = l3 + l4
print(li)

#03. loop
for x in l4:
    l3.append(x)
print(l3)    

#Global and Local Variable

#01. Global
x = 10
def myfunc():
    print(x)
myfunc()

# updating value
x = 10
def func():
   global x
   x = 11
   print(x)  

func()
print(x)   

# Local
y = 10
def f():
    y =13
    print(y) 

f()

#Tuple

#01.
a = ("Ram", "Shyam", 1, 5)
b = list(a)
b.append("Madhur")
c = tuple(b)
print(c)

#02.
for i in c:
    if i == "Shyam":
        print("yes")

#03.unpacking
i = ("Ram", "Shyam", "Suresh")
(a,b,c) = i
print(a)
print(c)
print(b)


