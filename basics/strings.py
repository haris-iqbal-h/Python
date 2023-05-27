a = "Hello"
print(a)

#String as  Array
a = "Hello, World!"
print(a[1])

#loop on string
for x in "banana":
    print(x)

#len()  function
a = "Hello, World!"
print(len(a))

#string check Boolean
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

#string slice
b = "Hello, World!"
print(b[2:5])

#slice from start
b = "Hello, World!"
print(b[:5])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

#strip remove space start and end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))