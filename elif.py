a=int(input("Enter the Time : "))
print("Time is :", a)
if(a>12):
    print("Good Morning")
elif (a<=4):
    print("Good Afternoon")
elif(a<=2 and a>=12):
    print("Good Noon")
elif(a==10):
    print("Good Evening")