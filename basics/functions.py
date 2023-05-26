#simple funtion
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#local scope difference
x1 = "awesome"

def myfunc1():
    x1 = "fantastic"
    print("Python is " + x1)    

myfunc1()

print("Python is " + x1)

#global scope difference
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python1 is " + x)