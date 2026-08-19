Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a= [12,34.8,'hi',5+j,True,False]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a= [12,34.8,'hi',5+j,True,False]
NameError: name 'j' is not defined
a= [12,34.8,'hi',5+6j,True,False]
a
[12, 34.8, 'hi', (5+6j), True, False]
type(a)
<class 'list'>
#append:it adds single element at the end of the list.
a=[1,24,5,67,8]
a.append(3)
a
[1, 24, 5, 67, 8, 3]
a.append(34,55)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append(34,55)
TypeError: list.append() takes exactly one argument (2 given)
a.append([34,54])
a
[1, 24, 5, 67, 8, 3, [34, 54]]
a.extend([23,89])
a
[1, 24, 5, 67, 8, 3, [34, 54], 23, 89]
#extend:it adds more than one element at the end of the list.synt:var_name.extend([element1,element2....]).
a.extend(12,45)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.extend(12,45)
TypeError: list.extend() takes exactly one argument (2 given)
a.extend([54,56])
a
[1, 24, 5, 67, 8, 3, [34, 54], 23, 89, 54, 56]
#insert:we can insert at particular position using index numbers.
a.insert(3,45)
a
[1, 24, 5, 45, 67, 8, 3, [34, 54], 23, 89, 54, 56]
#index
a=['hi','hello','how']
a.index('hi')
0
b='python'
nb.index('y')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    nb.index('y')
NameError: name 'nb' is not defined. Did you mean: 'b'?
b.index('y')
1
b[4]
'o'
b.clear
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b.clear
AttributeError: 'str' object has no attribute 'clear'
#clear
a
['hi', 'hello', 'how']
a.clear()
a
[]
#sort
a=[34,52,12,4,65,90]
a.sort()
a
[4, 12, 34, 52, 65, 90]
b=['lion','dog','cat','elephant']
a.sort()
a
[4, 12, 34, 52, 65, 90]
b.sort()
b
['cat', 'dog', 'elephant', 'lion']
#pop
a
[4, 12, 34, 52, 65, 90]
a.pop()
90
a
[4, 12, 34, 52, 65]
b
['cat', 'dog', 'elephant', 'lion']
b.pop()
'lion'
b
['cat', 'dog', 'elephant']
#remove
a
[4, 12, 34, 52, 65]
a.remove(12)
a
[4, 34, 52, 65]
a.remove([1])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.remove([1])
ValueError: list.remove(x): x not in list
#reverse
a
[4, 34, 52, 65]
a.reverse()
a
[65, 52, 34, 4]
b
['cat', 'dog', 'elephant']
b.reverse()
b
['elephant', 'dog', 'cat']
del a[1]
a
[65, 34, 4]
a.remove()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
#pop
b
['elephant', 'dog', 'cat']
b.pop(1)
'dog'
b
['elephant', 'cat']
a.pop(1)
34
a
[65, 4]
a.extend([23,45,45,67,21])
a
[65, 4, 23, 45, 45, 67, 21]
a.remove(45)
a
[65, 4, 23, 45, 67, 21]
a.pop(1,4)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.pop(1,4)
TypeError: pop expected at most 1 argument, got 2
a.pop(4)
67
a
[65, 4, 23, 45, 21]
#len()
a
[65, 4, 23, 45, 21]
len(a)
5
b='hello'
len(b)
5
#count
a.count(23)
1
#tuple: it is immutalbe
a=(12,3.4,"hi",5j,True,False)
type(a)
<class 'tuple'>
a.count('hi')
1
a.index(5j)
3
len(a)
6



#sets{}
#set is unordered and semi mutable
a={23,45,12,56}
a
{56, 12, 45, 23}
type(a)
<class 'set'>
b={34,56,23,34,5612}
b
{56, 34, 5612, 23}
#subset
a={1,2,3,4,5,6}
b={4,5,6}
a.issubset(b)
False
b.issubset(a)
True
#issuperset()
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a.union(b)
{1, 2, 3, 4, 5, 6}
a
{1, 2, 3, 4, 5, 6}
b
{4, 5, 6}
a={23,56,12,34,4}
b={45,231,45,12,4}
a.unoin(b)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.unoin(b)
AttributeError: 'set' object has no attribute 'unoin'. Did you mean: 'union'?
a.union(b)
{34, 4, 231, 12, 45, 23, 56}
a.intersection(b)
{4, 12}
#intersectio():common elements in both sets.
b.intersection(a)
{4, 12}
#update:completely upddate the set.where union just merges the sets i does not update sets.
a
{34, 4, 23, 56, 12}
b
{45, 4, 12, 231}
a.update(b)
a
{34, 4, 231, 12, 45, 23, 56}
b.update(a)
b
{34, 4, 231, 12, 45, 23, 56}
#difference()
a={1,2,3,4,5,6,7,8,9}
b={7,8,9,12,13,14,15,16}
a.difference(b)
{1, 2, 3, 4, 5, 6}
b.difference(a)
{12, 13, 14, 15, 16}
a.symmetric_difference(b)
{1, 2, 3, 4, 5, 6, 12, 13, 14, 15, 16}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16}
a.difference_update(b)
a
{1, 2, 3, 4, 5, 6}
b.difference_update(a)
a
{1, 2, 3, 4, 5, 6}
b
{7, 8, 9, 12, 13, 14, 15, 16}
#intersection_update()
a={1,2,3,7,8,9,4}
b={4,5,7,1,12}
a.intersection_update(b)
a
{1, 4, 7}
b.intersection_update(a)
a
{1, 4, 7}
b
{1, 4, 7}
#symetric_difference_update()
a={3,4,5,6,8,9,1}
b={12,5,6,2,4,9}
a.symmetric_difference_update(b)
a
{1, 2, 3, 8, 12}
b.symmetric_difference_update(a)
b
{1, 3, 4, 5, 6, 8, 9}
#pop
a
{1, 2, 3, 8, 12}
a.pop()
1
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a
{2, 3, 8, 12}
#remove()
a.remove(8)
a
{2, 3, 12}
#add
a={12,34,55}
a.add(20)
a
{34, 12, 20, 55}
#clear
a.clear()
a
set()
a=set()
a.add(20,40)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    a.add(20,40)
TypeError: set.add() takes exactly one argument (2 given)
a.add(40)
a
{40}
>>> #len()
>>> b
{1, 3, 4, 5, 6, 8, 9}
>>> len(b)
7
>>> b.count(6)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    b.count(6)
AttributeError: 'set' object has no attribute 'count'
>>> b.index(8)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    b.index(8)
AttributeError: 'set' object has no attribute 'index'
>>> #set is unordered and no duplicates are allowed so count and index doesnt work.
>>> 
>>> #isdisjoint()
>>> #all diffrent values means disjoint.
>>> 
>>> a={1,2,3,4,5}
>>> b={6,7,8,9}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(b)
False
