# Class Object
class car:
    car = " "   
obj1 = car() 
obj1.car = "Audi"
print(obj1.car)  

obj2 = car()
obj2.car = "BMW" 
print(obj2.car)

# Function inside Class
class person:
 def __init__(self,name,age):
    self.name = name
    self.age = age

 def printd(self):
    print(self.name , self.age)

user1 = person("Ravi", 23)
user2 = person("sami",21)

user1.printd()
user2.printd()

# Example
class Car:
   def __init__(self,brand,year,race):
       self.brand = brand
       self.year = year
       self.race = race

   def printd(self):
      print(self.brand, self.year, self.race)

car1 = Car("mustang",1969,150)
car2 = Car("audi",1970,250)
car3 = Car("bmw",1999,300)

car3.printd()

#Q1. Create a class of person and after create 4 object using fistname, lastname, age, gender and also create a function for print their name and age
class Person:
   def __init__(self,firstname,lastname,age,gender):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.gender = gender


   def printe(self):
     print(self.firstname, self.age) 

person1 = Person("Mahima","Khare",20,"Female")
person2 = Person("Ramesh","Kumar",23,"Male")
person3 = Person("Suresh","Kumar",12,"Male")
person4 = Person("Riya", "Sharma", 19, "Female")

person1.printe()      


#Q2.Create a class of person and after create 4 object using fistname, lastname, age, gender and also create a function for print their name and age also create a function to check user age is even or odd

class Person:
   def __init__(self,firstname,lastname,age,gender):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.gender = gender

   def printd(self):
      if self.age / 2 == 0:
         print(self.age,"number is even")
      else:
         print(self.age,"number is odd" ) 

person1 = Person("Mahima","Khare",20,"Female")
person2 = Person("Ramesh","Kumar",23,"Male")
person3 = Person("Suresh","Kumar",12,"Male")

person2.printd()

#Q3.create a class of calculator and pass a,b create 4 function for add, sub, mul, divide

class Calculator:
   def __init__(self,a,b):
      self.a = a
      self.b = b

   def sum(self):
      print(self.a + self.b)
      
   def sub(self):
      print(self.a - self.b)

   def mul(self):
      print(self.a * self.b)

   def divide(self):
      print(self.a / self.b)
         
         
         
value1 = Calculator(10,2)

value1.sum()
value1.sub()
value1.mul()
value1.divide()
        
        
