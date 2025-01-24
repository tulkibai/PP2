print('''Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds.''')

print()

print('''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.''')
print('''x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)''')

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

print()

print('''Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.''')
print('''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)''')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print()

print('''2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), 
      create a new tuple with the item(s), and add it to the existing tuple:''')
print('''thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)''')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

print()

print('''Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround 
      as we used for changing and adding tuple items:''')
print('''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)''')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print()

print("Or you can delete the tuple completely:")
print('''thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists''')

try:
    thistuple = ("apple", "banana", "cherry")
    del thistuple
    print(thistuple) #this will raise an error because the tuple no longer exists
except:
    print("NameError: name 'thistuple' is not defined")

print()

print('When we create a tuple, we normally assign values to it. This is called "packing" a tuple:')
print('When we create a tuple, we normally assign values to it. This is called "packing" a tuple:')

print()

print('But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":')
print('''fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)''')

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

print()

print('''If the number of variables is less than the number of values, you can add an * to the variable name 
      and the values will be assigned to the variable as a list:''')
print('''fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)''')

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print()

print('''If the asterisk is added to another variable name than the last, 
      Python will assign values to the variable until the number of values left matches the number of variables left.''')
print('''fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)''')

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)