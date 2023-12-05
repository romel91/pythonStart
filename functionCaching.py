from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*2

# print(fx(20))
# print("Done for 20")
# print(fx(2))
# print("Done for 2")
# print(fx(10))
# print("Done for 10")
@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])