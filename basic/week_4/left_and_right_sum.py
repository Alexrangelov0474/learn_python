n = int(input())
side_one = 0
side_two = 0

for idx in range(n * 2):
    new_number = int(input())

    if idx < n:
        side_one += new_number
    else:
        side_two += new_number

if side_one == side_two:
    print(f'Yes, sum = {side_one}')
else:
    print(f'No, diff = {abs(side_one - side_two)}')
