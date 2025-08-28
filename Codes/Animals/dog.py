from animals import AnimalWithRace, AgedCreature


class Dog(AnimalWithRace, AgedCreature):
    def __init__(self, weight: int, price: int, gender: str, race: str, age: int = 0) -> None:
        AnimalWithRace.__init__(self, weight, price, gender, race)
        AgedCreature.__init__(self, age, 14)

    def make_sound(self) -> str:
        return "Woof!"

    def __str__(self):
        return super().__str__().replace("Animal", "Dog")


if __name__ == '__main__':
    my_dog = Dog(12, 300000, 'Male', 'German')
    print(my_dog.get_age())
    print(my_dog.get_price())
    print(my_dog.get_gender())
    print(my_dog.get_race())
    print(my_dog)
    print(my_dog.make_sound())
    for i in range(20):
        print(my_dog.birthday())
        print(my_dog.get_age())
