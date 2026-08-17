Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 'hello'
a[1]
'e'
a[4]
'o'
a[1]+a[2]+a[3]
'ell'
b = 'Hello ,World!'
b[5]
' '
b[6]
','
c = 'Iam learning python'
c[4]+c[5]+c[6]+c[7]
'lear'
c[4]+c[5]+c[6]+c[7]+c[8]
'learn'
d
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
d = 'codegnan it solutions'
d[0]+d[1]+d[2]+d[3]
'code'
d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'olutions'
d[12]+d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]
'solution'
a = 'time is very precious
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)a = 'time is very preciousa = 'time is very precious
SyntaxError: invalid syntax
a = 'time is very precious'
a[-21]+a[-20]+a[-19]+a[-18]
'time'
a[-16]+a[-15]
'is'
a[-13]+a[-12]+a[-11]+a[-10]
'very'
a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'precious'
#sliceing
a = 'learn coding'
a[0:5]
'learn'
a[6:]
'coding'
a[::-1]
'gnidoc nrael'
a[:6]
'learn '
a ='work until you succeed'
a[0:5]
'work '
a[0:4]
'work'
a[6:11]
'ntil '
a[5:9]
'unti'
a[5:10]
'until'
a[11:14]
'you'
a[15:]
'succeed'
a='vizag is city of destiny'
a[-23:-18]
'izag '
a[-24:-18]
'vizag '
a[-24:-17]
'vizag i'
a[-7,1]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a[-7,1]
TypeError: string indices must be integers, not 'tuple'
a[-7,0]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a[-7,0]
TypeError: string indices must be integers, not 'tuple'
a[-8:-1]
' destin'
a[-7:]
'destiny'
>>> a[-24]
'v'
>>> 
>>> a[-24:]
'vizag is city of destiny'
>>> a
'vizag is city of destiny'
>>> a[-25]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a[-25]
IndexError: string index out of range
>>> a=[-18:-24]
SyntaxError: invalid syntax
>>> a[-18:-24]
''
>>> #striding
>>> a= 'machine learning'
>>> a[::-2]
'gire nha'
>>> a[2:5:2]
'ci'
>>> a[-4:]
'ning'
>>> a[-4:-1]
'nin'
>>> a[-1:-7]
''
>>> a[-7:-1]
'earnin'
>>> a[-1:-7:-1]
'gninra'
