import re
patter = r'([!*])([A-Z][a-z]{2,})\1:\[([A-Za-z]{8,})\]'
number_of_lines = int(input())
for line in range(number_of_lines):
    text = input()
    match = re.fullmatch(patter,text)
    if not match:
        print("The message is invalid")
    else:
        command = match.group(2)
        message = match.group(3)
        print(f"{command}:", end=" ")
        for char in message:
            print(ord(char), end=" ")
        print()