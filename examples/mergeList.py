listOne = []
listTwo = []

print("Enter 6 Elements for First List: ")
for i in range(6):
  listOne.append(input())
print("\nEnter 6 Elements for Second List: ")
for i in range(6):
  listTwo.append(input())

listThree = []
for i in range(6):
  listThree.append(listOne[i])
for i in range(6):
  listThree.append(listTwo[i])

print("\nThe New (Merged) List is: ")
print(listThree)