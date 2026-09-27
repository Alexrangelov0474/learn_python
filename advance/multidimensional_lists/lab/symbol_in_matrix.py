n_rows = int(input())

matrix = []

for _  in range(n_rows):
    numbers = list(input())
    matrix.append(numbers)

searched_symbol = input()
position = None

for row_index in range(n_rows):
    for col_index in range(n_rows):
        if matrix[row_index][col_index] == searched_symbol:
            position = (row_index, col_index)
            print(position)
            exit()

print(f'{searched_symbol} does not occur in the matrix')
