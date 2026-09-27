n_rows, n_cols = map(int, input().split())

matrix = [input().split() for _ in range(n_rows)]

def validating_positon(r1: int,c1: int,r2: int,c2: int,rows: int,cols: int) -> bool:
    return 0 <= r1 < rows and 0 <= r2 < rows and 0 <= c1 < cols and 0 <= c2 < cols


while True:
    line = input()
    if line == 'END':
        break

    command = line.split()

    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = map(int, command[1:])
    if validating_positon(row1, col1, row2, col2, n_rows, n_cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')

