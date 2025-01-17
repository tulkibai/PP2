"""
Both variants are eligible
print("Hello")
print('Hello')
"""

#Quotation
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = input("Enter string: ")
print(a)

#Multiple line string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = input("Enter string: ")
print("Char at 2 position is:", a[1])
for x in a:
    print(x)
print("String length = ", len(a))

txt = "The best things in life are free!"
print(txt)
print('Is "free" in txt?')
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print(txt)
print('Is "expensive" not in txt?')
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

b = input("Enter string with at least 6 chars: ")
print("Slice of string from 3-rd position to 5th:", b[2:5])
print("Slice of string from start to 5th:", b[:5])
print("Slice of string from 3-rd position to end", b[2:])
print("Slice of string from 5-th position fom the end to 3-rd from the end", b[-5:-2])

a = input("Enter strings: ")
print(a.upper())

a = input("Enter upper-case strings: ")
print(a.lower())

a = " Hello, World! "
print("Strip")
print(a)
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print("Replacing")
print(a)
print(a.replace("H", "J"))

a = "Hello, World!"
print("Splitting")
print(a.split(",")) # returns ['Hello', ' World!']

print("Concatenation")
a = "Hello"
b = "World"
print('a = "Hello" b = "World"')
c = a + b
print('c = a + b', c)
a = "Hello"
b = "World"
print(a, b)
c = a + " " + b
print('c = a + " " + b', c)

print("F-strings")
age = 36
txt = f"My name is John, I am {age}"
print('f"My name is John, I am {age}"')
print(txt)

print("Placeholders and Modifiers")
price = 59
txt = f"The price is {price} dollars"
print('txt = f"The price is {price} dollars"')
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print('txt = f"The price is {price:.2f} dollars"')
print(txt)

txt = f"The price is {20 * 59} dollars"
print('txt = f"The price is {20 * 59} dollars"')
print(txt)

print(r'txt = "We are the so-called \"Vikings\" from the north."')
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print("\n" * 10)

print(r"""\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value""")

print("\n" * 10)

print("""capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning""")