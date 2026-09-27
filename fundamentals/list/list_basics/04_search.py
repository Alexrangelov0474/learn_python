number_of_lines = int(input())
magic_word = input()

string_list = []

for _ in range(number_of_lines):
    current_string = input()
    string_list.append(current_string)

cleared_list = []

for _two in string_list:
    if magic_word in _two:
        cleared_list.append(_two)

print(f'{string_list}\n'
      f'{cleared_list}')