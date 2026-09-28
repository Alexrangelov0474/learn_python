numbers = list(map(int, input().split(", ")))
minimum = float('inf')

for i in range(len(numbers)):
    number = numbers[i]

    if number < minimum:
        minimum = number

print(minimum)

# numbers = list(map(int, input().split(", ")))
# minimum = 0
#
# for i in range(len(numbers)):
#     number = numbers[i + 1]
#
#     if number < minimum:
#         minimum = number
#
# print(minimum_value)