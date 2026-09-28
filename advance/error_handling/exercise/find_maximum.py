numbers = list(map(int,input().split(", ")))
largest = 0

for i in range(len(numbers)):
    current = numbers[i]

    if current > largest:
        largest = current

print(largest)



# numbers = input().split(", ")
# largest = 0
#
# for i in range(numbers):
#     current = numbers[i + 1]
#
#     if current > largest:
#         largest = current
#
# print(maximum)