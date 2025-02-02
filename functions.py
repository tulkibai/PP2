#1
def grtou(mass): #from grams to ounces 
    return mass * 28.3495231 

#2
def fatce(temp): #from fahrenheit centigrade 
    return (5 / 9) * (temp - 32)

#3
def solver(heads, legs): #a program to solve a classic puzzle: 
    #We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have
    return [2 * heads - 0.5 * legs, 0.5 * legs - heads]

#4
def prime(list):
    k = 0
    res = []
    flak = True
    for i in list:
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                flak = False
        if flak:
            res.append(i)
        flak = True
    return res

#5
from itertools import permutations
def permu(string):
    perms = [p for p in permutations(string)]
    return perms

#6
def revrs(string):
    list = string.split()
    k = len(list)
    for i in range(k - 1, -1, -1):
        print(list[i], end = " ")
    return ""

#7
def has33(list):
    k = len(list)
    for i in range(0, k):
        if i == 0:
            prev = list[0]
            continue
        if list[i] == 3 and prev == 3:
            return True
        prev = list[i]
    return False
#8
def has007(list):
    k = len(list)
    res = []
    for i in range(0, k):
        if list[i] == 0 or list[i] == 7:
            res.append(list[i])
    if res[0] == res[1] == 0 and res[2] == 7:
        return True
    else:
        return False

#9
import math
def vol(r):
    return math.pi * (r ** 3)

#10
def uniq(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    res = [0 for i in range(max + 1)]
    ans = []
    for i in list:
        res[i] += 1
    k = len(res)
    for i in range(0, k):
        if res[i] != 0:
            ans.append(i)
    return ans

#11
def palindrom(string):
    k = len(string)
    for i in range(0, k):
        if string[i] == string[k - 1 -i]:
            continue
        else:
            return False
    return True

#12 
def histogram(list):
    for i in list:
        for j in range(i):
            print('*', end = '')
        print(" ")
    return ""
#13
import random
def guesser():
    x = random.randint(1, 20)
    k = 1
    name = input("Hello! Whar is your name? ")
    guess = int(input(f'''Well, {name}, I am thinking of a number between 1 and 20.
Take a guess. '''))
    flak = True
    if guess == x:
        print(f"Good job, {name}! You guessed my number in {k} guesses!")
        flak = False
    elif guess < x:
            print('Your guess is too low.')
    else:
        print('Your guess is too high.')
    while(flak):
        k += 1
        guess = int(input("Take a guess  "))
        if guess == x:
            print(f"Good job, {name}! You guessed my number in {k} guesses!")
            flak = False
        elif guess < x:
            print('Your guess is too low.')
            continue
        else:
            print('Your guess is too high.')
            continue
    return ""