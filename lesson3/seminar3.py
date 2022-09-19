# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

""" from time import time_ns

a = time_ns()
a = a%1000000
a = round(a/100) 
print (a) """

# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.


""" from ast import Return


list1 = []
dgt = False
for i in range(3):
    list1.append(input('enter list: '))
for i in range(len(list1)):
    dgt = list1[i].isdigit()
    if (dgt):
        print('yes')
        break
if (not dgt):
    print('no') """


#3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

""" list1=[]
t = tuple(['trt', 'alal', 'trt'])
a = input('find: ')
for i in range(len(t)):
    if t[i] == a:
        list1.append(i)
if len(list1)>1:
    print(list1[1])
else:
    print('no') """