l1 = [11, 22, 33, 44, 55, 66, 1, 9, 15, "ajay"]

print(type(l1))
print(l1)

l1.remove("ajay")
print(l1)

l1.append(101)
print(l1)

l1.extend([52, 87, 64, 23])
print(l1)

l1.sort()
print(l1)

print(l1.index(64))
