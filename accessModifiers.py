class Employee:
    def __init__(self):
        self.name = "Romel"
        self.age =25
        self.salary =15000

a =Employee()
print(a.name)
print(a.age)
print(a.salary)
print(a.__dir__())

# Private Access Modifier***************

# class Student: 
#     def __init__(self, age, name): 
#         self.__age = age      # An indication of private variable
        
#         def __funName(self):  # An indication of private function
#             self.y = 34
#             print(self.y)

# class Subject(Student):
#     pass

# obj = Student(21,"Romel")
# obj1 = Subject

# # calling by object of class Student
# print(obj.__age)
# print(obj.__funName())

# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())

# Protected Access Modifier***************************************

class Student:
    def __init__(self):
        self._name = "Romel"

    def _funName(self):      # protected method
        return "CodeWithRomel"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())