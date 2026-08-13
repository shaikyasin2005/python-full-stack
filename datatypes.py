Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a= 10
type(a)
<class 'int'>
>>> b=5.6
>>> type(b)
<class 'float'>
>>> c='hi'
>>> type(c)
<class 'str'>
>>> d="hello"

>>> type(d)
<class 'str'>
>>> e='''how'''
>>> print(type(e))
<class 'str'>
>>> f=5j+6f
SyntaxError: invalid decimal literal
>>> f=5j+6
>>> print(type(f))
<class 'complex'>
>>> g=6i
SyntaxError: invalid decimal literal
>>> g=9d
SyntaxError: invalid decimal literal
>>> g=9z
SyntaxError: invalid decimal literal
>>> g=9j
>>> print(type(g))
<class 'complex'>
>>> h=True
>>> print(type(h))
<class 'bool'>
>>> i=False
>>> print(type(i))
<class 'bool'>
