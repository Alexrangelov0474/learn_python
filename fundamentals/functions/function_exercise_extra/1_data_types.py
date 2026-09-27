def action_by_command(command, next_action):
    if command == 'int':
        result = int(next_action) * 2
        return result
    elif command == 'real':
        result = float(next_action) * 1.5
        return f'{result:.2f}'
    elif command == 'string':
        return f'${next_action}$'

action = input()
second_action = input()

final_result = action_by_command(action, second_action)
print(final_result)