def create_set(range_str: str)-> set:
    start, end = range_str.split(',')
    return set(range(int(start), int(end) + 1))

longest_intersection = set()

for _ in range(int(input())):
    line = input().split('-')

    first_set = create_set(line[0])
    second_set = create_set(line[1])

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}')