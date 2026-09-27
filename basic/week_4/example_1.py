from sys import maxsize

n = int(input())
max_number = -maxsize
sum_num = 0

for _ in range(n):
    num = int(input())
    sum_num += num

    if num > max_number:
        max_number = num

if  max_number == (sum_num - max_number):
    print(f'Yes\nSum = {max_number}')
else:
    diff = abs(max_number - (sum_num - max_number))
    print(f'No\nDiff = {diff}')