# a=int(input("Enter the Time : "))
# print("Time is :", a)
# if(a>12):
#     print("Good Morning")
# elif (a<=4):
#     print("Good Afternoon")
# elif(a<=2 and a>=12):
#     print("Good Noon")
# elif(a==10):
#     print("Good Evening")

import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")