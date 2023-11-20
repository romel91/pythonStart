'''
for i in range(12):
    if(i==10):
        break
    print("5 X", i+1, "=", 5 * (i+1))

print("Loop Done")
'''
for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)

