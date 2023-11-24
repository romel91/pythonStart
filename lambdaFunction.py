def appl(fx ,value):
    return 6 + fx(value)

double = lambda a : a * 2
cube = lambda a:a*a*a
avg = lambda x,y,z :x+y+z/2
print(double(3))
print(cube(3))
print(avg(2,3,4))
print(appl(cube,2))