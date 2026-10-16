n_rows, n_cols = [int(x) for x in input().split()]

matrix = []
biggest_sub_matrix = []

max_sum = float('-inf')

for row in range(n_rows):
    line = list(map(int, input().split()))
    matrix.append(line)

for start_row in range(n_rows - 2):
    for start_col in range(n_cols - 2):
        current_sum = 0

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                current_sum += matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_sub_matrix = []

            for r in range(start_row, start_row + 3):
                biggest_sub_matrix.append(matrix[r][start_col: start_col + 3])


print(f'Sum = {max_sum}')

for row in biggest_sub_matrix:
    print(*row)