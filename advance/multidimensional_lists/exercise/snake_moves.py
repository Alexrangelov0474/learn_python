from collections import deque

n_rows, n_cols = map(int, input().split())

text = deque(input())
matrix = []

for row in range(n_rows):
    matrix.append([''] * n_cols)
    for col in range(n_cols):
        if row % 2 == 0:
            matrix[row][col] = text[0]
        else:
            matrix[row][-1 -col] = text[0]

        text.rotate(-1)

[print(*row, sep='') for row in matrix]
