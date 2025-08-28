from animals import AnimalWithRace

class Cat(AnimalWithRace):
    def make_sound(self) -> str:
        return "Meow!"

    def __str__(self):
        return super().__str__().replace("Animal", "Cat")

if __name__ == '__main__':
    my_cat = Cat(12, 300000, 'Male', 'Persian')
    print(my_cat.get_age())
    print(my_cat.get_price())
    print(my_cat.get_gender())
    print(my_cat.get_race())
    print(my_cat)
    print(my_cat.make_sound())
