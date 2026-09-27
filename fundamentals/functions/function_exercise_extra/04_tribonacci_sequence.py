def tribonacci_calculator(current_number:int) -> None:
    lst_of_numbers = [1,1,2]
    for idx in range(current_number - 3):
        next_number = lst_of_numbers[-1] + lst_of_numbers[-2] + lst_of_numbers[-3]
        lst_of_numbers.append(next_number)

    print(' '.join(str(num) for num in lst_of_numbers[:current_number]))

number = int(input())
tribonacci_calculator(number)