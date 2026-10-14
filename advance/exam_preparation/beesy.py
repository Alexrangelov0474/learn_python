n_rows = int(input())

matrix = []
bee_r, bee_c = 0, 0

for row in range(n_rows):
    line = list(input())
    if 'B' in line:
        bee_r, bee_c = row, line.index('B')
        line[bee_c] = '-'
    matrix.append(line)

bee_energy = 15
energy_restored_flag = False
min_nectar = 30
nectar = 0

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    bee_energy -= 1
    dr, dc = DIRECTIONS[input()]
    bee_r = (bee_r + dr) % n_rows
    bee_c = (bee_c + dc) % n_rows

    cell = matrix[bee_r][bee_c]

    if cell.isdigit():
        nectar += int(cell)
        matrix[bee_r][bee_c] = '-'

    elif  cell == 'H':
        if nectar >= min_nectar:
            print(f'Great job, Beesy! The hive is full. Energy left: {bee_energy}')
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if bee_energy <= 0:
        if not energy_restored_flag and nectar >= min_nectar:
            bee_energy += nectar - min_nectar
            energy_restored_flag = True
            nectar = min_nectar
        else:
            print('This is the end! Beesy ran out of energy.')
            break

matrix[bee_r][bee_c] = 'B'

for row in matrix:
    print(''.join(row))

