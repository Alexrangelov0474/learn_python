n1 = int(input())
n2 = int(input())
magic_number = int(input())
counter = 0
flag = False

for num_1 in range(n1, n2 + 1):
    for num_2 in range(n1, n2 + 1):
        counter += 1
        if num_1 + num_2 == magic_number:
            print(f"Combination N:{counter} ({num_1} + {num_2} = {magic_number})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")
