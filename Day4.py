Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 1 # int
>>> y = 2.8 # float
>>> z = 1j # complex
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> 
>>> x = 1
>>> y = 35656222554887711
>>> z = -3255522
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> 
>>> x = 1.10
>>> y = 1.0
>>> z = -35.59
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> 
>>> x = 35e3
>>> y = 12E4
>>> z = -87.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> 
>>> x = 3+5j
>>> y = 5j
>>> z = -5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> 
>>> x = 1 # int
>>> y = 2.8 #float
>>> z = 1j # complex
>>> # convert from int to float:
>>> a = float(x)
>>> # convert from float to int:
>>> b = int(y)
>>> # convert from int to complex:
>>> c = complex(x)
>>> print(a)
1.0
>>> print(b)
2
>>> print(c)
(1+0j)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1,10))
9
>>> print(random.randrange(1,10))
7
>>> print(random.randrange(1,10))
7
>>> print(random.randrange(1,10))
9
>>> 
