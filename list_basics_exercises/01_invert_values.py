numbers = input().split()
inverted_numbers = []
for number in numbers:
    inverted_number = -int(number)
    inverted_numbers.append(inverted_number)
print(inverted_numbers)