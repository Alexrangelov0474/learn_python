player_one_name = input('Player one name: ')
player_two_name = input('Player two name: ')

player_one_sign = input(f'{player_one_name} would you like to play with "X" or "O"?').upper()

player_two_sign = 'O' if player_one_sign == 'X' else 'X'

print('This is the numeration of the board:')
print('| 1 | 2 | 3 |')
print('| 4 | 5 | 6 |')
print('| 7 | 8 | 9 |')
print(f'{player_one_name} starts first!')

turn = 1
while True:
    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    try:
        position = int(input(f'{current_player} choose a free position [1-9]:'))
    except ValueError:
        print('Please enter a valid number!')
        continue

    if not (1<= position <= 9):
        print('Please enter a valid number, between 1 and 9.')
        continue

    turn += 1
