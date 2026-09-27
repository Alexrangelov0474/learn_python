number_list = list(map(int, input().split(', ')))
idx_list = [idx for idx in range(len(number_list)) if number_list[idx] % 2 == 0]
print(idx_list)