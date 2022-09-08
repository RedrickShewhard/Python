# типы данных int float boolean str list None
a = 1243
value = None
print(type(value))
print(type(a))
str = 'qwerty'
print(str)  # вывод строки

s = "hello 'world'"
ss = 'hello "world"'
sss = 'hello \'wolrd\''  # эскейп-последовательности
print(sss)

print(s, '-', ss, '-', sss)
print('{} - {} - {}'.format(s, ss, sss))
print('{1} - {2} - {0}'.format(s, ss, sss))
print(f'{s} - {ss} - {sss}')  # интерполяция

boo = True
print(boo)

list = []
list1 = [1, 2, 3, 4, 5, 'hello']
col = [1, 2, 3]
print(list, list1, col)

""" print('введите a')
a = int(input())
print('введите b')
b = int(input())
print(a, b)
#print('{} {}' .format(a, b))
#print(f'{a},{b}')
print(a, '+', b, '=', a+b) """
