import random


while True:
    try:
        opponents_count = int(input('брой опоненти: '))
        if opponents_count > 0:
            break
        else:
            print("Въведи положително число!")
    except ValueError:
        print("Моля въведи число!")

cars_models = ['mercedes','BMW','audi','toyota','mazda','ferari','lambo','rolls','bentley']
models_bmw = ['M3', 'M5', 'M4', 'X5 M', 'i8']
models_mercedes = ['G-Class','C63','E63','G63','CLS63']
models_audi = ['RS6', 'RS7', 'RS3', 'R8', 'RSQ8']
models_toyota = ['Supra', 'Land Cruiser', 'Corolla', 'Camry', 'GR Yaris']
models_mazda = ['MX-5', 'RX-7', 'RX-8', 'CX-5', 'Mazda 3']
models_ferrari = ['488 GTB', 'F8 Tributo', 'LaFerrari', 'SF90', 'Portofino']
models_lambo = ['Aventador', 'Huracan', 'Urus', 'Gallardo', 'Revuelto']
models_rolls = ['Phantom', 'Ghost', 'Wraith', 'Dawn', 'Cullinan']
models_bentley = ['Continental GT', 'Flying Spur', 'Bentayga', 'Mulsanne', 'Azure']

selected_cars = []

for i in range(opponents_count):
    while True:
        car = input(f'Избери кола {i + 1}: ')
        if car in cars_models:
            break
        else:
            print("Invalid car type!")

    if car == "mercedes":
        models = models_mercedes
    elif car == 'BMW':
        models = models_bmw
    elif car == 'audi':
        models = models_audi
    elif car == 'toyota':
        models = models_toyota
    elif car == 'mazda':
        models = models_mazda
    elif car == 'ferrari':
        models = models_ferrari
    elif car == 'lambo':
        models = models_lambo
    elif car == 'rolls':
        models = models_rolls
    elif car == 'bentley':
        models = models_bentley
    else:
        continue

    if car == 'ferrari' or car == 'lambo':
        car_type = 'Sport'
    elif car == 'bentley' or car == 'rolls':
        car_type = 'Luxury'
    else:
        car_type = 'Regular'

    chosen_model = random.choice(models)
    selected_cars.append((car,chosen_model,car_type))
    print(f'{car} model:', chosen_model)

print('\nВсички избрани коли:')
for car, models, car_type  in selected_cars:
    print(car, "->", models, car_type)
