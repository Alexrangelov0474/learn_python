n_rows = int(input())

matrix = []
knights = []

for r in range(n_rows):
    row = list(input())
    for c in range(n_rows):
        if row[c] == 'K':
            knights.append([r, c])
    matrix.append(row)

KNIGHT_MOVES = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))

removed_knights = 0

while True:
    max_hits = 0
    knight_with_max_hits = None
    for current_row, current_col in knights:
        hits = 0
        for d_row, d_col in KNIGHT_MOVES:
            new_row, new_col = current_row + d_row, current_col + d_col
            if 0 <= new_row < n_rows and 0 <= new_col < n_rows and matrix[new_row][new_col] == 'K':
                hits += 1

        if hits > max_hits:
            max_hits = hits
            knight_with_max_hits = [current_row, current_col]

    if max_hits == 0:
        break

    knights.remove(knight_with_max_hits)
    matrix[knight_with_max_hits[0]][knight_with_max_hits[1]] = '0'
    removed_knights += 1

print(removed_knights)