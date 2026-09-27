list_of_numbers = input().split()

absolute_numbers = []

for num in list_of_numbers:
    absolute_numbers.append(abs(float(num)))
print(absolute_numbers)