# -------------- ДОМАШНЕЕ ЗАДАНИЕ --------------------------------------------
# Создать окно обозреватель работы со списком:
# При запуске программы:
# 1. Просмотреть имеющийся список.
# 2. Добавить элемент в список.
# 3. Удалить элемент из списка.
# 4. Выйти.
import os


def print_list(array):
    print(array)


def entering_number():
    number = int(input('---------------------------------------------------\n'
                       'Выберите действие из списка ниже ↓ \n'
                       '1. Просмотреть имеющийся список. \n'
                       '2. Добавить элемент в список. \n'
                       '3. Удалить элемент из списка. \n'
                       '4. Отсортировать список по возрастанию.'
                       '5. Выйти. \n'
                       '\033[4m' + 'Введите номер действия:' + '\033[0m' + ' '))
    return number


list_num = []
int_num = None

while int_num != 5:
    try:
        int_num = entering_number()
        if 0 < int_num <= 5:
            if int_num == 1:
                if list_num:
                    os.system('cls')
                    print_list(list_num)
                    continue
                else:
                    os.system('cls')
                    print('-----------------')
                    print('-- Список пуст---')
                    print('-----------------')
                    continue
            elif int_num == 2:
                os.system('cls')
                add_ind = int(input('Введите номер индекса, куда нужно добавить число: '))
                list_num.insert(add_ind, float(input("Введите число которое нужно добавить в список: ")))
                continue
            elif int_num == 3:
                os.system('cls')
                print_list(list_num)
                remove_ind = int(input('Введите номер индекса числа которое нужно удалить: '))
                list_num.pop(remove_ind)
                continue
            elif int_num == 4:
                os.system('cls')
                list_num.sort()
                print_list(list_num)
                continue
            elif int_num == 5:
                os.system('cls')
                print('----- Вы вышли из программы! -----')

        else:
            os.system('cls')
            print('------ Такого номера команды нет! -------')
            continue
    except ValueError:
        os.system('cls')
        print('---------------------------------------------------')
        print('\033[1m' + 'Это не число! Необходимо ввести число! Попробуйте снова!' + '\033[0m')
