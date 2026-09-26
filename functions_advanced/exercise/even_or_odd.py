def even_odd(*args) -> list:
    command = args[-1]
    numbers = args[:-1]
    if command == 'even':
        filtered_args = list(filter(lambda x: x % 2 == 0, numbers))
    else:
        filtered_args = list(filter(lambda x: x % 2 != 0, numbers))

    return filtered_args

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))