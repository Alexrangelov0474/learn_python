number_of_cars = int(input())
cars = {}
for data in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = {
        'mileage':int(mileage),
        'fuel': int(fuel)
    }

while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break

    action = command[0]
    if action == 'Drive':
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car]['fuel'] > fuel:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if cars[car]['mileage'] >= 100000:
                print(f'Time to sell the {car}!')
                del cars[car]
        else:
            print('Not enough fuel to make that ride')

    elif action == 'Refuel':
        car, fuel = command[1], int(command[2])
        current_fuel = cars[car]['fuel']
        if current_fuel + fuel > 75:
            cars[car]['fuel'] = 75
            fuel_added = 75 - current_fuel
        else:
            fuel_added = fuel
            cars[car]['fuel'] += fuel
        print(f'{car} refueled with {fuel_added} liters')

    elif action == 'Revert':
        car, kilometers = command[1], int(command[2])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

for car, data in cars.items():
    mileage = data['mileage']
    fuel = data['fuel']
    print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')