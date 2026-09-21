from collections import deque

n_rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n_rows)]
n_cols = len(matrix[0])

commands = input().split()
bombs = deque()
for command in commands:
    row, col = map(int, command.split(','))
    bombs.append((row, col))

alive_cells = matrix.copy()

for bomb_row, bomb_col  in bombs:
    bomb = matrix[bomb_row][bomb_col]
    bomb_strenght = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0
    for row in range(n_rows):
        for col in range(n_cols):

