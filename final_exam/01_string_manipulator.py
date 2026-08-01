string = input()

while True:
    command = input().split()
    if command[0] == 'End':
        break
    action = command[0].lower()
        #potentual problem!
    if action == 'translate':
        char, replacement = command[1], command[2]
        string = string.replace(char, replacement)
        print(string)

    elif action == 'includes':
        substring = command[1]

        if substring in string:
            print(True)
        else:
            print(False)

    elif action == 'start':
        substring = command[1]
        if string.startswith(substring):
            print(True)
        else:
            print(False)

    elif action == 'lowercase':
        string = string.lower()
        print(string)

    elif action == 'findindex':
        char = command[1]
        print(string.rfind(char))

    elif action == 'remove':
        start_index, count = int(command[1]), int(command[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)
