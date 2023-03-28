# №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

'''
from random import randint # функция регенирует рандомные целые числа
list_1 = [] #создаем пустой список
for _ in range(randint(5, 15)): # от 5 до 15 (длинна диапазона)
    numdber = randint(-10, 10) # само число от -10 до 10
    print(numdber, end = " ") # выводим результат
    list_1.append(numdber) # преобразовываем список в множество 
set_1 = set(list_1) # откидывает повторяющиеся элементы (set уникальные множества)
print()
print(len(set_1)) # функция len указывает кол уникальных элем
'''

from random import randint
list_1 = [randint(-10, 10) for _ in range(randint(5, 15))]
set_1 = set(list_1)
print()
print(len(set_1))