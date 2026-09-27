from sys import maxsize
max_number = -maxsize

while True:
    new_input = input()
    if new_input == 'Stop':
        break

    num = int(new_input)

    if num > max_number:
        max_number = num

print(max_number)