def combine_functions(main_command: str, action: str) -> int or str:

    if main_command == 'int':
        return int_action(action)
    elif main_command == 'real':
        return float_action(action)
    elif main_command == 'string':
        return string_action(action)
    return 'Invalid'

def int_action(action: str) -> int:
    result = int(action) * 2
    return result

def float_action(action: str) -> str:
    result = float(action) * 1.5
    return f"{result:.2f}"

def string_action(action: str) -> str:
    result = f'${action}$'
    return result

command = input()
action_by_command = input()

print(combine_functions(command, action_by_command))