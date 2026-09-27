total_floors = int(input())
room_per_floor = int(input())

for floor in range(total_floors, 0 , -1):
    for rooms in range(room_per_floor):
        if floor == total_floors:
            print(f'L{floor}{rooms}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{rooms}', end=' ')
        elif floor % 2 != 0:
            print(f'A{floor}{rooms}', end=' ')
    print()