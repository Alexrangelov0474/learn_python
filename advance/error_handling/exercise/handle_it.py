numbers = list(map(int,input().split(", ")))
result = 1

for i in range(len(numbers)):
    number = numbers[i]

    if number <= 3:
        result *= number
    elif 3 < number <= 6:
        result /= number
    elif number > 6:
        result += number

print(result)




# numbers = input().split(", ")
# result = 1

# for i in range(len(numbers)):
#     number = numbers[i]
#
#     if number <= 3:
#         result *= number
#     elif 3 < number <= 6:
#         result /= number
#     elif number > 6:
#         result += number
#
# print(final_result)