"""You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy()."""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print("\n---------------------------------------------------\n")

#Another way to make a copy is to use the built-in function dict().
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

print("\n---------------------------------------------------\n")

#A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

print("\n---------------------------------------------------\n")

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)

print("\n---------------------------------------------------\n")

#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"])

print("\n---------------------------------------------------\n")

#You can loop through a dictionary by using the items() method like this:
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])