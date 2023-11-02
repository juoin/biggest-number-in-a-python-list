li = [10,25,75,41,96]
max = 54
max1 = 4
for i in li:
    if i > max:
        max = i
print(max)
for i in li:
    if i > max1 and i <max:
        max1 = i
print(max1)
