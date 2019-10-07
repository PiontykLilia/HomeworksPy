#1завдання
#i=0
#while i < 100:
#    if i % 2 == 0:
#       print (i)
#    i=i+1
#else:
#    print('end')

#i=0
#for i in range(0,100,2)
#    print (i)

#print(list(range(0,100,2)))

#print(list(range(1,100,2)))


#for i in range(0,100):
#    if i % 2 == 0:
#        continue
#        print (i)
#    else:
#        print (i, end=' ')

#3 завдання

#for i in [2,4,66,76,56,55,76,78,88,99]:
#    if i % 2 == 1:
#        break
#    print (i)
#print ('the end')

#list_number=[2,4,6,8,10]
#contain_odd=False
#for item in list_number:
#    if not item % 2 == 0:
#        contain_odd=True
#        break
#if contain_odd:
#    print("There is odd number in the list")
#else:
#    print("There is only even number in the list")

#4 task
#sps=[2,3,4,5,7,8,88]
# print (sps)
# i = 0
# for a in sps:
#     sps[i] = float(a)
#     i = i+1
# print(sps)


# sps = [9,0,7,5,4,3]
# for i in range(len(sps)):
#     sps[i] = float(sps[i])
# print(sps)

#5 task
# fib1 = fib2 = 1
# n = int(input())
# if n < 2:
#     quit()
# print(fib1, end=' ')
# print(fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
# print()

#6 task
# spysok = ['Today','is','Wednesday','have a good day:)']
# for i in spysok:
#     print(i)

#7 task
# spysok = ['Today', 'is', 'Wednesday', 'have a good day']
# for i in spysok:
#     print(i, end = ' # ')

#8 task
import math
n = int(input("Enter your number: "))
if n < 2:
    print("A number must be 2 and more")
    quit()
elif n == 2:
    print("It's prime number")
    quit()
i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("This is composite number")
        quit()
    i += 1
print("It's prime number")