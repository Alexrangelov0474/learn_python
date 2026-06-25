import random

class Dog:
    def __init__(self, name, breed, age, color,  paws=4,):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.paws = paws

    def bark(self):
        return f'{self.name} says: Woof!'

    def get_info(self):
        return f'{self.name} is a {self.color} {self.breed} and is {self.age} years old, and have {self.paws} paws.'

    def dog_age(self):

dog_name = input()
dog_bread = input()
dog_age = int(input())
colors = ["Black", "White", "Brown", "Golden", "Gray"]
dog_color = random.choice(colors)


first_dog = Dog(dog_name, dog_bread, dog_age,dog_color)
print(f'{first_dog.bark()}\n{first_dog.get_info()}')
