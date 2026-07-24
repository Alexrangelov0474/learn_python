message = input()
while True:
    command = input().split('|')
    if command[0] == 'Reveal':
        break
    action = command[0]
    if action == 'Insert':
        index = int(command[1])
        text  = command[2]
        message = message[:index] + text + message[index:]
    elif action == 'Delete':
        start_index = int(command[1])
        end_index = int(command[2])
        message = message[:start_index] + message[end_index + 1:]
    elif action == 'Swap':
        first_string = command[1]
        second_string = command[2]
        temporary = '#temp#'
        message = message.replace(first_string, temporary)
        message = message.replace(second_string,first_string)
        message = message.replace(temporary,second_string)
    elif action == 'Upper':
        message = message.upper()
print(f'Secret message: {message}')