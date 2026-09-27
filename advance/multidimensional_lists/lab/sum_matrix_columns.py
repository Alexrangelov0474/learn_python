n_rows, n_cols = map(int, input().split(', '))

matrix = []

for _ in range(n_rows):
    numbers = [int(n) for n in input().split()]
    matrix.append(numbers)

for col_index in range(n_cols):
    col_sum = 0
    for row_index in range(n_rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)