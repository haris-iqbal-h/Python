#syntax

print("Hello, World!")

#This is a comment      Single Line and Multy Line

"""
This is a comment
written in
more than just one line
"""

#variables

x = 5
y = "John"
print(x)
print(y)

#type casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

print(type(x))
print(type(y))

#
a = "John1"
# is the same as Case-Sensitive
A = 'John'
print(a)
print(A)

#Assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#collection and unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)