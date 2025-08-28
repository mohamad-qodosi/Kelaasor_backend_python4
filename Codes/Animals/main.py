from cat import Cat
from dog import Dog

my_animals = [
    Dog(12, 300000, 'Male', 'German'),
    Cat(12, 300000, 'Male', 'British'),
    Dog(12, 300000, 'Female', 'Bulldog'),
    Cat(12, 300000, 'Male', 'Scottish'),
    Cat(12, 300000, 'Male', 'Persian'),
    Dog(12, 300000, 'Male', 'Huskey'),
]

for animal in my_animals:
    print(animal)
    print(animal.make_sound())