# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n =int(input('Введите трёхзначное число:'))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print('Сумма:', sum)