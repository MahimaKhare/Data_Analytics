#set
s = {
    "Apple",
    "Mango",
    "Orange"
}
print(s)
print(len(s))

# constructor
e = [1,2,3,8,5,3,1]
x = set(e) 
print(x)

# set with loop
for i in x :
    print(i)

# add data into set
x.add(4)
print(x)

# remove data from set
x.remove(2)
print(x)

#dictionary

d = {
     "brand" : "volvo",
     "year" : 1990
     }
print(d)

#constructor
d1 = dict(name = "Ravi", age = 20)
print(d1)

#Access value
print(d1['name'])

#Access Keys 
print(d.keys())

# Access all valuse
print(d.values())

# to add value
d1['year'] = 2000
print(d1)

# Pop()
print(d1.pop('year'))

# nested dictionary
data = {
    "user1" :{
        'fname' : "Mahima",
        'lname' : "Khare"
    },
    "user2" :{
        'fname' : "Ravi",
        'lname' : "Singh"
    }
}
print(data)
#Q1. Unique Cities Finder
cities = ["Delhi", "Mumbai", "Pune", "Delhi", "Pune", "Jaipur", "Mumbai"]
# 1.unique cities set from List
x = set(cities)
print(x)
print(type(x))

# 2. Total unique cities count 
print(len(x))

#Q2. Remove Duplicates from List Using Set
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]
#1. remove duplicates using set
y = set(nums)
print(y)
# 2. Convert result into list
y2 = list(y)
print(y2)
print(type(y2))

#Q3. Count Word Frequency (Dictionary)
text = "apple mango apple orange mango apple"

#1. creat dictionary
fruits ={
         "apple" : 3,
         "mango" : 2,
         "orange" : 1
}
print(fruits)

#Q4. Student Marks Dictionary
marks = {
    "Ajay": 85,
    "Rohit": 92,
    "Simran": 78,
    "Neha": 90
}
# 1.Print students names 
for i in marks:
    print(i)

# 2. Average marks 
sum = sum(marks.values())
print(sum / len(marks))

# 3. Highest marks laane wale student ka naam print karo


#Q5. Price Updater
prices = {
    "pen": 10,
    "pencil": 5,
    "notebook": 50
}

# Task:
# 1. Sab items ki price 10% badhao 
for i in prices.values():
    new_dict = i * 1.10
    print(new_dict)
# 2. print new dictionary
print(new_dict)