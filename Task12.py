# 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 2) Пользователь вводит два числа построчно, 
# первое – сумма двух чисел, второе – произведение этих чисел.
# Нужно вывести исходные числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

'''
s = int(input("Введите сумму двух чисел: "))
p = int(input("Введите произведние двух чисел: "))

y = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
x = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
if s == x + y and p == x * y:
    print(x, y)
else:
    print("No")
'''

s = int(input("Введите сумму двух чисел: "))
p = int(input("Введите произведние двух чисел: "))
for i in range(s):
    for j in range(p):
        if (s == i + j and p == i * j):
            print(i, j)