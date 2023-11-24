f = open('myfile.txt', 'w')
contents = f.write('Romel')
print(contents)

f = open('myfile.txt', 'a')
abc =f.write('Hello, world!')
print(abc)

with open('myfile.txt', 'r') as f:
    print(f.read())
    
file = open('myfile.txt', 'r')
file.close()

# Output:
# No output, but the file 'myfile.txt' is now closed and resources are freed.
   
