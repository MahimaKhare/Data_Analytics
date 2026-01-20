#Function
def add(a,b):
    print(a + b)

add(10,20)

# input by user
i = int(input("enter a number"))
j = int(input("enter a number"))

def sum(i,j):
    print(i+j)

sum(i,j)   

#return
def a(num1,num2):
    return num1+num2
result = a(10,20)
print(result)

#default values
def details(name = "Mahima Khare", age = 20):
    print(name)
    print(age)

details()

#01.
def student_details(name,last_name,age,roll_no):
    print(name)
    print(last_name)
    print(age)
    print(roll_no)


student_details("Mahima", "Khare", 20, 23)   

#Lambda function
add = lambda a,b : a+b
result = add(30,40)
print(result)

#2. 
def test(x,y):
    return x if x>y else y
print(test(test(2,5),test(10,3)))