# print(numbers[2])
#
# a = 5
# b = 3
# (a, b) = (b, a)

# numbers = (1, 2, 3, 4, 5)
# num = int(input())
#
# if num in numbers:
#     print('first option')
# else:
#     print('second option')

#############################
# Словари
# character = {
#     'name': "Айрат",
#     'class': "cartoon character",
#     'age': 36
# }
#
# character['sex'] = 'male'   # Добавление нового элемента в словарь
# character.pop('class')  # Удаление последнего элемента словаря (если указать ключ, то удалит именно его)
#
# # Цикличная обработка словарей
# for key in character:
#     print(key)
#     print(character[key])
#
# # Доступ к ключу и содержимому сразу
# for (key, item) in character.items():
#     print(key, '-', item)
#
#
# print(character)

###############################
# Множества
# names = {'Pavel', 'Dmitry', 'Mihail'}
#
# print(names)
#
# names.add('Airat')
#
# print(names)
#
# if 'Alex' in names:
#     print("Элемент есть")
# else:
#     print("Элемента нет")

###
# names1 = {'Pavel', 'Dmitry', 'Mihail'}
# names2 = {'Olga', 'Nataly', 'Dmitry'}
#
# n1 = names1.union(names2)  # Объединение множеств (не будет повторяющихся элементов)
# n2 = names1.intersection(names2)  # Пересечение множеств (выдаст только то, что повторяется в обоих множествах)
#
# print(n1)
# print(n2)
##################################

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3 or len(name) > 8:
            print("Не корректная длина имени!")
        else:
            self.__name = name
            print('Обновление имени успешно выполнено!')

    def __str__(self):
        return f'Всем привет, меня зовут {self.__name} и мне {self.age} лет.'


class Worker(Human):
    def __init__(self, name, age, specialty='Unknown', xp=0):
        super().__init__(name, age)
        self.specialty = specialty
        self.xp = xp

    def __str__(self):
        return super().__str__() + f'\nЯ работаю по специальности {self.specialty} уже {self.xp} лет.'


dima = Worker('Dmitry', 35, 'Programmer', 10)
pavel = Human('Pavel', 19)

dima.name = 'Dima'
print(dima.__str__())
