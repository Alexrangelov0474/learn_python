numbers = list(map(int, input().split()))
total = 0
product = 1

for i in range(len(numbers)):
    number = numbers[i]

    if number > 0:
        total += number
    elif number < 0:
        product *= number

print(total)
print(product)


# numbers = list(map(int, input().split()))
# total = 0
# product = 1
#
# for i in range(numbers):
#     number = numbers[i]
#
#     if number > 0:
#         total += number
#     elif number < 0:
#         product *= number
#
# print(sum)
# print(product)