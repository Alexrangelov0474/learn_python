numbers = list(map(int, input().split(", ")))
result = 1

for i in range(len(numbers)):
    number = numbers[i]

    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)

# numbers = input().split(", ")
# result = 1
#
# for i in range(numbers):
#     number = numbers[i + 1]
#
#     if number < 5:
#         result *= number
#     elif 5 <= number <= 10:
#         result /= number
#
# print(total)