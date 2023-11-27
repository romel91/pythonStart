class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

# Creating an instance using the regular constructor
e1 = Employee("Romel", 15000)
print(e1.name, e1.salary)

# Creating an instance using the class method
string = "john-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)
