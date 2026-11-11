from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def food_allowed(self):
        return [Meat]

    @property
    def weight_increase(self) :
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return 'Hoot Hoot'

class Hen(Bird):
    @property
    def food_allowed(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def weight_increase(self):
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return 'Cluck'


