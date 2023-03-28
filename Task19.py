#  №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

'''
list_1 = []
for i in range(1, 6):
    list_1.append(i)
print(list_1)
k = int(input("Введите число сдвига:"))
for i in range(k): 
    # list_1.pop(0) удаляет первый элемент
    list_1.append(list_1.pop(0))
print()
print(list_1)
'''


len_list =int(input('Введите размер мвссива: '))
k = int(input('Введите сдвиг k элементов:'))
a = []
b = []

for _ in range(len_list):
    c = int(input('Значение массива: '))
    a.append(c)
print(a)
print()
print("Результат:")
for i in range(1, len_list + 1):
    b.append(a[i - k])
print(b)


''''
mas = [1, 2, 3, 4, 5]
k = int(input("k "))

for _ in range(k): #цикл пойдет влево/вправо на то число которое вводит пользователь
    mas.insert(0, mas.pop()) # добавлябю последнй элемент в начало
print(mas)
'''
'''
list = [1, 2, 3, 4, 5]
print(list)
K = 3

temp = list[K:]
list[K:] = list[:K]
list[:K] = temp

print(list)
'''

'''
list = [1, 2, 3, 4, 5]
print(list)
K = 3
list[K:], list[:K] = list[:K], list[K:]
print(list)
'''
'''
list = [1, 2, 3, 4, 5]
print(list)
K = 3
print(list[K:] + list[:K])
'''