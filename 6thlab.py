#Python Directories and Files exercises

#1
import os
def content_listing(option):
    if option == 1:
        path='.'
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        print("Directories:", directories)
    if option == 2:
        path='.'
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print("Files:", files)
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        print("Directories:", directories)
    if option == 3:
        path = input("Enter the path: ")
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print("Files:", files)

#2
def access_checker(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

#3
def path_checker(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory portion:", os.path.dirname(path))
        print("Filename portion:", os.path.basename(path))
    else:
        print("Path does not exist.")   

#4
def lines_counter(filename):
    f = open(filename, 'r')      
    res = sum(1 for _ in f) 
    f.close()
    return res 

#5
def custom_write(filename, data):
    f = open(filename, 'w')
    for item in data:
        f.write(str(item) + '\n')
    f.close()

#6
import string
def file_generator():
    for char in string.ascii_uppercase:
        f = open(f"{char}.txt", 'w')
        f.write(f"This is {char}.txt\n")
        f.close()
#7
def file_copywriter(a, b):
    src = open(a, 'r')
    dest = open(b, 'w')
    dest.write(src.read())

#8
def file_deletor(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print(f"Permission denied: Cannot delete '{path}'.")
    else:
        print(f"File '{path}' does not exist.")


#Python builtin functions exercises

#1
from functools import reduce
def f1(a, b):
    print(f"Processing: {a}, {b}")
    return a + b
nums = [1, 2, 3, 4, 5]
result = reduce(f1, nums)
print("Result:", result)

#2
def case_counter(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"Uppercase": upper, "Lowercase": lower}
print(case_counter("Hello World"))

#3
def isP(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(isP("madam"))  
print(isP("Hello"))

#4
import time
import math
def lazy_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)
num = int(input("Enter the number: "))
delay = int(input("Enter the delay: "))
print(f"Square root of {num} after {delay} milliseconds is {lazy_sqrt(num, delay)}")

#5
def f5(tup):
    return all(tup)
print(f5((True, True, True)))
print(f5((True, False, True)))