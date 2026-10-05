player_one_name = input('Player one name: ')
player_two_name = input('Player two name: ')

while True:
    player_one_sign = input(f'{player_one_name} would you like to play with "X" or "O"? ').upper()
    if player_one_sign in ('X', 'O'):
        player_two_sign = 'O' if player_one_sign == 'X' else 'X'
        break

    print('Please choose either X or O !')

print('This is the numeration of the board:')
print('| 1 | 2 | 3 |')
print('| 4 | 5 | 6 |')
print('| 7 | 8 | 9 |')
print(f'{player_one_name} starts first!')

turn = 1
board = [[' ', ' ', ' '] for _ in range(3)]

def print_board(the_board: list) -> None:
    for current_row in the_board:
        print(f'| {" | ".join(current_row)} |')

def check_row_winner(the_board: list, cur_sign: str) -> bool:
    for cur_row in the_board:
        if cur_row.count(cur_sign) == 3:
            return True
    return False

def check_col_winner(the_board: list, cur_sign: str) -> bool:
    for cur_col in range(len(the_board)):
        column = [the_board[cur_row][cur_col] for cur_row in range(len(the_board))]

        if all(el == cur_sign for el in column):
            return True

    return False

    # for cur_col in range(len(the_board)):
    #     count = 0
    #     for cur_row in range(len(the_board)):
    #         if the_board[cur_row][cur_col] == cur_sign:
    #             count += 1
    #
    #     if count == 3:
    #         return True
    # return False

def check_diagonal_winner(the_board:list, cur_sign: str) -> bool:
    primary_diagonal = [the_board[index][index] for index in range(len(the_board))]
    secondary_diagonal = [the_board[index][len(the_board) - index -1] for index in range(len(the_board))]

    if all(el == cur_sign for el in primary_diagonal) or all(el == cur_sign for el in secondary_diagonal):
        return True
    return False

    #     # if the_board[index][index] == cur_sign:
    #     #     primary_counter += 1
    #     if the_board[index][3 - index - 1] == cur_sign:
    #         secondary_counter += 1
    #
    #     if primary_counter == 3 or secondary_counter == 3:
    #         return True
    # return False

def check_for_winner(the_board: list, cur_sign) -> bool:
    return (check_row_winner(the_board, cur_sign)
            or check_col_winner(the_board, cur_sign)
            or check_diagonal_winner(the_board, cur_sign))

    # row_winner = check_row_winner(the_board, cur_sign)
    # col_winner = check_col_winner(the_board, cur_sign)
    # diagonal_winner = check_diagonal_winner(the_board, cur_sign)
    # return row_winner or col_winner or diagonal_winner

while turn <= 9:

    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    try:
        position = int(input(f'{current_player} choose a free position [1-9]: '))
    except ValueError:
        print('Please enter a valid number!')
        continue

    if not (1<= position <= 9):
        print('Please enter a valid number, between 1 and 9.')
        continue

    row = (position - 1) // 3
    col = (position - 1) % 3

    if board[row][col] != ' ':
        print('This position is already occupied.')
        continue

    board[row][col] = current_sign
    print_board(board)

    if turn >= 5 and check_for_winner(board, current_sign):
        print(f'Congrats! {current_player} wins!')
        exit()

    turn += 1
print('Thanks for playing, no winner today!')