def multiplication_sign(number_1: int,number_2: int,number_3: int) -> str:
    if number_1 == 0 or number_2 == 0 or number_3 == 0:
        return 'zero'

    counter = 0
    if number_1 < 0:
        counter += 1

    if number_2 < 0:
        counter += 1

    if number_3 < 0:
        counter += 1

    if counter % 2 == 0:
        return 'positive'
    return 'negative'

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_sign(first_number,second_number,third_number))