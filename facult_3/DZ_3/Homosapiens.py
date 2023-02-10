class Homosapiens():
    def __init__(self, name, age, gender, nation, ):
        self.name = name  # имя человека
        self.age = age  # возраст человека
        self.gender = gender  # пол человека
        self.nation = nation  # нация человека

    def get_name(self):
        print(f'{self.name}')

    def adult(self):
        if self.age >= 18:
            print("Человек совершеннолетний, ему 18 и более лет!")
        else:
            print("Человек ещё не совершеннолетний")

    def went_to_work(self):
        print(f'{self.name} пошёл на работу зарабатывать деньги')

    def resting_at_home(self):
        print(f'{self.name} отдыхает дома')

    def changed_gender(self):
        if self.gender == "Мужской":
            self.gender = "сменил свой пол на женский"
            print(f'{self.name} {self.gender}')
        else:
            self.gender = "- не менял свой пол"
            print(f'{self.name} {self.gender}')

    def get_nation(self):
        print(f'{self.name} - {self.nation}')


ivan = Homosapiens("Иван", 23, "Мужской", "Русский")

ivan.get_name()
ivan.adult()
ivan.get_nation()
ivan.went_to_work()
ivan.resting_at_home()
ivan.changed_gender()

