mylist = list()
print("Enter 5 elements for the list: ")
for i in range(5):
    mylist.append(input())

print("\nOriginal list:", mylist)

revlist = mylist[::-1]
print("Reversed List:", revlist)