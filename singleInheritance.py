# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Creating an instance of the Dog class
my_dog = Dog(name="Buddy")

# Accessing methods from both the parent and child classes
my_dog.speak()  # This will call the speak method from the Animal class
my_dog.bark()   # This will call the bark method from the Dog class
