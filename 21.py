print("You can loop through the set items by using a for loop:")
print('''thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)''')

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("\n__________________________________________\n")

print('''There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.''')

print("\n__________________________________________\n")

print("The union() method returns a new set with all items from both sets.")
print('''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)''')

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

print("\n__________________________________________\n")

print("You can use the | operator instead of the union() method, and you will get the same result.")
print('''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)''')

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

print("\n__________________________________________\n")

print('''All the joining methods and operators can be used to join multiple sets.
When using a method, just add more sets in the parentheses, separated by commas:''')
print("Join multiple sets with the union() method:")
print('''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)''')

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

print("\n__________________________________________\n")

print("When using the | operator, separate the sets with more | operators:")
print('''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)''')

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

print("\n__________________________________________\n")

print('''The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.''')
print('''x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)''')

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

print("\n__________________________________________\n")

print('''The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.''')
print("Note: Both union() and update() will exclude any duplicate items.")
print('''set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)''')

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

print("\n__________________________________________\n")

print('''Keep ONLY the duplicates
The intersection() method will return a new set, that only contains the items that are present in both sets.''')
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

print("\n__________________________________________\n")

print("You can use the & operator instead of the intersection() method, and you will get the same result.")
print('''Note: The & operator only allows you to join sets with sets, 
      and not with other data types like you can with the intersection() method.''')
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

print("\n__________________________________________\n")

print(""""The intersection_update() method will also keep ONLY the duplicates,
       but it will change the original set instead of returning a new set.""")
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

print("\n__________________________________________\n")

print("The values True and 1 are considered the same value. The same goes for False and 0.")
print('''set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)''')

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

print("\n__________________________________________\n")

print("""The difference() method will return a new set that will contain only the items 
      from the first set that are not present in the other set.""")
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

print("\n__________________________________________\n")

print("You can use the - operator instead of the difference() method, and you will get the same result.")
print("""Note: The - operator only allows you to join sets with sets, 
      and not with other data types like you can with the difference() method.""")
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

print("\n__________________________________________\n")

print('''The difference_update() method will also keep the items from the first set that are not in the other set, 
      but it will change the original set instead of returning a new set.''')
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

print("\n__________________________________________\n")

print("The symmetric_difference() method will keep only the elements that are NOT present in both sets.")
print("""set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)""")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

print("\n__________________________________________\n")

print("You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.")
print('''Note: The ^ operator only allows you to join sets with sets, 
      and not with other data types like you can with the symmetric_difference() method.''')
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

print("\n__________________________________________\n")

print("The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.")
print('''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)''')

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)