encrypted_message = input()
while True:
    command = input().split('|')
    if command[0] == 'Decode':
        break

    action = command[0]

    if action == 'Move':
        number_of_letters = int(command[1])
        moving_part = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + moving_part

    elif action == 'Insert':
        index, value = int(command[1]), command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == 'ChangeAll':
        substring, replacement = command[1], command[2]
        encrypted_message = encrypted_message.replace(substring,replacement)

print(f'The decrypted message is: {encrypted_message}')