#There are several methods to remove items from a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

print('\n----------------------------------------------\n')

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

print('\n----------------------------------------------\n')
 
#The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

print('\n----------------------------------------------\n')

#The del keyword can also delete the dictionary completely:
try:
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    del thisdict
    print(thisdict) #this will cause an error because "thisdict" no longer exists.
except:
    print("NameError: name 'thisdict' is not defined")
 
print('\n----------------------------------------------\n')

#The clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\n----------------------------------------------\n')

'''You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.'''
for x in thisdict:
    print(x)

print('\n----------------------------------------------\n')

#Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

print('\n----------------------------------------------\n')

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)

print('\n----------------------------------------------\n')

#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)

print('\n----------------------------------------------\n')

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)