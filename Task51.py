# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects):
    #for i in range(1,len(objects)):
    # # if characteristic(objects[i]) != characteristic(objects[i -1]):
    # # return False
    # #return True
    # #print(objects)
    # #map_obj = list(map(characteristic, objects))
    # #print(map_obj)
    # #print(set(map_obj))
    # #print(len(set(map_obj)))
    print(len(set(map(characteristic, objects))) == 1)
    return len(set(map(characteristic, objects))) == 1

values = [1, 3, 11, 7]
if same_by(lambda x: x % 2, values): # True - правда - да, False - ложь - нет
    print('same')
else:
    print('different')