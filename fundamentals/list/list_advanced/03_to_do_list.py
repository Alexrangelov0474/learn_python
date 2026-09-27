notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break

    priority, note = command.split('-')
    priority = int(priority) - 1

    notes.pop(priority)
    notes.insert(priority, note)

result = [idx for idx in notes if idx != 0]

print(result)