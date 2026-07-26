towns = {}
while True:
    lines = input().split('||')
    if lines[0] == 'Sail':
        break
    town,citizen,gold = lines[0], int(lines[1]), int(lines[2])
    if town not in towns.keys():
        towns[town] = {
        'citizens':citizen,
        'gold':gold
        }
    else:
        town_data = towns[town]
        town_data['citizens'] += citizen
        town_data['gold'] += gold

while True:
    command = input().split('=>')
    if command[0] == 'End':
        break

    action = command[0]
    if action == 'Plunder':
        town, peoples_killer, gold = command[1], int(command[2]), int(command[3])
        town_data = towns[town]
        town_data['citizens'] -= peoples_killer
        town_data['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {peoples_killer} citizens killed.')
        if town_data['citizens'] <= 0 or town_data['gold'] <= 0:
            print(f'{town} has been wiped off the map!')
            del towns[town]



    if action == 'Prosper':
        town, gold = command[1], int(command[2])
        town_data = towns[town]
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            town_data['gold'] += gold
            current_gold = town_data['gold']
            print(f'{gold} gold added to the city treasury. {town} now has {current_gold} gold.')


if not towns:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    towns_left = len(towns)
    print(f'Ahoy, Captain! There are {towns_left} wealthy settlements to go to:')
    for town, data in towns.items():
        population = data['citizens']
        gold = data['gold']
        print(f'{town} -> Population: {population} citizens, Gold: {gold} kg')
