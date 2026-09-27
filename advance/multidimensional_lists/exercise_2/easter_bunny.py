n = int(input())

matrix = []
bunny_r = bunny_c = 0

for r in range(n):
    row = input().split()
    if 'B' in row:
        bunny_r, bunny_c = r, row.index('B')
    matrix.append(row)

DIRECTIONS = {
    'left' : (0, -1),
    'right' : (0, 1),
    'up' : (-1, 0),
    'down' : (1, 0)
}

max_eggs = float('-inf')
best_direction = ''
best_path = []

for direction, (dr, dc) in DIRECTIONS.items():
    eggs = 0
    current_path = []

    new_row, new_col = bunny_r + dr, bunny_c + dc

    while 0 <= new_row < n and 0 <= new_col < len(matrix[0]):
            if matrix[new_row][new_col] == 'X':
                break

            eggs += int(matrix[new_row][new_col])
            current_path.append([new_row, new_col])

            new_row += dr
            new_col += dc

    if eggs > max_eggs and current_path:
        max_eggs = eggs
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)
