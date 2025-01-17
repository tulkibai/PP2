x = 5
y = "John"
print(x)
print(y)
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
x = 5
y = "John"
print(type(x))
print(type(y))
x = "John"
# is the same as
x = 'John'
a = 4
A = "Sally"
#A will not overwrite a
#legible naming
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
illegal naming
2myvar = "John"
my-var = "John"
my var = "John"
"""
#camel case
myVariableName = "John"
#pascal case
MyVariableName = "John"
#snake case
my_variable_name = "John"
#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
illegible outing
x = 5
y = "John"
print(x + y)
"""
#legible multi outing
x = 5
y = "John"
print(x, y)
#concatenation
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#global variables
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
