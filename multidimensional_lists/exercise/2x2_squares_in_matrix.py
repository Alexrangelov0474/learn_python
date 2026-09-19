n_rows, n_cols = map(int, input().split())

matrix = []

for _ in range(n_rows):
    numbers = input().split()
    matrix.append(numbers)

squares_counter = 0

for row_index in range(n_rows -1):
    for col_index in range(n_cols -1):
        # current_number = matrix[row_index][col_index]
        # next_number = matrix[row_index][col_index + 1]
        # below_number = matrix[row_index + 1][col_index]
        # diagonal_number = matrix[row_index + 1][col_index + 1]
        #
        # if current_number == next_number \
        #         and next_number == below_number \
        #         and below_number == diagonal_number:
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
            squares_counter += 1

print(squares_counter)