def check_health_status(current_health:int) -> bool:
    return current_health > 0

n_rows = int(input())

matrix = []
hero_r, hero_c = 0, 0
health = 100
treasures = 0

game_status = 'playing'

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n_rows):
    line = list(input())
    if 'P' in line:
        hero_r, hero_c = row, line.index('P')
        line[hero_c] = '.'
    matrix.append(line)

while True:
    command = input()
    if command == '':
        break

    health -= 5
    if not check_health_status(health):
        game_status = 'dead'
        print('The hero died!')
        break

    dr, dc = DIRECTIONS[command]
    new_hero_r, new_hero_c = hero_r + dr, hero_c + dc
    if 0 <= new_hero_r < n_rows and 0 <= new_hero_c < n_rows:
        matrix[hero_r][hero_c] = '.'

        if matrix[new_hero_r][new_hero_c] == 'T':
            matrix[new_hero_r][new_hero_c] = '.'
            health -= 30
            if not check_health_status(health):
                matrix[hero_r][hero_c] = 'P'
                game_status = 'dead'
                print('The hero died!')
                break

            matrix[new_hero_r][new_hero_c] = 'P'

        elif matrix[new_hero_r][new_hero_c] == 'C':
            treasures += 1
            matrix[new_hero_r][new_hero_c] = 'P'

        elif matrix[new_hero_r][new_hero_c] == 'E':
            matrix[new_hero_r][new_hero_c] = 'P'
            game_status = 'escaped'
            print('The hero escaped!')
            break

        else:
            matrix[new_hero_r][new_hero_c] = 'P'

        hero_r, hero_c = new_hero_r, new_hero_c

    else:
        new_hero_r, new_hero_c = hero_r, hero_c

if game_status == 'playing':
    print('Exploration ended.')

print(f'{health} \n{treasures}')

for row in matrix:
    print(''.join(row))






