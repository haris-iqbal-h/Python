import mymodule as mx
import platform
import datetime

mx.greeting("Jonathan")

a = mx.person1["age"]
print(a)


a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform)
print(x)

from mymodule import person1

print (person1["age"])

x = datetime.datetime.now()
print(x)