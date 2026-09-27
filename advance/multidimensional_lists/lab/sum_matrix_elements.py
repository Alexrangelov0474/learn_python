n_rows, n_cols = map(int, input().split(', '))

matrix = []
matrix_sum = 0

for _ in range(n_rows):
    numbers = [int(x) for x in input().split(', ')]
    matrix_sum += sum(numbers)
    matrix.append(numbers)

print(matrix_sum)
print(matrix)