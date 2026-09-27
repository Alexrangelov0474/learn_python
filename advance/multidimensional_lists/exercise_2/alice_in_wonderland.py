def alice_path(current_matrix: list, r:int, c:int):
    current_matrix[r][c] = '*'

def print_matrix()-> None:
    for cur_row in matrix:
        print(*cur_row)

n_rows = int(input())

matrix = []
alice_row = 0
alice_col = 0

for row in range(n_rows):
    current_row = [int(x) if x.isdigit() else x for x in input().split()]
    matrix.append(current_row)

    for col in range(n_rows):
        if current_row[col] == 'A':
            alice_row = row
            alice_col = col
            alice_path(matrix, alice_row, alice_col)
            break

DIRECTIONS = {
    'left' : (0, -1),
    'right' : (0, 1),
    'up' : (-1, 0),
    'down' : (1, 0)
}

total_tea_collected = 0

while True:
    command = input()
    dr, dc = DIRECTIONS[command]

    new_row, new_col = alice_row + dr, alice_col + dc

    if not (0 <= new_row < n_rows and 0 <= new_col < n_rows):
        print("Alice didn't make it to the tea party.")
        print_matrix()
        exit()

    if matrix[new_row][new_col] == 'R':
        print("Alice didn't make it to the tea party.")
        alice_path(matrix, new_row, new_col)
        print_matrix()
        exit()

    if isinstance(matrix[new_row][new_col],  int):
        total_tea_collected += matrix[new_row][new_col]

    alice_row = new_row
    alice_col = new_col
    alice_path(matrix, alice_row, alice_col)

    if total_tea_collected >= 10:
        print('She did it! She went to the party.')
        print_matrix()
        exit()




