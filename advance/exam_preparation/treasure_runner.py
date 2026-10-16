n_rows = int(input())

p_row, p_col = 0, 0
matrix = []

for row in range(n_rows):
    line = list(input())
    if 'P' in line:
        p_row, p_col = row, line.index('P')
        line[p_col] = '.'
    matrix.append(line)

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

n_commands = int(input())

game_over = False
treasure = 0

for _ in range(n_commands):
    dr, dc = DIRECTIONS[input()]
    new_row, new_col = p_row + dr, p_col + dc
    if 0 <= new_row < n_rows and 0 <= new_col < n_rows and matrix[new_row][new_col] != '#':
        matrix[p_row][p_col] = '.'

        if matrix[new_row][new_col] == 'E':
            matrix[new_row][new_col] = 'P'
            game_over = True
            print(f'Exit reached! Coins collected: {treasure}')
            break

        if matrix[new_row][new_col] == 'C':
            treasure += 1

        matrix[new_row][new_col] = 'P'
        p_row, p_col = new_row, new_col

if not game_over:
    print(f'Exploration finished. Coins collected: {treasure}')

for line in matrix:
    print(''.join(line))
