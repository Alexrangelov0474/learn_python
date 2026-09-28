numbers = list(map(int, input().split()))
even_numbers = []

for i in range(len(numbers)):
    number = numbers[i]

    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# numbers = list(map(int, input().split()))
# even_numbers = []
#
# for i in range(len(numbers) + 1):
#     number = numbers[i]
#
#     if number % 2 = 0:
#         even_numbers.append(number)
#
# print(evens)