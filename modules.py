# import random
# number=random.randint(1,100)
# while True:
#     guess=input("Please guess the number between 1 and 100:\n")
#     i=int(guess)
#     if i==number:
#         print("You guessed!!!")
#         break
#     elif i<number:
#         print("Choose a larger number")
#     elif i>number:
#         print("Choose a smaller number")

#2 Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
from math import pow
from math import pi
def rectangle_area(a,b):
    r_area = a * b
    print(r_area)
    return r_area

def triangle_area(h, a):
    t_area = 0.5 * h * a
    print(t_area)
    return t_area

def circle_area(r):
    c_area = round(pi * pow(r, 2), 3)
    print(c_area)
    return c_area


circle_area(2)
