n_rows = int(input())

matrix = []

for _ in range(n_rows):
    numbers = [int(n) for n in input().split()]
    matrix.append(numbers)

diagonal_sum = 0
for index in range(n_rows):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)