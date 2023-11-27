class circle():
    def __init__(self, radius):
      self.radius = radius

    def area(self):
       return 3.14 * self.radius * self.radius  
      
a = circle(radius=5)
print (a.area())

# another example method override

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating instances of the classes
animal_obj = Animal()
dog_obj = Dog()
cat_obj = Cat()

# Calling the make_sound method for each object
animal_obj.make_sound()  # Output: Generic animal sound
dog_obj.make_sound()     # Output: Woof! Woof!
cat_obj.make_sound()     # Output: Meow!
