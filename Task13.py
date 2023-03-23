# Пользователь вводит число N (1 ≤ N ≤ 10). 
# Далее построчно N чисел от -50 до 50.
# Нужно вывести наибольшее количество идущих подряд положительных чисел.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


n = int(input("Введите число от 0 до 10 "))
count = 0
count_max = 0

for _ in range(n):
    c = int(input())  # если нужно рандомно генерировать числа c = randint(-50, 50)
    if c > 0:
        count += 1
        if count > count_max:
            count_max = count
    else:
        count = 0

print("Наибольшее число идущих подряд положительных чисел", count_max)