num = int(input())
total_num = 0

while True:
    next_num = int(input())
    total_num += next_num

    if total_num >= num:
        break
print(total_num)

