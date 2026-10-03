import os

while True:
    line = input()
    if line == 'End':
        break

    action, filename, *args = line.split('-')

    if action == 'Create':
        open(filename, 'w').close()

    elif action == 'Add':
        with open(filename, 'a') as file:
            file.write(f'{args[0]}\n')

    elif action == 'Replace':
        try:
            with open(filename, 'r+') as file:
                old_string, new_string = args
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(old_string, new_string))
        except FileNotFoundError:
            print('An error occurred')

    elif action == 'Delete':
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('An error occurred')


