import csv

file = open("hello.txt", "w")
file.write("Hello, world!")
file.close()

with open("hello.txt") as f:
    for line in f:
        #do something with line
        print(line)



with open('favorite_colors.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))

f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
    print(x)

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

f = open("myfile.txt", "x")

f = open("myfile.txt", "w")


import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

os.rmdir("myfolder")