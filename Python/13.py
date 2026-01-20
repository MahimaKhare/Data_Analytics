#inheritance 

class Car:
    def __init__(self, color, year,brand):
        self.color = color
        self.year = year
        self.brand = brand

class Audi(Car):
    def __init__(self,color, year,brand,race):
        super().__init__(color,brand,year)
        self.race = race

    def printd(self):
        print(self.color, self.race, self.year, self.brand)

obj1 = Audi("red","mustang",1976,180)
obj1.printd()

#Q1. Create a parent class person and pass name and age as parameters and create a child class student and pass the parameter name age and graduation year, and inherit all property from parent class to child

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,graduation_year):
        super().__init__(name,age)
        self.graduation_year = graduation_year

    def printd(self):
        print(self.name,self.age)

obj1 = Student("Mahima",20,2025)

obj1.printd()

#polymorphism
class Bike():
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        print(self.brand)

class Boat():
    def __init__(self,model):
        self.model = model   
    def move(self):
        print(self.model)

class Plane():
    def __init__(self,name):
        self.name = name 
    def move(self):
        print(self.name)

Bike1 = Bike("Honda")
Boat1 = Boat("boat")
Plane1 = Plane("plane")   

for x in(Bike1,Boat1,Plane1):
    x.move()


    

