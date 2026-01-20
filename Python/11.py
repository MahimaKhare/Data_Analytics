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

#Task:
# 1.unique cities set from List
x = set(cities)
l = list(x)
print(l)

# 2. Total unique cities count 
print(len(l))


#Q2. Remove Duplicates from List Using Set
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]

#Task:
#1. remove duplicates using set
y = set(nums)
print(y)

# 2. Convert result into list
y2 = list(y)
print(y2)

#Q3. Count Word Frequency (Dictionary)
text = "apple mango apple orange mango apple"

#Task:
#Create new dictionary
d2 = text.split(" ")
print(d2)

this_dict = {}
for i in d2:
    if i in this_dict:
        this_dict[i] += 1
    else:
        this_dict[i] = 1
print(this_dict)  

#Q4. Student Marks Dictionary
marks = {
    "Ajay": 85,
    "Rohit": 92,
    "Simran": 78,
    "Neha": 90
}

#Task:
# 1.Print students names 
for i in marks.keys():
    print(i)

# 2. Average marks 
sum = 0
for i in marks.values():
    sum += i
    avg = sum / len(marks)
print(avg)        

# 3.Print student name who got Highest marks 
highest = 0
Student = ""
for key, value in marks.items():
    if value > highest:
        highest = value
        Student = key
print(Student, highest)


#Q5. Price Updater
prices = {
    "pen": 10,
    "pencil": 5,
    "notebook": 50
}

# Task:
# 1. increase the items price by 10% 
new_dict = {}
for i, j in prices.items():
    new_dict[i] = j * 1.10
print(new_dict)