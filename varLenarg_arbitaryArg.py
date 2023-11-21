'''
# arbitary argument

def name(*name):
    print("Hello,", name[0], name[1], name[2] ,name[3])

name("James", "Buchanan", "Barnes","Romel")
'''
# see hand notes if not understand later

# keyword arbitary arguments

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"] ,name["tname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James" , tname ="Dhaka")