number_of_lines = int(input())
parking = {}

for _ in range(number_of_lines):
    command = input().split()
    action = command[0]
    if action == 'register':
        name, plate_number = command[1], command[2]
        if name in parking.keys():
            print(f'ERROR: already registered with plate number {plate_number}')
        else:
            parking[name] = plate_number
            print(f'{name} registered {plate_number} successfully')

    elif action == 'unregister':
        name = command[1]
        if name not in parking.keys():
            print(f'ERROR: user {name} not found')
        else:
            del parking[name]
            print(f'{name} unregistered successfully')

for name, plate_number in parking.items():
    print(f'{name} => {plate_number}')

