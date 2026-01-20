data = [10,20,30,10,40,50,60]
max = 0
min = 0

for i in data:
    if i > max:
        max = i 

    if max > i:
        min = i        

second_largest = 0
for i in data:
    if i < max and i > second_largest:
        second_largest = i   
print(second_largest)        

second_smallest = 10
for i in data:
    if i < max and i > second_smallest:
        second_smallest = i

print(second_smallest)        
