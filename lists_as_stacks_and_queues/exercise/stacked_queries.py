stack = []

number_of_lines = int(input())

queries = {
    '1': lambda x: stack.append(int(x)),
    '2': lambda: stack.pop() if stack else None,
    '3': lambda: print(max(stack)) if stack else None,
    '4': lambda: print(min(stack)) if stack else None,
}

for _ in range(number_of_lines):
    command = input().split()
    queries[command[0]](*command[1:])

print(*reversed(stack), sep=', ')