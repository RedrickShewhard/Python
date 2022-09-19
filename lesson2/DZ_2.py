""" Напишите программу, которая принимает на вход вещественное число
 и показывает сумму его цифр
Пример:
- 6782 -> 23
- 0,56 -> 11 """

# n = (input("enter number: "))
# list_n= list(n)
# sum = 0
# for i in list_n:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)

""" Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

# from math import factorial


# n = int(input("enter number: "))
# list = []
# for i in range(1, n+1):
#     list.append(factorial(i))
# print(list)

""" Задайте список из n чисел последовательности $(1+\ frac 1 n)^n$ 
и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} """

# n = int(input())
# some_dict = {}
# summ=0
# for i in range(1, n + 1):
#     some_dict[i] = (1+1/i)**i
#     summ+=some_dict[i]
# print(some_dict)

""" Реализуйте алгоритм перемешивания списка. """

# from random import shuffle

# list_1 = [2, 4, 6, 8]
# shuffle(list_1)
# print(list_1)