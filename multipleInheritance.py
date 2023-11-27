# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Parent class 2
class Flyable:
    def fly(self):
        print(f"{self.name} can fly")

# Child class inheriting from both Animal and Flyable
class Bird(Animal, Flyable):
    def chirp(self):
        print("Chirp! Chirp!")

# Creating an instance of the Bird class
my_bird = Bird(name="Robin")

# Accessing methods from both parent classes and the child class
my_bird.speak()  # Calls the speak method from the Animal class
my_bird.fly()    # Calls the fly method from the Flyable class
my_bird.chirp()  # Calls the chirp method from the Bird class
