# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 2) Пользователь вводит число n. 
# На следующих строках нужно вводить 1 или 0, 
# в ответе вывести количество наименее встречающихся из них 
# (т.е либо количество 0 либо 1, в зависимости от того, кого меньше)

# 5 -> 1 0 1 1 0
# 2

n = int(input("Введите число : "))
most_common = None # наиболее часто встречаемое значение
qty_most_common = 0 # его количество

for _ in range(n):
    c = int(input())
    for item in c:
        qty = c.count(item)
        if qty > qty_most_common:
            qty_most_common = qty # заменяем на него максимальное,
            most_common = item # запоминаем само значение
            print(most_common)