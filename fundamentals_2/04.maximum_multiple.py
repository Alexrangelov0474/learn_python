divisor = int(input())
boundary = int(input())
number = 0

for number in range(boundary, divisor, -1):
    if number % divisor == 0:
        break
print(number)