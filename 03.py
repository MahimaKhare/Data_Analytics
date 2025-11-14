# Q.1. covert hello into upper case
x = "hello"
y = x.upper()
print(y)

# Q.2 z=hello cover the first letter into upper case
z = "hello"
x1 = z[0].upper()
y1 = z[1:5] 
z2 = x1 + y1
print(z2)

# 03. String Modify
fname = input("enter your name")
lname = input("enter your last name")

x = fname .strip()
y = lname .strip()

x1 = x[0].upper()
y1 = y[0].upper()

x2 = x[1: ].lower()
y2 = y[1: ].lower()

x3 = x1 + x2
y3 = y1 + y2

z = x3 + " " + y3
print(z)

#Q.4. text = "hello world" convert the string into uppercase
text = "hello world"
x4 = text.upper()
print(x4)

#Q.5. name = "PYTHON PROGRAMING" convert the string into lowercase
name = "PYTHON PROGRAMING"
x5 = name.lower()
print(x5)

#Q.6. data =" apple,banana,grapes  " strip spaces and then split using comma
data = "  apple,banana,grapes  "
x6 = data.strip()
y4 = x6.split(',')
print(y4)

# Q.7. msg = "PythonisAwesome" print only "Python" using slicing
msg = "PythonisAwesome"
y5 = msg[0:6]
print(y5)

# Q.8. word = "banana" count how many times a appears in the string
word = "banana"
z3 = word.count('a')
print(z3)

#Q.9 sentence = "I Love Python Programing" print python from here
sentence = "I Love Python Programing"
x7 = sentence[7:13]
print(x7)

# Q.10. text2 = "HELLO" convert the string into lowercase using lower()
text2 = "HELLO"
x8 = text2.lower()
print(x8)

# Q.11. info = "  Welcome to Python  " remove the leading and trailing spaces
info = "  Welcome to Python  "
y6 = info.strip()
print(y6)

# Q.12. fruits = "apple orange mango" split the string by spaces into a list
fruits = "apple orange mango"
y7 = fruits.split(" ")
print(list(y7))

#Q.13. Course = "DataScience" print characters from index 4 to 9 using slicing
Course = "DataScience"
y8 = Course[4:10]
print(y8)
