from collections import deque

n_rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n_rows)]
n_cols = len(matrix[0])

commands = input().split()
bombs = deque()

for command in commands:
    row, col = map(int, command.split(','))
    bombs.append((row, col))

for bomb_row, bomb_col  in bombs:
    if matrix[bomb_row][bomb_col] <= 0:
        continue

    bomb_strenght = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

    start_row = max(0, bomb_row - 1)
    end_row = min(n_rows, bomb_row + 2)
    start_col = max(0, bomb_col - 1)
    end_col = min(n_cols, bomb_col + 2)

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            cell = matrix[row][col]

            if cell > 0:
                matrix[row][col] -= bomb_strenght

alive_cells = 0
alive_cell_counter = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += cell
            alive_cell_counter += 1

print(f'Alive cells: {alive_cell_counter}')
print(f'Sum: {alive_cells}')

for row in matrix:
    print(*row)
