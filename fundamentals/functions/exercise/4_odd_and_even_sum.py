def calculate_sum(number):
    odd_sum = 0
    even_sum = 0
    for num in str (number):
        num = int(num)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return odd_sum, even_sum

number = int(input())
odd_sum, even_sum = calculate_sum(number)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")