#1
#  def count_middle(*args):
#     middle = (sum(args)/len(args))
#     print( middle )
#     return middle 


#2
# def total_mean (num):
#     return abs(num)
# print (total_mean(-15))



#3 
# def max_num(x,y):
#     """This function returns maximum of 2 numbers"""
#     if x>y:
#         print(x)
#     if x==y:
#         print("Equal")
#     else:
#         return y
# print(max_num(98,22))



# 4
# def rectangel(a,b):
#     """This function calculate area of rectangel"""
#     s_rectangel=a*b
#     return s_rectangel

# def triangle(a,b,c):
#     """This function calculate area of triangle"""
#     p=(a+b+c)/2
#     return ((p*(p-a)*(p-b)*(p-c))** 0.5)

# def circle(r):
#     """This function calculate area of circle"""
#     return(3.14*(r**2))



# 5
# def sum_of_numbers():
#     '''Find sum of entered number'''
#     num = input('Enter a number ')
#     sum_1 = 0
#     for i in number:
#         i=int(i)
#         sum_1+=i
#     return sum_1
# print(sum_of_digits())


# 6
def adding(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculator():
 """ Calculator program """
action = input('Please, enter your action: ')
while True:
    if action == 'adding':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(adding(a, b))
        break
    elif action == 'subtraction':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(subtraction(a, b))
        break
    elif action == 'multiplication':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(multiplication(a, b))
        break
    elif action == 'division':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(division(a, b))
        break
    else:
        print('False action')
calculator()