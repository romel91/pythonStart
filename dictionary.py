dic ={
    "Romel" : "human being",
    "Spoon" : "object"
}
print(dic["Romel"])

# Accessing single values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info["age"])
print(info.get('eligible'))

# Accessing multiple values:

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# Accessing keys:

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# Accessing key-value pairs:

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())