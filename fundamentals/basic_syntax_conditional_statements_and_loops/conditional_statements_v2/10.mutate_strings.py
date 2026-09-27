first_string = input()
second_string = input()
for index in range(len(first_string)):
    left_side = second_string[:index + 1]
    right_side = first_string[index + 1:]
    new_string = left_side + right_side
    if first_string[index] != second_string[index]:
        print(new_string)
