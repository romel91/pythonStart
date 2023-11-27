class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden in subclasses

class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} is giving birth.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Dog(Mammal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Mammal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Eagle(Bird):
    def speak(self):
        print(f"{self.name} screeches.")

# Creating instances of the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
eagle = Eagle("Freedom")

# Using methods from different levels of the hierarchy
dog.give_birth()  # Accessing method from Mammal
eagle.fly()       # Accessing method from Bird
cat.speak()       # Accessing overridden method in Cat

# Output:
# Buddy is giving birth.
# Freedom is flying.
# Whiskers says Meow!
