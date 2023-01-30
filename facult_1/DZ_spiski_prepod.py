# 1. Написать программу для работы пользователя со списком.
#
# Пользовательский интерфейс должен представлять из себя консольное меню из четырех пунктов:
#
# 1 - Демонстрация списка
#
# 2 - Добавление элемента в конец списка
#
# 3 - Удаление последнего элемента из списка
#
# 4 - Выход
#
# Программа ожидает ввод от пользователя числа от 1 до 4 для перехода к соответствующему действию.
# Реагировать на ввод любых других чисел программа не должна.
# При переходе к каждому из действий пункты меню стираются. Изначально список пуст.
import os
import sys


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_list(my_list):
    clear()
    if len(my_list) == 0:
        print('Your list is still empty')
    else:
        print('Your list is here! Press any key to return')
        print(my_list)

    print('Press any key to return')
    input()


def add_element(my_list):
    clear()
    my_list.append(input('Write here a new element for your list: '))
    print('Well done! Press any key to return')
    input()


def add_element_extra(my_list):
    clear()
    while True:
        index = int(input(f'Input an index for your new element (from 0 to {len(my_list)}):'))

        if index <= len(my_list):
            my_list.insert(index, input('Write here a new element for your list: '))
            break
        else:
            print("Incorrect input!")

    print('Press any key to return')
    input()


def remove_element_extra(my_list):
    clear()
    if len(my_list) == 0:
        print('Our list is empty! Press any key to return')
        input()
        return

    while True:
        index = int(input(f'Input an index of element for removing (from 0 to {len(my_list) - 1}):'))

        if index < len(my_list):
            my_list.pop(index)
            break
        else:
            print("Incorrect index!")

    print('Complete! Press any key to return')
    input()


def list_sorting(my_list):
    clear()
    type_of_sorting = input('Choose a type of sorting: \n'
                            'a - ascending \n'
                            'd - descending\n')

    if type_of_sorting == 'a' or type_of_sorting == 'd':
        my_list.sort()
    if type_of_sorting == 'd':
        my_list.reverse()

    print('Complete! Press any key to return')
    input()


def end_of_program():
    clear()

    if input('Are you sure? Press "y" for exit and "n" for return to main menu.\n') == 'y':
        clear()
        sys.exit()


our_list = []

while True:
    clear()
    print('Welcome to our first program! Here you can do some basic things with list.')
    user_choice = int(input('Choose one of the options:\n'
                            '1 - Show list\n'
                            '2 - Add element into a list\n'
                            '3 - Remove element from a list\n'
                            '4 - Sorting list\n'
                            '5 - Exit \n'))

    if user_choice == 1:
        show_list(our_list)
    elif user_choice == 2:
        add_element_extra(our_list)
    elif user_choice == 3:
        remove_element_extra(our_list)
    elif user_choice == 4:
        list_sorting(our_list)
    elif user_choice == 5:
        end_of_program()