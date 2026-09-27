from sys import maxsize
min_number = maxsize

while True:
    new_input = input()
    if new_input == 'Stop':
        break
    num = int(new_input)

    if num < min_number:
        min_number = num

print(min_number)



