print("""thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)""")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print()

print("""thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
""")
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print()

print("""thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)""")
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

print()

print("""list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)""")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print()

print("""list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)""")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

print()

print("""list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)""")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)