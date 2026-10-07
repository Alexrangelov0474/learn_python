class InvalidColumnError(Exception):
    pass

def valid_column_choice(cur_col: int, max_idx: int):
    if not (0 <= cur_col < max_idx):
        raise InvalidColumnError


def create_matrix(cur_row: int, cur_col: int) -> list:
    return [[0 for _ in range(cur_col)] for _ in range(cur_row)]

def print_matrix(cur_matrix:list) -> None:
    for line in cur_matrix:
        print(line)
ROWS = 6
COLS = 7

matrix = create_matrix(ROWS, COLS)

print_matrix(matrix)

player_num = 1

while True:
    try:
        column_num = int(input(f'Player {player_num}, please choose a column:\n')) - 1
        valid_column_choice(column_num, COLS)

        player_num = 2 if player_num == 1 else 1
    except ValueError:
        print('Please enter an digit and valid number!')

    except InvalidColumnError:
        print(f'Please select a number between 1 and {COLS}')

