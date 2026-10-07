class InvalidColumnError(Exception):
    pass
class ColumnFullError(Exception):
    pass

def is_player_num(cur_matrix: list, r: int, c: int, cur_player_num: int):
    if r < 0 or c < 0 or r >= len(cur_matrix) or c >= len(cur_matrix[0]):
        return False
    return cur_matrix[r][c] == cur_player_num

def is_vertical_win(cur_matrix: list, r: int, c: int, cur_player_num: int, slots: int):
    return all(is_player_num(cur_matrix, r + index, c, cur_player_num) for index in range(slots))

def is_horizontal_win(cur_matrix: list, r: int, c: int, cur_player_num: int, slots: int):
    filled = 1

    for index in range(1, slots):
        if is_player_num(cur_matrix, r, c + index,  cur_player_num):
            filled += 1
        else:
            break

    for index in range(1, slots):
        if is_player_num(cur_matrix, r, c - index, cur_player_num):
            filled += 1
        else:
            break

    return filled >= slots

def is_right_diagonal_win(cur_matrix: list, r: int, c: int, cur_player_num: int, slots: int):
    filled = 1

    for index in range(1, slots):
        if is_player_num(cur_matrix, r - index, c + index, cur_player_num):
            filled += 1
        else:
            break

    for index in range(1, slots):
        if is_player_num(cur_matrix, r + index, c - index, cur_player_num):
            filled += 1
        else:
            break


def is_left_diagonal_win(cur_matrix: list, r: int, c: int, cur_player_num: int, slots: int):
    filled = 1

    for index in range(1, slots):
        if is_player_num(cur_matrix, r - index, c - index, cur_player_num):
            filled += 1
        else:
            break

    for index in range(1, slots):
        if is_player_num(cur_matrix, r + index, c + index, cur_player_num):
            filled += 1
        else:
            break

def is_winner(cur_matrix: list, r: int, c: int, cur_player_num: int, slots: int):
    return (is_vertical_win(cur_matrix, r, c, cur_player_num, slots)
            or is_horizontal_win(cur_matrix, r, c, cur_player_num, slots)
            or is_left_diagonal_win(cur_matrix, r, c, cur_player_num, slots)
            or is_right_diagonal_win(cur_matrix, r, c, cur_player_num, slots))

def place_player_choice(cur_matrix: list, c: int, cur_player_num: int):
    for r in range(len(cur_matrix)-1, -1, -1):
        if cur_matrix[r][c] == 0:
            cur_matrix[r][c] = cur_player_num
            return r, c
    raise ColumnFullError


def valid_column_choice(c: int, max_idx: int):
    if not (0 <= c < max_idx):
        raise InvalidColumnError


def create_matrix(r: int, c: int) -> list:
    return [[0 for _ in range(c)] for _ in range(r)]

def print_matrix(cur_matrix:list) -> None:
    for line in cur_matrix:
        print(line)

ROWS = 6
COLS = 7
SLOTS = 4

matrix = create_matrix(ROWS, COLS)

print_matrix(matrix)

player_num = 1

while True:
    try:
        column_num = int(input(f'Player {player_num}, please choose a column:\n')) - 1
        valid_column_choice(column_num, COLS)
        row, col = place_player_choice(matrix, column_num, player_num)
        print_matrix(matrix)

        if is_winner(matrix, row, col, player_num, SLOTS):
            print(f'The winner is player {player_num}')
            break

        player_num = 2 if player_num == 1 else 1

    except ValueError:
        print('Please enter an digit and valid number!')

    except InvalidColumnError:
        print(f'Please select a number between 1 and {COLS}')

    except ColumnFullError:
        print('This column is full! Please select another')
