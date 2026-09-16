string_expression = input().split()
numbers_stack = []

def calculator(current_values: list,operator: str) -> int:
    current_result = values[0]

    for current_values in values[1:]:
        if operator == '*':
            current_result *= current_values
        elif operator == '+':
            current_result += current_values
        elif operator == '-':
            current_result -= current_values
        elif operator == '/':
            current_result //= current_values

    return current_result

for element in string_expression:
    if element in ['*', '+', '-', '/']:
        values = numbers_stack.copy()
        numbers_stack.clear()

        numbers_stack.append(calculator(values, element))

    else:
        numbers_stack.append(int(element))

print(*numbers_stack)



