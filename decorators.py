# ****************decorator*****************


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         result = fx(*args, **kwargs)
#         print("Thanks for using this function")
#         return result
#     return mfx

# @greet
# def hello():
#     print("Hello world")

# @greet
# def add(a, b):
#     return a + b

# hello()
# result = add(1, 2)
# print(result)

# *******************logging*****************

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
result = my_function(1, 2)
print(result)
