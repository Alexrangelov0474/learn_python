n_rows = int(input())

matrix = [[int(n) for n in input().split()] for _ in range(n_rows)]

primary_diagonal = [matrix[index][index] for index in range(n_rows)]
secondary_diagonal = [matrix[index][-1 -index] for index in range(n_rows)]

difference = sum(primary_diagonal) - sum(secondary_diagonal)

print(abs(difference))