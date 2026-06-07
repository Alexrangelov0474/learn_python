def int_action(second_action: str) -> int:
    result = int(second_action) * 2
    return result

def float_action(second_action: str) -> str:
    result = float(second_action) * 1.5
    return f"{result:.2f}"

def string_action(second_action: str) -> str:
    return f'${second_action}$'

action = input()
action_by_command = input()

final_result = '' or 0

if action == 'int':
    final_result = int_action(action_by_command)
elif action == 'real':
    final_result = float_action(action_by_command)
elif action == 'string':
    final_result = string_action(action_by_command)

print(final_result)

