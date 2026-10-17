n_rows = int(input())

matrix = []
p_row, p_col = 0, 0
health = 100
stars_count = 0
collected_stars = 0
freeze = False

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n_rows):
    line = list(input())
    if 'P' in line:
        p_row, p_col = row, line.index('P')
        line[p_col] = '-'

    stars_count += line.count('*')
    matrix.append(line)

while health > 0 and collected_stars < stars_count:
    command = input()

    if command == 'end':
        break

    dr, dc = DIRECTIONS[command]
    matrix[p_row][p_col] = '-'

    p_row = (p_row + dr) % n_rows
    p_col = (p_col + dc) % n_rows


    if matrix[p_row][p_col] == '*':
            collected_stars += 1

    elif matrix[p_row][p_col] == 'F':
        freeze = True

    elif matrix[p_row][p_col] == 'G':
        if freeze:
            freeze = False
        else:
            health -= 50

    matrix[p_row][p_col] = 'P'

if health == 0:
    print(f'Game over! Pacman last coordinates [{p_row},{p_col}]')

if stars_count == 0:
    print('Pacman wins! All the stars are collected.')

if health > 0 and collected_stars < stars_count:
    print('Pacman failed to collect all the stars.')

print(f'Health: {health}')

if collected_stars < stars_count:
    print(f'Uncollected stars: {stars_count - collected_stars}')

for row in matrix:
    print(''.join(row))
