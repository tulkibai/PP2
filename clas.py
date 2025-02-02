#1
class pupil:
    name = "Alibek"
    surname = "Mambetgazin"
    gpa = 4.0
    iq = 300
    mmr = 11000
    cs = "The global Elite"
    faceit = 10
    grade = 5
    def getString(self):
        self.name = input("Input any name:")
    def printString(self):
        print(self.name.capitalize)

#2
class shape():
    area = 0
    def area(self):
        print(self.area)
class square(shape):
    def __init__(self, len):
        self.length = len
        self.area = len ** 2

#3
class rectangle(shape):
    def __init__(self, len, wid):
        self.length = len
        self.width = wid
    def areacomp(self):
        return self.length * self.width

#4
import math
class point:
    x = 0
    y = 0
    def __init__(self, ix, iy):
        self.x = ix
        self.y = iy
    def show(self):
        print(self.x, self.y)
    def move(self, cx, cy):
        self.x = cx
        self.y = cy
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

#5
class Account:
    owner = "Alibek"
    balance = 0
    def __init__(self, iowner, ibalance):
        self.owner = iowner
        self.balance = ibalance
    def deposit(self, dep):
        self.balance += dep
    def withdraw(self, wthd):
        if wthd <= self.balance:
            self.balance -= wthd
            print("Operation is successful!")
        else:
            print(f"Sorry, insufficient funds in the account, balance is {self.balance}, withdraw is {wthd}")

alibek = Account("Alibek", 1000)
print(alibek.balance)
alibek.deposit(1000)
print(alibek.balance)
alibek.withdraw(3000)
print(alibek.balance)
alibek.withdraw(1000)
print(alibek.balance)

#6
is_prim = lambda n: n > 1 and (n % i != 0 for i in range(2, n))