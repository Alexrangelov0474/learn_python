def employees_happiness_calculator(happiness: list, factor: int) -> str:
    multiply_happiness = [current_happiness * factor for current_happiness in happiness]
    average_happiness = sum(multiply_happiness) / len(multiply_happiness)
    happy_employees_counter = sum(number >= average_happiness for number in multiply_happiness)
    total_count = len(multiply_happiness)

    message = 'happy' if happy_employees_counter >= total_count / 2 else 'not happy'

    return f'Score: {happy_employees_counter}/{total_count  }. Employees are {message}!'

employees_happiness = list(map(int, input().split()))
happiness_factor = int(input())
result = employees_happiness_calculator(employees_happiness, happiness_factor)
print(result)