number_of_sym = int(input())
for first_sym in range(97, 97 + number_of_sym):
    for second_sym in range(97, 97 + number_of_sym):
        for third_sym in range(97, 97 + number_of_sym):
            print(f"{chr(first_sym)}{chr(second_sym)}{chr(third_sym)}")