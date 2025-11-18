#Conditional Operator

#if 
age = int(input("enter your age"))
if age >= 18 :
    print("Can Drive")

# if else 
if age >= 18:
    print("Can Drive")
else:
    print("Can't Drive" )

#if elif else
Day = int(input("Enter a number"))   
if Day == 1:
    print("Monday") 
elif Day == 2:
    print("Tuesday")
elif Day == 3:
    print("Wednesday")
elif Day == 4:
    print("Thursday")    
elif Day == 5:
    print("Friday")
elif Day == 6:
    print("Saturday")
elif Day == 7:
    print("Sunday")
else:
    print("enter a valid number")   

#01. Months name using if elif statement
month = int(input("enter a number"))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")   
elif month == 11:
    print("November")                                     
elif month == 12:
    print("December")
else:
    print("Enter a valid number")    

#and operator with conditional statements
Age = 18
name = "Harshit"
if Age >= 18 and name == "Harshit":
    print("Yes")
else:
    print("no")

#or operator with conditional statement
if age >= 10 or name == "H":
    print("yes")
else:
    print("no")    

#02
Num = int(input("enter a number"))
if Num == 25:
    print("winner")
else:
    print("Losser")    

#03.
num = int(input("enter a number between 1 to 50"))
if num == 25:
    print("winner")
elif num >= 0 and num <= 24:
    print("lesser")
elif num >= 26 and num <=50 :
    print("Greater")
else:
    print("Enter a valid number")     

#04.
Num = int(input("enter a number between 1 to 50"))
if Num == 25:
    print("Winner")
elif Num >= 0 and Num <= 20:
    print("lesser")
elif Num >= 21 and Num <= 24:
    print("lesser but near to win")
elif Num >= 26 and Num <= 30:
    print("Greater but near to win")
elif Num >= 31 and Num <= 50:
    print("Greatest")
else:
    print("enter a valid number")    

#Match
#01.
day = int(input("enter a number"))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Enter a valid number")

#02.
Month = int(input("enter a number"))
match Month:
    case 1:
        print("January")
    case 2:
        print("February") 
    case 3:
        print("march")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November") 
    case 12:
        print("December")
    case _:
        print("enter a valid number")                                              

#03
num2 = int(input("enter a number"))
match num2:
    case("num2 == 25"):
         print("winner")
    case _:
         print("Losser")  

