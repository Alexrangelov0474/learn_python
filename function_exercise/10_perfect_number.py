def perfect_number_checker(some_number: int) -> str:
    devisor_sum = 0
    for idx in range(1,some_number):
        if some_number % idx == 0:
            devisor_sum += idx

    if devisor_sum == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())

print(perfect_number_checker(number))
