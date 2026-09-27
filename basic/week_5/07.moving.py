width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

command = input()

while command != 'Done':
    box_size = int(command)
    free_space -= box_size
    if free_space < 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    command = input()

else:
    print(f'{free_space} Cubic meters left.')
