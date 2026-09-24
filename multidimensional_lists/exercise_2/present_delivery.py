presents = int(input())
n_rows = int(input())

matrix = []

santa_row = 0
santa_col = 0

naughty_kids = []
nice_kids = []
cookies = []

DIRECTIONS = {
    'left' : (0, -1),
    'right' : (0, 1),
    'up' : (-1, 0),
    'down' : (1, 0)
}

for row in range(n_rows):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(n_rows):
        if current_row[col] == 'S':
            santa_row = row
            santa_col = col
        elif current_row[col] == 'X':
            naughty_kids.append((row, col))

        elif current_row[col] == 'V':
            nice_kids.append((row,col))

        elif current_row[col] == 'C':
            cookies.append((row, col))


