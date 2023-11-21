a =input("Enter the number: ")
print(f"multiplication table of {a} is: ")

try:
    for i in range(1,11):
     print(f"{int(a)} x {i} = {int(a)*i}")

except:
   print("error input")



print("hello math")

# ................................................

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

# finally clause
# This finally clause may be used for various purposes
# like closing some resourse files, 
# closing the database connections or ending the program with some appreciative messages.

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")