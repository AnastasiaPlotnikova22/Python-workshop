# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - изменение данных
6 - удаление''')
    user_input = input('Введите нужный вариант: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        change_person()
    elif user_input == '6':
        delete_contact()


def add_person():
    last_name = input('Введите фамилию: ')  # 'Иванов'
    name = input('Введите имя: ')  # 'Иван'
    surname = input('Введите отчество: ')  # 'Иванович'
    phone = input('Введите номер телефона: ')  # '9784561230'
    data = open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([last_name, ' ', name, ' ', surname, ' ', phone, '\n'])# 1-й вар.
    #data.writelines([last_name + ' ', name + ' ', surname + ' ', phone]) #2-й вар.
    data.close()
add_person()


def print_data():
    with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())
print_data()


def search():
    search_name = input('Введите данные: ')
    with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)
#search()


def load_data():
    with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'r+', encoding='utf-8')as data:
        text_data = data.read().splitlines()
        path = input("Укажите путь к импортируемому файлу: ")
        with open(path, 'r', encoding="utf-8") as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line)

                    
def change_person():
change_name = input('Введите данные контакта, который хотите изменить: ')
last_name = input('Введите новую фамилию: ')
name = input('Введите новое имя: ')
surname = input('Введите новое отчество: ')
phone = input('Введите новый номер телефона: ')

with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'r', encoding='utf-8') as data:
    d = data.readlines()
for i_line in range(len(d)):
    if change_name in d[i_line]:
        d[i_line] = last_name + ' ' + name + ' ' + surname + ' ' + phone

with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'w', encoding='utf-8') as data:
          for line in d:
              data.write(line) 


def delete_contact():
    del_name = input("Введите данные контакта: ")
    with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for i_line in range(len(d)):
            if del_name in d[i_line]:
                del d[i_line]
    with open('G:\\GeekBrains\\Знакомство с языком Pyton\\Seminar pt\\phonebook.txt', 'w', encoding='utf-8') as data:
        print(d)
        for line in d:
            data.write(line)

def main():
    ui()

if __name__ == "__main__":
    main()