Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#varibles
a=10
b=20
print(a+b)
30
c=1,2,3,4
print(c)
(1, 2, 3, 4)
print(c)
(1, 2, 3, 4)
>>> d,e,f=(23,45,67)
>>> print(d,e,f)
23 45 67
>>> a='hi'
>>> print(a)
hi
>>> a
'hi'
>>> b='hello'
>>> print(a+b)
hihello
>>> print(a,' ',b)
hi   hello
>>> print(a,' ',b)
hi   hello
>>> print(f'{a} yasin {b}')
hi yasin hello
>>> '''rules for variables:
...    1.does not start with numbers
...    2.does not start with special characters
...    3.does not start with keywords
...    4.variables are case sensitive
...    5.varibles can have a-z,A-Z,0-9
...    6.dont use spaces between variables ,instead of it use underscore'''
'rules for variables:\n   1.does not start with numbers\n   2.does not start with special characters\n   3.does not start with keywords\n   4.variables are case sensitive\n   5.varibles can have a-z,A-Z,0-9\n   6.dont use spaces between variables ,instead of it use underscore'
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
