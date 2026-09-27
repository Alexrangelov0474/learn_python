def modify_sets(current_odd_set: set, current_even_set: set)-> set:
    if sum(current_odd_set) == sum(current_even_set):
        return current_odd_set.union(current_even_set)

    elif sum(current_odd_set) > sum(current_even_set):
        return current_odd_set.difference(current_even_set)

    else:
        return current_odd_set.symmetric_difference(current_even_set)

current_row = 1
odd_set = set()
even_set = set()

for _ in range(int(input())):
    ascii_sum = (sum(ord(x) for x in input()) // current_row)
    if ascii_sum % 2 != 0:
        odd_set.add(ascii_sum)
    elif ascii_sum % 2 == 0:
        even_set.add(ascii_sum)

    current_row += 1

current_values = modify_sets(odd_set, even_set)
print(*current_values, sep=', ')

