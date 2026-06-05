def min_number(number: list) -> int:
    return min(number)

def max_number(number: list) -> int:
    return max(number)

def sum_number(number: list) -> int:
    return sum(number)

numbers_as_string = input().split()
numbers_as_digit = []
for num in numbers_as_string:
    numbers_as_digit.append(int(num))

biggest_number = max_number(numbers_as_digit)
smallest_number = min_number(numbers_as_digit)
total_sum = sum_number(numbers_as_digit)

print(f"The minimum number is {smallest_number}")
print(f"The maximum number is {biggest_number}")
print(f"The sum number is: {total_sum}")