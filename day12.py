Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 =5
>>> num2 = 7

>>> txt = "Please, I want {} sandwishes and {} donutes"
>>> txt = txt.replace("i","we")
>>> txt = txt.format(num1,num2)
>>> txt = txt.replace("a","A")
>>> print(txt)
PleAse, I wAnt 5 sAndwweshes And 7 donutes
>>> 
