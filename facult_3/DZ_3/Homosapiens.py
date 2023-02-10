class Homosapiens():
    def __init__(self, name, age, gender, nation, ):
        self.name = name  # имя
        self.age = age  # возраст
        self.gender = gender  # пол
        self.nation = nation  # нация

    def get_name(self):
        """Метод выводит имя экземпляра класса"""
        print(f'{self.name}')

    def adult(self):
        """Метод определяет, является ли экземпляр класса совершеннолетним"""
        if self.age >= 18:
            print("Человек совершеннолетний, ему 18 и более лет!")
        else:
            print("Человек ещё не совершеннолетний")

    def went_to_work(self):
        """Метод выводит, что экземпляр класса пошел на работу"""
        print(f'{self.name} пошёл на работу зарабатывать деньги')

    def resting_at_home(self):
        """Метод выводит, что экземпляр класса отдыхает дома"""
        print(f'{self.name} отдыхает дома')

    def get_gender(self):
        """Метод класса который выводит пол экземпляра класса"""
        print(f'{self.name} - имеет пол {self.gender}')

    def changed_nation(self):
        """Метод показывает - хочет ли экземпляра класса сменить национальность"""
        if self.nation == "Русский":
            self.nation = "хочет сменить свою религию на Мусульманин"
            print(f'{self.name} {self.nation}')
        else:
            self.nation = "- не хочет менять свою религию"
            print(f'{self.name} {self.nation}')


ivan = Homosapiens("Иван", 23, "Мужской", "Русский")

ivan.get_name()
ivan.adult()
ivan.get_gender()
ivan.went_to_work()
ivan.resting_at_home()
ivan.changed_nation()

ruslan = Homosapiens("Руслан", 15, "Мужской", "Мусульманин")
ruslan.get_name()
ruslan.adult()
ruslan.get_gender()
ruslan.went_to_work()
ruslan.resting_at_home()
ruslan.changed_nation()


