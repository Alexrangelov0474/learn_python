elements = input().split()
number_of_moves = 0
player_won = False
turn = input()
while turn != 'end':
    number_of_moves += 1
    turn_as_list = turn.split()
    first_index = int(turn_as_list[0])
    second_index = int(turn_as_list[1])

    if first_index == second_index \
            or first_index not in range(len(elements)) \
            or second_index not in range(len(elements)):
        middle_of_the_elements = len(elements) // 2
        left_side = elements[:middle_of_the_elements]
        right_side = elements[middle_of_the_elements:]
        elements = left_side + \
                    [f'-{number_of_moves}a',
                     f'-{number_of_moves}a']\
                    + right_side
        print('Invalid input! Adding additional elements to the board')

    else:
        if elements[first_index] == elements[second_index]:
            matching_elements = elements[first_index]

            while matching_elements in elements:
                elements.remove(matching_elements)

            print(f'Congrats! You have found matching elements - {matching_elements}!')
        else:
            print('Try again!')

    if not elements:
        player_won = True
        break
    turn = input()

if player_won:
    print(f'You have won in {number_of_moves} turns!')
else:
    print('Sorry you lose :(')
    print(' '.join(elements))


