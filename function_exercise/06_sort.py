def sorting_numbers(current_numbers: int) -> int:
    return sorted(current_numbers)

mixed_numbers = input().split()
sorted_numbers = []

for num in mixed_numbers:
    sorted_numbers.append(int(num))

result = sorting_numbers(sorted_numbers)
print(result)