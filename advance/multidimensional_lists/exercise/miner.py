from collections import deque

field_size = int(input())
commands = input().split()

matrix = []
coal_count = 0
miner_row = 0
miner_col = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(field_size):
    current_row = input().split()
    matrix.append(current_row)

    for col in range(field_size):
        if current_row[col] == 's':
            miner_row = row
            miner_col = col
        elif current_row[col] == 'c':
            coal_count += 1

for command in commands:
    direction = command
    row_change, col_change = directions[direction]

    new_row = miner_row + row_change
    new_col = miner_col + col_change

    if 0 <= new_row < field_size and 0 <= new_col < field_size:
        miner_row = new_row
        miner_col = new_col
        if matrix[miner_row][miner_col] == 'e':
            print(f'Game over! ({miner_row}, {miner_col})')
            exit()

        if matrix[miner_row][miner_col] == 'c':
            coal_count -= 1
            matrix[miner_row][miner_col] = '*'

    if coal_count == 0:
        print(f'You collected all coal! ({miner_row}, {miner_col})')
        exit()

print(f'{coal_count} pieces of coal left. ({miner_row}, {miner_col})')
