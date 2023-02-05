class Human:
    # Конструктор объектов класса
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Функция, которая берет объекты класса и выводит их пользователю
    def main_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} лет')


nataly = Human('Nataly', 13)
nataly.main_info()
print(nataly.age)
print(nataly.name)




