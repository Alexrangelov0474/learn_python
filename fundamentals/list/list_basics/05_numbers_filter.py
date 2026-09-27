number_of_lines = int(input())

numbers_list = []

for _ in range(number_of_lines):
    number = int(input())
    numbers_list.append(number)

command = input()

clear_list = []

if command == 'even':
    for num in numbers_list:
        if num % 2 == 0:
            clear_list.append(num)
elif command == 'odd':
    for num in numbers_list:
        if num % 2 != 0:
            clear_list.append(num)
elif command == 'negative':
    for num in numbers_list:
        if num < 0:
            clear_list.append(num)
elif command == 'positive':
    for num in numbers_list:
        if num >= 0:
            clear_list.append(num)

print(clear_list)