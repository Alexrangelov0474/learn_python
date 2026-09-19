n_rows = int(input())

matrix = []

for _ in range(n_rows):
    numbers = [int(n) for n in input().split(', ')]
    matrix.append(numbers)


primary_diagonal = []
secondary_diagonal = []


for index in range(n_rows):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][-index -1])

print(f'Primary diagonal: {", ".join(str(n) for n in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(n) for n in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')


