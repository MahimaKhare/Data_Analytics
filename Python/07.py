#01.Program to print all even numbers from 1 to 50 (using for loop and if condition).
for i in range (1,51):
    if i % 2 == 0:
        print(i)

#02.Program that prints numbers from 1 to 20 but skips multiples of 3 using continue.
for n in range (1,21):
    if n % 3 == 0:
        continue
    print(n)

#03.Program to find the sum of numbers from 1 to 100 using a while loop.
a = 1
sum = 0
while a <= 100:
    sum = a + sum
    a += 1
print(sum)  

#04.Program that takes a number from the user and checks if it is a prime number (use for loop, if-else, and boolean flag).
num = int(input("enter a number"))
is_prime = True
if num <=1:
    is_prime = False
else:
    for i in range(2,num):
        if num%i == 0:
            is_prime= False
            break
if is_prime:
    print("is Prime number")
else:
    print("Not Prime")

#05.Write a program to print the multiplication table of any number (example: table of 7) using a for loop.
for j in range (1,11):
  print(j * 12)

#06.Program that prints numbers from 1 to 20 but stops the loop if the number becomes greater than 12 (use break).
for num in range (1,21):
    if num > 12:
        break
    print(num)

#07.Program using a while loop that keeps asking the user for a password until the correct password is entered (use if-else + break).
p = 123456
while True:
    password = int(input("Enter password"))
    if password == p:
        print("Your Password is Correct")
        break
    else:
        print("Enter correct password")

#08.Program to count the number of vowels in a string using a for loop and if condition.
v = "aeiouAEIOU"
count = 0
for s in  "Mahima Khare":
    if s in v:
        count += 1
print(count)    
  
#09.Program to print numbers from 1 to 30 but only print numbers divisible by 5 OR 7 (use boolean operator OR).
for e in range (1,31):
    if e % 5 == 0 or e % 7 == 0:
        continue
    print(e)
#010.Write a program to take 5 numbers from the user and find the largest number (use for loop and if condition).
largest = 0
for i in range(5):
    n = int(input("Enter a number"))

    if n > largest:
        largest = n
print(largest)