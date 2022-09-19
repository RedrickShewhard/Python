from asyncore import write
from dataclasses import dataclass


""" colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
# data.writelines(colors) #без разделений
data.write('\nLINE2\n')
data.write('LINE3\n')
data.close() """

""" with open('file.txt', 'w') as data:
    data.write('line1\n')
    data.write('line2\n') """


""" path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit() """

# import hell as azaza
# azaza.f()

""" def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ... """

# фибоначчи рекурсия
""" def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34 """

# кортежи (неизменяемый список)
""" a = (3, 4)
print(a)
print(a[0]) """
# a[0] = 12 - так работать не будет, т.к. неизменяемый список
# чтобы создать кортеж из одного числа нужно ставить запятую a = (3,)

""" t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support 
item assignment """

""" t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print(type(t))
print(red, green, blue) """

# словари

""" dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)
    print(dictionary[k]) """

# множества 
""" colors = {'red', 'green'}
colors.add('red')
colors.add('pink')
print(colors)
colors.remove('red') #discard для удаления без ошибки
print(colors)
colors.clear()
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a) #замороженное множество, в котором не работают никакие методы
 """

# list1 = [1,2,3,4,5]

# print(len(list1))
# print(list1.pop())
# print(len(list1))
# print(list1.pop(2))
# print(list1)
# print(list1.append(55))
# print(list1)
# print(list1.insert(1, 'poop'))
# print(list1)