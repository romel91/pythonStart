# def my_generator():
#     for i in range(500000):
#         yield i

# # Using the generator
# gen = my_generator()

# # print(next(gen))  # Output: 1
# # print(next(gen))  # Output: 2
# # print(next(gen))  # Output: 3
# for j in gen:
#     print(j)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator in a for loop
for i in countdown(5):
    print(i)

