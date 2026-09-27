def factorial_calculator(number:int) -> int:
    result = 1
    for num in range(1,number + 1):
        result *= num

    return result

first_number = int(input())
second_number = int(input())

first_factorial = factorial_calculator(first_number)
second_factorial = factorial_calculator(second_number)

final_result = first_factorial / second_factorial
print(f'{final_result:.2f}')
