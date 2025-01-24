print('To add one item to a set use the add() method.')
print('''thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)''')

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("__________________________________________________\n")

print("To add items from another set into the current set, use the update() method.")
print('''thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)''')

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

print("__________________________________________________\n")

print("The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).")

print('''thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)''')

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

print("__________________________________________________\n")

print("To remove an item in a set, use the remove(), or the discard() method.")
print('Note: If the item to remove does not exist, remove() will raise an error.')
print('Note: If the item to remove does not exist, discard() will NOT raise an error.')
print('''thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)''')


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

print('''thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)''')


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

print("__________________________________________________\n")

print('''You can also use the pop() method to remove an item, 
      but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.''')
print('Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.')
print('''thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)''')

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

print('''thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)''')

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

print('''thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)''')

try:
    thisset = {"apple", "banana", "cherry"}
    del thisset
    print(thisset)
except:
    print("NameError: name 'thisset' is not defined")