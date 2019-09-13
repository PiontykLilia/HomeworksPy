Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Задано чотирицифрове натуральне число. 
#Знайти добуток цифр цього числа.
#Записати число в реверсному порядку.
#Посортувати цифри, що входять в дане число
a=input('Please type 4-digit number: ')
Please type 4-digit number: 5643
>>> print('Product is ', int(a[0])*int(a[1])*int(a[2])*int(a[3]))
Product is  360
>>> print ('Reverse is',  a[3], a[2], a[1], a[0])
Reverse is 3 4 6 5
>>> sorted(a)
['3', '4', '5', '6']
>>> 
