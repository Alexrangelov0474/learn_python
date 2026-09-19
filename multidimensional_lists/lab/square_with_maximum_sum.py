n_rows, n_cols = map(int, input().split(', '))

matrix = []

for _ in range(n_rows):
    numbers = [int(n) for n in input().split(', ')]
    matrix.append(numbers)

max_sum = float('-inf')
sub_matrix = []

for row_index in range(n_rows -1):
    for col_index in range(n_cols -1):
        current_number = matrix[row_index][col_index]
        next_number = matrix[row_index][col_index + 1]
        below_number = matrix[row_index + 1][col_index]
        diagonal_number = matrix[row_index + 1][col_index + 1]
        sum_numbers = current_number + next_number + below_number + diagonal_number

        if sum_numbers > max_sum:
            max_sum = sum_numbers
            sub_matrix = [
                [current_number, next_number], [below_number, diagonal_number]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)