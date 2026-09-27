def positive_numbers(current_numbers: list) -> str:
    filtered_numbers = [number for number in current_numbers if int(number) >= 0]
    return ', '.join(filtered_numbers)

def negative_numbers(current_numbers: list) -> str:
    filtered_numbers = [number for number in current_numbers if int(number) < 0]
    return ', '.join(filtered_numbers)

def even_numbers(current_numbers: list) -> str:
    filtered_numbers = [number for number in current_numbers if int(number) % 2 == 0]
    return ', '.join(filtered_numbers)

def odd_numbers(current_numbers: list) -> str:
    filtered_numbers = [number for number in current_numbers if int(number) % 2 != 0]
    return ', '.join(filtered_numbers)

numbers = input().split(', ')

print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')
