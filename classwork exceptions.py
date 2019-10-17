# try:
#     num = int(input ("Enter your number: "))
#     if num < 0 :
#         print ("Number couldn't be less then 0")
#     elif num % 2 == 1:
#         print ("This number is odd")
#     else:
#         print ("This number is even")
# except TypeError:
#     print ("Oops type error.")




# n = input("Input entire number: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("\n You entered incorrect data!\n")
#         n = input("Input entire number:\n ")
 
# if n % 2 == 0:
#     print("{0} is the even number.".format(n))
# else:
#     print("{0} is the odd number.".format(n))

#2
# def enter_age():
#     if age < 0:
#         raise ValueError("Age couldn't be less then 0")
#     if age % 2 == 0:
#             print("age is even")
#     else:
#         print("age is odd")

# try:
#     num = int(input("Enter your age: "))
#     enterage(num)
 
# except ValueError as e:
#     print("Only positive integers are allowed!!!", e)
# except:
#     print("something is wrong")

#3
# def divide ():
#     sps = list(map(int(input("Enter two numbers: ").split(','))))
#     if sps == sps[0] and sps[1]:
#         try:
#             result = sps[0] / sps[1]
#             print ("Result is: ", result)
#         except ZeroDivisionError:
#             print("division by zero!")
#         except ValueError:
#             print("Value isn't correct. Please enter integer")
#         finally:
#             print("The end!")
#     else: 
#         print("Enter 2 numbers")
        
#4
class NumberError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

while True:
    try:
        day = int(input("Enter number: "))
        week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
        if day <= 7 and day >= 1:
            print(week.get(day))
        elif day > 7 :
            raise NumberError('Your value is too large! Please enter a smaller number.')
        elif day < 1:
            raise NumberError('Your value is too small! Please enter a larger number.')
    except(ValueError):
        print('Enter number!')
    except NumberError as e:
        print("Error: ", e.data)