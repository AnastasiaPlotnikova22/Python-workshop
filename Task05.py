# Вагоны в электричке пронумерованы натуральными числами, 
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, 
# сколько всего вагонов в электричке. Напишите программу, 
# которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

number_1 = int(input('введите номер вагона i: '))
number_2 = int(input('введите номер вагона j: '))
if number_1 == number_2:
    print('Без дополнительной информации это сделать невозможно')
else:
    print('сколько всего ваговов в электричке', number_1 + number_2 - 1)