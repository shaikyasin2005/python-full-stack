Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data type conversions
int(10)
10
int(6.5)
6
int('hi')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int('hi')
ValueError: invalid literal for int() with base 10: 'hi'
int(3+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(3+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(10)
10.0
float(2.4)
2.4
float('hi')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float('hi')
ValueError: could not convert string to float: 'hi'
float(5j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(10)
'10'
str(2.5)
'2.5'
str('hi')
'hi'
>>> str(5+4j)
'(5+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(10)
(10+0j)
>>> complex(2.4)
(2.4+0j)
>>> complex('hello')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    complex('hello')
ValueError: complex() arg is a malformed string
>>> complex(3+4j)
(3+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(10)
True
>>> bool(2.4)
True
>>> bool('hi')
True
>>> bool(2j)
True
>>> bool(True)
True
>>> bool(False)
False
