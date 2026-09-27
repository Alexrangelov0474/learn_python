number_of_lines = int(input())

cars = set()

for line in range(number_of_lines):
    action, plate = input().split(', ')
    if action == 'IN':
        cars.add(plate)

    elif action == 'OUT':
        if plate in cars:
            cars.remove(plate)


if not cars:
    print('Parking Lot is Empty')
else:
    for current_plate in cars:
        print(current_plate)
