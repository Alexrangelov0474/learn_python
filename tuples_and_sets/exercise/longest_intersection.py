longest_intersection = set()

for _ in range(int(input())):
    first_set = set()
    second_set = set()
    line = input().split('-')
    first_start, first_end = line[0].split(',')
    second_start, second_end = line[1].split(',')

    for num in range(int(first_start), int(first_end) + 1):
        first_set.add(num)


    for num in range(int(second_start), int(second_end) + 1):
        second_set.add(num)


    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}')