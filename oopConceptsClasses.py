# def hello():
#     print("Hello World!")

# hello()
class Person:
  name ="Romel"
  occupation ="Software Developer"
  networth = 20
  def info(self):
    print(f"{self.name} is a {self.occupation}")

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It must be provided as the extra parameter inside the method definition.

a =Person()
# a.name ='Sobuj'
# a.occupation ='Accountant'
# a.networth = 10
# print(a.name,a.occupation)
a.info()


