string = input()

values_map = {}

for char in string:
    if char not in values_map.keys():
        values_map[char] = 1
    else:
        values_map[char] += 1

for key, value in sorted(values_map.items()):
    print(f'{key}: {value} time/s')