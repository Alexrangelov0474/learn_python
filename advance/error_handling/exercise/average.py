numbers = list(map(int, input().split()))
total = 0

for i in range(len(numbers)):
    total += numbers[i]

average = total / len(numbers)

print(average)


# numbers = map(int, input().split())
# total = 0
#
# for i in range(len(numbers)):
#     total += numbers[i]
#
# average = total / len(numbers)
#
# print(average)