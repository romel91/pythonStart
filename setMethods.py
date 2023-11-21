# joining sets
s1 ={9,11,13,1,2,3}
s2 ={4,5,6,2,3}
# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.update(s2)
# s1.intersection_update(s2)
s3 =s1.symmetric_difference(s2)
print(s3)
# print(s1,s2)

#  difference() and difference_update():

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference_update(cities2)
print(cities3)

# isdisjoint():

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset():

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid","Delhi"}
print(cities.issuperset(cities3))

# issubset():

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# pop()

# This method removes the last item of the set but the catch is that we don’t 
# know which item gets popped as sets are unordered. However, you can access 
# the popped item if you assign the pop() method to a variable.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del
# This method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

# clear
# This method clears all items in the set and prints an empty set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if item exists

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


