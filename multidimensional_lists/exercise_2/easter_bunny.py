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

