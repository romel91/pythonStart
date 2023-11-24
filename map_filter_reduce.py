# map()***************************
def cube(x):
    return x*x*x
print(cube(2))

array = [2,4,6,8,10,12,1]
newarr =list(map(cube,array))
print(newarr)

sentence ="ROMEL Is Learning PYTHON"

# Define a lambda function to filter out uppercase words

get_uppercase_words =lambda word:word if word.isupper() else ''

# Use map to apply the lambda function to each word in the sentence
uppercase_words =list(map(get_uppercase_words,sentence))
print(uppercase_words)

# filter()************************
def filter_function(y):
    return y>4


newfilter =list(filter(filter_function, array))
print(newfilter)

# reduce**************
from functools import reduce

numbers =[1,2,3,4,5]

def reduce_func(x,y):
    return x + y
reducer =reduce(reduce_func,numbers)
print(reducer)


# "is vs '==" in python
a=5
b =5
print(a is b)
print(a == b)

c=[5,4,3]
d=[5,4,3]
print(c is d)
print(c == d)


