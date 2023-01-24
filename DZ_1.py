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
                       '4. Выйти. \n'
                       '\033[4m' + 'Введите номер действия:' + '\033[0m' + ' '))
    return number


list_num = []
int_num = None

while int_num != 4:
    try:
        int_num = entering_number()
        if 0 < int_num <= 4:
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
                list_num.insert(0, float(input("Введите число которое нужно добавить в список: ")))
                continue
            elif int_num == 3:
                os.system('cls')
                print_list(list_num)
                list_num.remove(float(input("Введите число которое нужно удалить из списка: ")))
                continue
            elif int_num == 4:
                os.system('cls')
                print('----- Вы вышли из программы! -----')

        else:
            os.system('cls')
            print('------ Такого номера команды нет! -------')
            continue
    except ValueError:
        os.system('cls')
        print('---------------------------------------------------')
        print('\033[1m' + 'Это не число! Необходимо ввести целое число от 1 до 4 !' + '\033[0m')
