print(number:=10)
a = True
print(a:=False)

numbers =[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())

# Without the walrus operator
numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared_num = num ** 2
    squared.append(squared_num)

# With the walrus operator
numbers = [1, 2, 3, 4, 5]
squared = [num_squared for num in numbers if (num_squared := num ** 2)]

print(squared)
