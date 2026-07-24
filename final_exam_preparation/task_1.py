message = input()
while True:
    command = input().split('|')
    if command[0] == 'Finish':
        break
    action = command[0]
    if action == 'Append':
        text_to_be_added = command[1]
        message += text_to_be_added
    elif action == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        message = message[:start_index] + message[start_index + count:]
    elif action == 'Replace':
        old_string = command[1]
        new_string = command[2]
        message = message.replace(old_string,new_string)
    elif action == 'Reverse':
        message = message[::-1]

print(f'Final message: {message}')