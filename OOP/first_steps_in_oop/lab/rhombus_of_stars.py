def print_rows(size:int, stars:int) -> None:
    print(' ' * (size - stars) + '* ' * stars)

def print_upper_part(size:int) -> None:
    for row in range(1, size):
        print_rows(size, row)

def print_lower_part(size:int) -> None:
    for row in range(size, 0, -1):
        print_rows(size, row)

def print_rhombus(size:int) -> None:
    print_upper_part(size)
    print_lower_part(size)

n = int(input())
print_rhombus(n)