numbers = list(map(int,input().split()))
total = 0

for i in range(len(numbers)):
    number = numbers[i]
    total += number

average = total / len(numbers)

print(average)



# numbers = input().split()
# total = 0
#
# for i in range(numbers):
#     number = numbers[i + 1]
#     total += number
#
# average = total / count
#
# print(average)