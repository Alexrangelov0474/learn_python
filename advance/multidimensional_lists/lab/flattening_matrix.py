n_rows = int(input())

matrix = []

for _ in range(n_rows):
    numbers = [int(n) for n in input().split(', ')]
    matrix.extend(numbers)

print(matrix)