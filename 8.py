a = -10
print(+a)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if(a > b):
    print(f"First number {a} is greater than second number {b}")
if(a == b):
    print(f'First number {a} is equal to second number {b}')
if(a < b):
    print(f"First number {a} is lower than second number {b}")

print()

b = True
while(b):
    a = input("Whether you enter empty string, tuple (anything) or 0 ('0' true, int(0) false), boolean variable will be false\nEnter any type of data (enter 'Exit' to leave loop): ")
    if a.isdigit():
        a = int(a)
    print(bool(a))
    if a == 'exit':
        b = False
    if a == 'Exit':
        b = False

print()

print("""class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) //False""")

print()

print("""x = 200
print(isinstance(x, int)) //is digit so true""")

print()

print("""+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y""")

print()

print("""=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3""")

print()

print("""==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y""")

print()

print("""and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)""")

print()

print("""is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y""")

print()

print("""in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y""")

print()

print("""& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2""")

print()

print("""()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR""")