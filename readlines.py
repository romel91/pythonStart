# f = open('myfile.txt', 'r')
# i = 0

# for line in f.readlines():
#     i += 1
#     m1, m2, m3 = line.strip().split(",")[:3]  # Split the line into three parts
#     print(f"First subject {i} is: {m1}")
#     print(f"Second subject {i} is: {m2}")
#     print(f"Third subject {i} is: {m3}")
#     print(line)

f = open("myfile.txt", "a")
lines =["See you soon!", "Over and out."]
f.writelines(lines)
f.close()


f.close()