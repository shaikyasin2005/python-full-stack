Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a = 'iam learning python'
len(a)
19
b = 'how are you?'
len(b)
12
c = a+b
len(c)
31
d = ''
len(d)
0
e = ' '
len(e)
1
#count()
#count():it is used to count the repeated characters or words in the given string
a = 'twinkle twinkle little star'
a.count('twinkel')
0
a.count('twinkle')
2
a.count('t')
5
a.count(' ')
3
#find a string: it is used to find the index of the given letter or word in the string find()
a = 'hello world'
a.find('o')
4
a.find('d')
10
a[2:4]
'll'
#escape sequences: \n : new line , \t : tab space
a = 'name:yasin\ncity:gnt\tpin:522034'
print(a)
name:yasin
city:gnt	pin:522034
#replace:we can replacd the words in string.
a = 'are you doing well'
a.replace('are','well')
'well you doing well'
print(a)
are you doing well
b = a.replace('are','well')
b
'well you doing well'
b.replace('well','welcome')
'welcome you doing welcome'
#upper(): make all letters in the string to upper means capital letters.
a = 'yasin'
a.upper()
'YASIN'
#captalize(): it is used to make the first letter captial in the string.
a.capatalize()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'. Did you mean: 'capitalize'?
a.captalise()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.captalise()
AttributeError: 'str' object has no attribute 'captalise'. Did you mean: 'capitalize'?
a.capitalize()
'Yasin'
#title(): it is used to make the each words first letter capital
a = 'iam a student'
a.title()
'Iam A Student'
#isupper(),isdigit(),isalpha(),isalnum()
a = 'hi'
a.isupper()
False
a.islower()
True
b = 'python4.0'
a.isdigit()
False
a.isalnum()
True
a.isalpha()
True
b.isalnum()
False
b = 'python4'
b.isalnum()
True
#conctination: udsed to add to strings.
fname = 'yasin'
lname = 'shaik'
print(fname+lname)
yasinshaik
print(fname+' '+lname)
yasin shaik
print((fname+' '+lname).capitalize())
Yasin shaik
print((fname+' '+lname).title())
Yasin Shaik
#split():it is used to remove the spaces in the string.
#there are two types of strip 1.lstrip():remove left spaces,2.rstrip():remove right spaces.
a = '   yasin   '
a.strip()
'yasin'
a.lstrip()
'yasin   '
a.rstrip()
'   yasin'
#split : it is used to split the string by default it splits at spaces.
a = 'iam learning python'
a.split()
['iam', 'learning', 'python']
a.split('a')
['i', 'm le', 'rning python']
a.split('a',1)
['i', 'm learning python']
#split('particular letter or symbool',at how many numbers)
#join(): used to join the strings.
a = 'iam learning str methods'
a.join()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
a = 'iam,learning,str,methods'
a.join()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
a = 'iam','learning','str','methods'
a.join()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.join()
AttributeError: 'tuple' object has no attribute 'join'
>>> ''.join(a)
'iamlearningstrmethods'
>>> #formating:used to add the additional string.
>>> a = 10
>>> b = 12
>>> c = a+b
>>> print('sum of a+b is:',c)
sum of a+b is: 22
>>> #f-string
>>> print(f'sum of a+b is {c}')
sum of a+b is 22
>>> print('sum of a+b is {}'.format(c))
sum of a+b is 22
>>> d = a-b
>>> print('sum of a+b is {} and a-b is {}'.format(c,d))
sum of a+b is 22 and a-b is -2
>>> print('sum of a+b is {} and a-b is {}'.format(d,c))
sum of a+b is -2 and a-b is 22
>>> print('sum of a+b is {c} and a-b is {d}'.format())
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print('sum of a+b is {c} and a-b is {d}'.format())
KeyError: 'c'
>>> print(f'sum of a+b is {\'c\'}')
SyntaxError: unexpected character after line continuation character
>>> print(f'sum of a+b is \'{c}\'')
sum of a+b is '22'
