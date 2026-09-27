n = int(input())
flag = False
for num1 in range(1,10):
    for num2 in range(9,num1 - 1, -1):
        for num3 in range (10):
            for num4 in range(9, num3 - 1,- 1):
                sum_one = num1 + num2 + num3 + num4
                sum_two = num1 * num2 * num3 * num4

                if sum_one == sum_two and n % 10 == 5:
                    print(f'{num1}{num2}{num3}{num4}')
                    flag = True
                    break
                elif sum_one != 0 and sum_two // sum_one == 3 and n % 3 == 0:
                    print(f'{num4}{num3}{num2}{num1}')
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
if not flag:
    print('Nothing found')

