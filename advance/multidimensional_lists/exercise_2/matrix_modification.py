n_rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n_rows)]

def modify_matrix(current_action:str, current_row:int, current_col:int, current_value:int):
    if current_action == 'Add':
        matrix[current_row][current_col] += current_value

    elif current_action == 'Subtract':
        matrix[current_row][current_col] -= current_value

while True:
    commands = input().split()
    action = commands[0]
    if action == 'END':
        break

    row, col, value = map(int, commands[1:])

    if 0 <= row < n_rows and 0 <= col < n_rows:
        modify_matrix(action, row, col, value)
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row)