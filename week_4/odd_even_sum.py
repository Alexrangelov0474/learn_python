n = int(input())

odd_nums = 0
even_nums = 0

for idx in range(n):
    new_number = int(input())

    if idx % 2 == 0:
        odd_nums += new_number
    else:
        even_nums += new_number

if odd_nums == even_nums:
    print('Yes')
    print(f'Sum = {odd_nums}')
else:
    print('No')
    print(f'Diff = {abs(odd_nums - even_nums)}')