print('''Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
      * Note: Set items are unchangeable, but you can remove items and add new items.''')
print('Sets are written with curly brackets.')
print('thisset = {"apple", "banana", "cherry"}')

thisset = {"apple", "banana", "cherry"}
print(thisset)

print('_________________________________________________________________________')

print("Sets cannot have two items with the same value.")
print('thisset = {"apple", "banana", "cherry", "apple"}')

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print('_________________________________________________________________________')

print('True and 1 is considered the same value:')
print('thisset = {"apple", "banana", "cherry", True, 1, 2}')

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

print('_________________________________________________________________________')

print('''False and 0 is considered the same value:
      thisset = {"apple", "banana", "cherry", False, True, 0}''')

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

print('_________________________________________________________________________')

print('To determine how many items a set has, use the len() function.')
print('thisset = {"apple", "banana", "cherry"}')

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

print('_________________________________________________________________________')

print('Set items can be of any data type:')
print('''set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set1 = {"abc", 34, True, 40, "male"}''')

print('_________________________________________________________________________')

print("From Python's perspective, sets are defined as objects with the data type 'set':")
print('myset = {"apple", "banana", "cherry"}')

myset = {"apple", "banana", "cherry"}
print(type(myset))

print('_________________________________________________________________________')

print('It is also possible to use the set() constructor to make a set.')
print('thisset = set(("apple", "banana", "cherry")) # note the double round-brackets')

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print('_________________________________________________________________________')

print('''You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.''')
print('''thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)''')

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print('_________________________________________________________________________')

print('Check if "banana" is present in the set:')
print('thisset = {"apple", "banana", "cherry"}')

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

print('Check if "banana" is NOT present in the set:')
print('thisset = {"apple", "banana", "cherry"}')

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

print('_________________________________________________________________________')

print('Once a set is created, you cannot change its items, but you can add new items.')