#Generator

#1
def square_generator(n):
    for i in range(n):
        yield i * i

#2
def even_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
n = int(input())
even = even_generator(n)
for i in even:
    print(i)

#3
def generator34(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
l34 = generator34(n)
for i in l34:
    print(i)

#4
def square_generator2(a, b):
    for i in range(a, b + 1):
        yield i * i
a = int(input())
b = int(input())
square2 = square_generator2(a, b)
for i in square2:
    print(i)

#5
def down_generator(n):
    for i in range(n, -1, -1):
        yield i

#Date

#1
from datetime import datetime, timedelta
cur = datetime.now()
new = cur - timedelta(days = 5)
print(new)

#2
cur = datetime.now()
ye = cur - timedelta(days = 1)
tr = cur + timedelta(days = 1)
print(ye, cur, tr)

#3
cur = datetime.now()
new = cur.replace(microsecond=0)
print(new)

#4
ou = cur - ye
ou = ou.total_seconds()
print(ou)

#Math

#1
import math
deg = int(input("Input degree: "))
rad = math.radians(deg)
print("Ouput radian:", rad)

#2
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
s = 0.5 * (b1 + b2) * h
print("Expected output:", s)

#3
ns = int(input("Input number of sides: "))
ls = int(input("Input length of sides: "))
s = (ns * ls ** 2) / (4 * math.tan(math.pi / ns))
print("Expected output:", s)

#4
bl = int(input("Input length of base: "))
ph = int(input("Input height of parallelogram: "))
s = bl * ph
print("Expected output:", s)

#Parsing

import json

file = open("sample-data.json", "r") 
data = json.load(file) 
file.close()

print("Interface Status")
print("=" * 50)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 50)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "Unknown")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "Unknown")
    mtu = attributes.get("mtu", "Unknown")
    
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")