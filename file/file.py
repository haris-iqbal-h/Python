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