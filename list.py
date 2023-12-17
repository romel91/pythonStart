'''
Python Lists:
-Lists are ordered collection of data items.
-They store multiple items in a single variable.
-List items are separated by commas and enclosed within square brackets [].
-Lists are changeable meaning we can alter them after creation.
'''

'''
l =[3,2,5,"Romel",True,6,7,8,43,1]

print(type(l))
print(l[0])
print(l[1])
print(l[-3])
print(l[-2])
print(l[-1])
# nagative index start from last and starting value is -1
print(l[1:-4:2])
# slicing list with step size 2 means take every second element,,, it's jumping 2 repetadly

print(l[:5])
print(l[5:])

'''
# ******list comprehension*******************************

'''
lst =[i*i for i in range(8) if i%2==0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)

'''
# *******************end***********************************


# *******************list methods***************************

# l =[11,21,19,2,3,43,5,4,4,3,3]
# print(l)
# l.append(99)
# print("After append : ", l)
# l.sort() showing ascending order
# l.sort(reverse=True)
# l.reverse()
# print(l.index(43))
# print(l.count(4)) it detect repeatation of a value
# l.insert(4 ,"Romel") index 4 is romel   
# print(l)

#add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)
# concate
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
colors3 =["ultrablur","lightGray"]
colors2.append(colors3)
print(colors2)
# print(colors + colors2)


