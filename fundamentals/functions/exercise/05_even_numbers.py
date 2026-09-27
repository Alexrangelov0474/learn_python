def even_numbers(current_numbers: int) -> bool:
    return current_numbers % 2 == 0

number_as_string = input().split()
numbers_as_digit = []
for number in number_as_string:
    numbers_as_digit.append(int(number))

result = list(filter(even_numbers, numbers_as_digit))
print(result)

