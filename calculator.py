'''
n1 = int(input("Press Your First Number:"))
n2 =int(input("Press Your Second Number:"))

# addition

print("{} + {} =".format(n1 , n2))
print(n1 + n2)
# subtraction

print("{} - {} =".format(n1 , n2))
print(n1 - n2)
# multiplication

print("{} * {} =".format(n1 , n2))
print(n1 * n2)
# division

print("{} / {} =".format(n1 , n2))
print(n1 / n2)

'''
#Another Calculator

#addition
def addition(n1,n2):
    return n1+n2
#subtraction
def subtraction(n1,n2):
    return n1-n2
#multiplication
def multiplication(n1,n2):
    return n1*n2
#division
def division(n1,n2):
    return n1/n2

print("select operation")
print(
    "1.Addition"
    "2.Subtraction"
    "3.Multiplication"
    "4.Division"
)
choice=int(input("Enter your choice 1/2/3/4 :"))

n1 =float(input ("Enter the first value :"))
n2 =float(input ("Enter the second value :"))

if choice ==1:
    print (n1, "+", n2, "=", addition(n1, n2))

elif choice ==2:
    print(n1,"-",n2,"=",subtraction(n1,n2))
    
elif choice ==3:
    print(n1,"*",n2,"=",multiplication(n1,n2))
    
elif choice ==4:
    print(n1,"/",n2,"=",division(n1,n2))

else:
    print("Invalid value")
