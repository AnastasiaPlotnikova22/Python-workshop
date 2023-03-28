# 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
len_list =int(input('Введите размер мвссива: '))
a = []
for _ in range(len_list):
    numdber = randint(0, 10)
    print(numdber, end = " ")
    a.append(numdber)
    
print()
temp = 0
X = int(input('Заданное число для поиска: '))
for i in range(len(a)):
    if (X - a[i]) < X - temp and X -a[i] > 0:
        temp = i
print("->")
print(a[temp])
