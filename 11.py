print("""thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)""")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print()

print("""thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)""")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

print()

print("""thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)""")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print()

print("""thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)""")
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print()

print("""thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)""")
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print()

print("1 - Работает с индексом, 2 - Работает с значением, 3 - Возвращает значение, 4 - Генерирует ошибку, если элемент не найден")
print("""	1	2	3	4
pop()	✅	❌	✅	✅
del	✅	❌	❌	✅
remove()❌	✅	❌	✅""")

print()

print("""thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)""")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print()

print("""thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)""")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print()

print("""thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])""")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print()

print("""thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1""")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print()

print("""thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]""")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]