from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    @property
    def food_allowed(self):
        return [Vegetable, Fruit]

    @property
    def weight_increase(self):
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return 'Squeak'

class Dog(Mammal):
    @property
    def food_allowed(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return 'Woof!'

class Cat(Mammal):
    @property
    def food_allowed(self):
        return [Vegetable, Meat]

    @property
    def weight_increase(self):
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return 'Meow'

class Tiger(Mammal):
    @property
    def food_allowed(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return 'ROAR!!!'