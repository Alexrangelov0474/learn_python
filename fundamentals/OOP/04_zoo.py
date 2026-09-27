class Zoo:
    __animals = 0
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species_type, name):
        if species_type == 'mammal':
            self.mammals.append(name)
        elif species_type == 'fish':
            self.fishes.append(name)
        elif species_type == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species_type):
        message = ''
        if species_type == 'mammal':
            message += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species_type == 'fish':
            message += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species_type == 'bird':
            message += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        message += f'Total animals: {Zoo.__animals}'
        return message

zoo = input()
name_of_the_zoo = Zoo(zoo)
count = int(input())
for number in range(count):
    animals = input().split()
    species = animals[0]
    animal = animals[1]
    name_of_the_zoo.add_animal(species, animal)

info = input()
print(name_of_the_zoo.get_info(info))
