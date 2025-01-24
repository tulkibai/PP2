print('''Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:''')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

print("\n_____________________________\n")

print('''Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.''')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

print("\n_____________________________\n")

print("Dictionaries cannot have two items with the same key:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

print("\n_____________________________\n")

print("To determine how many items a dictionary has, use the len() function:")
print(len(thisdict))

print("\n_____________________________\n")

print("The values in dictionary items can be of any data type:")
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print("\n_____________________________\n")

print('''From Python's perspective, dictionaries are defined as objects with the data type 'dict':''')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

print("\n_____________________________\n")

print("It is also possible to use the dict() constructor to make a dictionary.")
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print("\n_____________________________\n")

print("You can access the items of a dictionary by referring to its key name, inside square brackets:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()

print('''The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.''')
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

print("\n_____________________________\n")

print("The values() method will return a list of all the values in the dictionary.")
x = thisdict.values()

print("The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

print("\n_____________________________\n")

#Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

print("\n_____________________________\n")

print("The items() method will return each item in a dictionary, as tuples in a list.")
x = thisdict.items()
print("The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

print("\n_____________________________\n")

print("Add a new item to the original dictionary, and see that the items list gets updated as well:")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

print("\n_____________________________\n")

print("To determine if a specified key is present in a dictionary use the in keyword:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")