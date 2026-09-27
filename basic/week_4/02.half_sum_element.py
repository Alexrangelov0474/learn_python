from sys import maxsize

n = int(input())

total_sum = 0
max_num = -maxsize

for _ in range(n):
    num = int(input())
    total_sum += num

    if num > max_num:
        max_num = num

if max_num == (total_sum - max_num):
    print(f'Yes\nSum = {max_num}')
else:
    diff = abs(max_num - (total_sum - max_num))
    print(f'No\nDiff = {diff} ')