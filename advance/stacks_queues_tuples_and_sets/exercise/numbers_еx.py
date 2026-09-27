
def set_manipulation(current_action: str, second_action: str, current_numbers: list, set_one: set, set_two: set):
    if current_action == 'Add' and second_action == 'First':
        for num in current_numbers:
            set_one.add(num)

    elif current_action == 'Add' and second_action == 'Second':
        for num in current_numbers:
            set_two.add(num)

    elif current_action == 'Remove' and second_action == 'First':
        for num in current_numbers:
            if num in set_one:
                set_one.remove(num)
    elif current_action == 'Remove' and second_action == 'Second':
        for num in current_numbers:
            if num in set_two:
                set_two.remove(num)

def check_subset(set_one: set, set_two: set) -> bool:
    return set_one.issubset(set_two) or set_two.issubset(set_one)

first_set = set(map(int,input().split()))
second_set = set(map(int,input().split()))

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    second_command = command[1]
    numbers = list(map(int, command[2:]))

    set_manipulation(action, second_command, numbers, first_set, second_set)

    if action == 'Check' and second_command == 'Subset':
        print(check_subset(first_set, second_set))



print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')