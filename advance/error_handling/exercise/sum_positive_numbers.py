numbers = list(map(int,input().split()))
total = 0

for i in range(len(numbers)):
    number = numbers[i]

    if number > 0:
        total += number

print(total)



# numbers = input().split()
# total = 0
#
# for i in range(numbers):
#     number = numbers[i]
#
#     if number > 0:
#         total += number
#
# print(sum)