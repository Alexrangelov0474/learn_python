n_rows, n_cols = map(int, input().split())

matrix = [[int(num) for num in input().split()] for _ in range(n_rows)]

max_sum = float('-inf')

max_row = 0
max_col = 0

for row_index in range(n_rows -2):
    for col_index in range(n_cols -2):
        current_sum = 0

        for row in range(row_index, row_index + 3):
            for col in range(col_index, col_index + 3):
                current_sum += matrix[row][col]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_col  = col_index

print(f'Sum = {max_sum}')
sub_matrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in sub_matrix]

