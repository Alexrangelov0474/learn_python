string = input()

parentheses_stack = []

for i in range(len(string)):
    if string[i] == '(':
        parentheses_stack.append(i)
    elif string[i] == ')':
        start_idx = parentheses_stack.pop()
        end_idx = i + 1
        print(string[start_idx:end_idx])
