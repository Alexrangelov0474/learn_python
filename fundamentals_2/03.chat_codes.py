num_messages = int(input())

for messages in range(num_messages):
    current_number = int(input())
    current_message = ''
    if current_number == 88:
        current_message = 'Hello'
    elif current_number == 86:
        current_message = 'How are you?'
    elif current_number < 88:
        current_message = 'GREAT!'
    elif current_number > 88:
        current_message = 'Bye.'
    print(current_message)