marks =[12,34,21,45,67,90,97,54,23]
# index=0
# for mark in marks:
#     print(mark)
#     if(index == 4):
#         print("This is average mark")
#     else:
#         print("This is not a average mark")    
#     index += 1

# enumerate

for index, mark in enumerate(marks):
    print(mark)
    if(index == 4):
        print("This is average mark")
    else:
        print("This is not a average mark")    

# another example

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# ........

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

# Changing the start index

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# string example
name ='Romel'
for index, c in enumerate(name):
    print(index, c)
    

