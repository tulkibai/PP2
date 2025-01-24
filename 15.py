print("""Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.""")
print('thistuple = ("apple", "banana", "cherry")')

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print()

print("Since tuples are indexed, they can have items with the same value:")
print('thistuple = ("apple", "banana", "cherry", "apple", "cherry")')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print()

print("To determine how many items a tuple has, use the len() function:")
print('thistuple = ("apple", "banana", "cherry")')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print()

print("To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.")
print('thistuple = ("apple",)')

print(type(thistuple))

print('thistuple = ("apple")')

print(type(thistuple))

print()

print("Tuple items can be of any data type:")
print('''tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)''')

print()

print("A tuple can contain different data types:")
print('tuple1 = ("abc", 34, True, 40, "male")')

print()

print("From Python's perspective, tuples are defined as objects with the data type 'tuple':")
print('mytuple = ("apple", "banana", "cherry")')

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print()

print("It is also possible to use the tuple() constructor to make a tuple.")
print('thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets')

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print()

print("You can access tuple items by referring to the index number, inside square brackets:")
print('''thistuple = ("apple", "banana", "cherry")
print(thistuple[1])''')

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print()

print('''Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.''')
print('''thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])''')

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print()

print('''You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.''')
print('''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])''')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print()

print('By leaving out the start value, the range will start at the first item:')
print('''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])''')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

print()

print("By leaving out the end value, the range will go on to the end of the tuple:")
print('''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])''')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

print()

print("Specify negative indexes if you want to start the search from the end of the tuple:")
print('''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])''')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

print()

print("To determine if a specified item is present in a tuple use the in keyword:")
print('''thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")''')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")