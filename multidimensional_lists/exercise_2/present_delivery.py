presents = int(input())
n_rows = int(input())

matrix = []

santa_row = 0
santa_col = 0

naughty_kids_count = 0
nice_kids_count = 0

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
            naughty_kids_count += 1

        elif current_row[col] == 'V':
            nice_kids_count += 1

def execution_of_commands(current_matrix:list,current_command: str ,s_row: int ,s_col:int, current_presents: int, current_nice_kids: int):
    dr, dc = DIRECTIONS[current_command]
    new_row, new_col = s_row + dr, s_col + dc

    if 0 <= new_row < n_rows and 0 <= new_col < n_rows:

        if current_matrix[new_row][new_col] == 'V':
            current_presents -= 1
            current_nice_kids -= 1

        elif current_matrix[new_row][new_col] == 'X':
            pass

        elif current_matrix[new_row][new_col] == 'C':

            for dr, dc in DIRECTIONS.values():
                next_row, next_col = new_row * dr, new_col * dc

                if current_matrix[next_row][next_col] == 'V':
                    current_presents -= 1
                    current_nice_kids -= 1

                elif current_matrix[next_row][next_col] == 'X':
                    current_presents -= 1

                current_matrix[next_row][next_col] = '-'


        current_matrix[s_row][s_col] = '-'
        current_matrix[new_row][new_col] = 'S'


        s_row, s_col = new_row, new_col
    return s_row, s_col, current_presents



while True:
    command = input()
    if command == 'Christmas morning':
        break
    if presents <= 0:
        break



