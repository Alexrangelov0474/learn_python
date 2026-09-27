first_line = input().split(', ')
second_line = input().split(', ')
substrings = []
for first_string in first_line:
    for second_string in second_line:
        if first_string in second_string:
            substrings.append(first_string)
            break

print(substrings)
