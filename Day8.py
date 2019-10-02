Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = " Hello, World! "
>>> print(a.strip()) # return "Hello, World!"
Hello, World!
>>> print(a.len())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a.len())
AttributeError: 'str' object has no attribute 'len'
>>> print(len(a))
15
>>> a = "Hello, World!"
>>> print(len(a))
13
>>> print(a.lower())
hello, world!
>>> print(a.upper())
HELLO, WORLD!
>>> print(a.replace("H","J"))
Jello, World!
>>> a = "Hello, World!"
>>> print(a.split(",")) # returns ['Hello', 'World!']
['Hello', ' World!']
>>> 
