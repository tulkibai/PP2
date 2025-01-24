print('You can loop through the tuple items by using a for loop.')
print('Iterate through the items and print the values:')
print('''thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)''')

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print()

print('''You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.''')
print('''thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])''')

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

print()

print('''You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple, 
      then start at 0 and loop your way through the tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration.''')
print('''thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1''')

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

print('To join two or more tuples you can use the + operator:')
print('Join two tuples:')
print('''tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)''')

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

print()

print('If you want to multiply the content of a tuple a given number of times, you can use the * operator:')
print('''fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)''')

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)