matrix = [[int(x) for x in row.split()] for row in input().split('|')]

result = []
for row in matrix[::-1]:
    result.extend(row)

print(*result)