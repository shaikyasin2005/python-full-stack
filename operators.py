Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a= 20
b= 4
print(a+b)
24
print(a-b)
16
print(a*b)
80
print(a/b)
5.0
print(a//b)
5
print(a**)
SyntaxError: invalid syntax
print(a**b)
160000
print(a%b)
0
print(b%a)
4
print
<built-in function print>


#assignment operators: these are mostly used in loops.
c = 5
d = 6
c+=d
c
11
c-=d
c
5
c*=d
c
30
c/=d
c
5.0
c//=d
c
0.0
c**=d
c
0.0
d**=c
d
1.0
d%=c
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d%=c
ZeroDivisionError: division by zero


#comparison operators: These are mostly used in conditional statements.
a=65
b = 32
a.b
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.b
AttributeError: 'int' object has no attribute 'b'
a>b
True
a<b
False
b>a
False
b<a
True
b==a
False
a==b
False
a!=b
True
a>=b
True
a<=b
False
b>=a
False
b<=a
True
AttributeError: 'int' object has no attribute 'b'
SyntaxError: invalid syntax. Is this intended to be part of the string?


#logicl operators:and,or,not

a=34
b=12
a<b and b>a
False
a<=b and a>=b
False
a!=b and a==b
False
a<b or a>b
True
a==b or a+=b
SyntaxError: 'expression' is an illegal expression for augmented assignment
a==b or a>b
True
not true
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
>>> not False
True
>>> 
>>> 
>>> #Membership operators:in,not in
>>> a=5,6,3
>>> 5 in a
True
>>> 7 in a
False
>>> 9 not in a
True
>>> 5 not in a
False
>>> 
>>> 
>>> #identity operators:is ,is not
>>> a=3
>>> a is int
False
>>> type(a) is str
False
>>> type(a)  is not float
True
>>> type(a) is not int
False
>>> 
>>> 
>>> #bitwise operators:&,|,~,^,!,<<
>>> a = 2
>>> b = 3
>>> bin(a)
'0b10'
