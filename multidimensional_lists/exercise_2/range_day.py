matrix = []

n_rows = 5
player_row = 0
player_col = 0
targets_count = 0

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
       if current_row[col] == 'A':
           player_row = row
           player_col = col

       if  current_row[col] == 'x':
           targets_count += 1

def execution_of_commands(current_matrix:list, current_command:list, p_row: int, p_col: int,)-> tuple:
    action = current_command[0]
    target_hit = None

    if action == 'move':
        steps = int(current_command[2])
        dr, dc = DIRECTIONS[current_command[1]]
        new_row, new_col = p_row + dr * steps, p_col + dc * steps

        if 0 <= new_row < n_rows and 0 <= new_col < n_rows:
            if current_matrix[new_row][new_col] == '.':
                current_matrix[p_row][p_col] = '.'
                current_matrix[new_row][new_col] = 'A'

                p_row, p_col = new_row, new_col

    elif action == 'shoot':
        dr, dc = DIRECTIONS[current_command[1]]

        new_row, new_col = p_row + dr, p_col + dc

        while 0 <= new_row < n_rows and 0 <= new_col < n_rows:
            if current_matrix[new_row][new_col] == 'x':
                t = [new_row, new_col]
                current_matrix[new_row][new_col] = '.'
                break

            new_row += dr
            new_col += dc

    return p_row, p_col, target_hit

DIRECTIONS = {
    'left' : (0, -1),
    'right' : (0, 1),
    'up' : (-1, 0),
    'down' : (1, 0)
}

targets_hited = []
targets_left = targets_count

n_lines = int(input())
for line in range(n_lines):
    command = input().split()
    player_row, player_col, target_hit = execution_of_commands(matrix, command, player_row, player_col)

    if target_hit is not None:
        targets_hited.append(target_hit)
        targets_left -= 1

    if targets_left == 0:
        print(f'Training completed! All {len(targets_hited)} targets hit.')
        print(*targets_hited, sep='\n')
        exit()
else:
    print(f'Training not completed! {targets_left} targets left.')
    print(*targets_hited, sep='\n')

