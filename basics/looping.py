i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

for x in range(6):
        print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)