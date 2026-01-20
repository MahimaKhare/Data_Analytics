#Loops

#While Loop
start = 1
while(start <= 10):
    print(start)
    start += 1

#01. Print odd numbers
start = 1
while (start <= 10):
    print(start)
    start += 2

#02. print sum of all numbers
first = 1
sum = 0
while(first <= 10):
    sum = sum + start
    first += 1
print(sum) 

#03. sum of odd numbers
start = 1
sum = 0
while(start <= 10):
    sum = sum + start
    start += 2
print(start)    

#04.even numbers
num = 1
while(num <= 10):
    if num % 2 == 0:
        print(num)
    num += 1  

#05. print string character one by one
string = "Hello World"
s = 0
while(s<(len(string))):
    print (string[s])
    s += 1

#06.count "l" in "Hello World"
string = "Hello World"
count = 0
i = 0
while i<len(string):
    if string[i] == 'l':
     count += 1 
    i += 1   
print(count)  

#07 
text = input("enter a string")
char = input("enter a char")
count = 0
i = 0
while i < len(text):
   if text[i] == char:
    count += 1
   i += 1
print(count)   