class Animal:
    def __init__(self, weight: int, price: int, gender: str):
        self._name = None
        self._weight = weight
        self._price = price
        self._gender = gender

    def set_name(self, name: str) -> None:
        self._name = name

    def set_weight(self, weight: int) -> None:
        self._weight = weight

    def set_price(self, price: int) -> None:
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_weight(self) -> int:
        return self._weight

    def get_price(self) -> int:
        return self._price

    def get_gender(self) -> str:
        return self._gender

    def make_sound(self):
        raise NotImplementedError()

    def __str__(self):
        return f"Animal({self.get_price()})"

class AnimalWithRace(Animal):
    def __init__(self, weight: int, price: int, gender: str, race: str):
        super().__init__(weight, price, gender)
        self._race = race

    def get_race(self) -> str:
        return self._race

class AgedCreature:
    def __init__(self, age: int, max_age) -> None:
        self._age = age
        self._max_age = max_age

    def birthday(self):
        if self._age > self._max_age:
            return False
        self._age += 1
        return True

    def get_age(self) -> int:
        return self._age