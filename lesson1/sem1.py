""" 1. Напишите программу, которая принимает на вход два числа и проверяет, 
является ли одно число квадратом другого.

*Примеры:*

- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет """

# print('введите первое число ')
# a = int(input())
# print('введите второе число ')
# b = int(input())

# if a == b**2:
#     print('yay')
# elif b == a**2:
#     print('yay')
# else:
#     print('nooooo')

""" 2. Напишите программу, которая на вход принимает 5 чисел
 и находит максимальное из них.
Примеры:
- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90 """

# print('введите пять чисел:')
# a = list(input())
# max = a[0]
# for i in a:
#     if i > max:
#         max = i
# print(max)

# другой вариант
# maxx = int(input('Введите число'))
# for _ in range(4):
# n = int(input('Введите число: '))
# if n > maxx:
# maxx = n
# print(maxx)

""" Напишите программу, которая будет на вход принимать число N 
и выводить числа от -N до N
*Примеры:*
- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 """
# a=int(input('Enter number: '))
# for i in range(-a, a+1, 1):
#     print(i)

""" Напишите программу, которая будет принимать на вход дробь 
и показывать первую цифру дробной части числа.
*Примеры:*
- 6,78 -> 7
- 5 -> нет
- 0,34 -> 3 """
# a = str(input('Enter number: '))
# print(a[2])

""" Напишите программу, которая принимает на вход число и проверяет, 
кратно ли оно 5 и 10 или 15, но не 30. """
a = int(input('Enter number: '))
if (a % 10 == 0 and a % 5 == 0 or a % 15 == 0) and a%30 != 0: 
    print('yay') 
else:
    print('nooooo') 
   
