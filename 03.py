# Type Casting
a = 5
print(float(a))

# Genrating random numbers 
import random
a1 = random.randrange(1,7)
print(a1)

# length of string
b = "Hello"
print(len(b))

# String Slice
b1 = "Hello World"
c = b1[0:5]
print(c)

# Split
b2 = "Hello"
b3 = b2.split('e')
print(b3)

# Strip
a2  = "  Hello " 
a3 = a2.strip()
print(a3)

#01. convert hello into upper case
x = "hello"
y = x.upper()
print(y)

#02 z=hello convert the first letter into upper case
z = "hello"
x1 = z[0].upper()
y1 = z[1:5] 
z2 = x1 + y1
print(z2)

#03. String Modify
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

#04. text = "hello world" convert the string into uppercase
text = "hello world"
x4 = text.upper()
print(x4)

#05. name = "PYTHON PROGRAMING" convert the string into lowercase
name = "PYTHON PROGRAMING"
x5 = name.lower()
print(x5)

#06. data =" apple,banana,grapes  " strip spaces and then split using comma
data = "  apple,banana,grapes  "
x6 = data.strip()
y4 = x6.split(',')
print(y4)

#07. msg = "PythonisAwesome" print only "Python" using slicing
msg = "PythonisAwesome"
y5 = msg[0:6]
print(y5)

#08. word = "banana" count how many times a appears in the string
word = "banana"
z3 = word.count('a')
print(z3)

#09 sentence = "I Love Python Programing" print python from here
sentence = "I Love Python Programing"
x7 = sentence[7:13]
print(x7)

#10. text2 = "HELLO" convert the string into lowercase using lower()
text2 = "HELLO"
x8 = text2.lower()
print(x8)

#11. info = "  Welcome to Python  " remove the leading and trailing spaces
info = "  Welcome to Python  "
y6 = info.strip()
print(y6)

#12. fruits = "apple orange mango" split the string by spaces into a list
fruits = "apple orange mango"
y7 = fruits.split(" ")
print(list(y7))

#13. Course = "DataScience" print characters from index 4 to 9 using slicing
Course = "DataScience"
y8 = Course[4:10]
print(y8)
