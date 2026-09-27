number_of_lines = int(input())

counter = 0
balanced = True

for _ in range(number_of_lines):
    character = input()

    if character == '(':
        counter += 1

    elif character == ')':
        counter -= 1

    if counter < 0:
        balanced = False
        break

    if counter > 1:
        balanced = False
        break

if counter != 0:
    balanced = False

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')