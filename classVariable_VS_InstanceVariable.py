class Employee:
    company_name = "Google"
    noOfEmployes = 0

    def __init__(self, name):
        self.name = name
        self.salary = 1500000
        Employee.noOfEmployes +=1

    def showdetails(self):
        print(f"Name: {self.name} is an employee of {Employee.noOfEmployes} in sized {self.company_name} and his/her salary is {self.salary}")

emp1 = Employee("Romel")
emp1.company_name = "Microsoft"
emp2 = Employee("Razia")
emp2.salary = 2000000

emp1.showdetails()
emp2.showdetails()

            