# factorial(7) =7*6*5*4*3*2*1
# factorial(6) =6*5*4*3*2*1
# factorial(5) =5*4*3*2*1
# factorial(4) =4*3*2*1
# factorial(3) =3*2*1
# factorial(2) =2*1
# factorial(1) =1
# factorial(0) =1
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# fibonacci sequence

def fibonacci(n):
  if n == 0:  # base case
    return 0
  elif n == 1:  # base case
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)  # recursive call

# Print out the Fibonacci sequence up to the 10th term
for i in range(4):
  print(fibonacci(i))