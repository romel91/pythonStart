class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of employee is: {self.id} is {self.name}")
        
# Programmer inherit Employee
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")
            

e =Employee("Romel",201)
e.showDetails()
e1 =Programmer("Habibur",203)
e1.showDetails()
e1.showLanguage()