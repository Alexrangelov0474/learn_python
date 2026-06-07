from math import floor


def distance_calculation(x: float, y: float) -> float:
    return x ** 2 + y ** 2


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

first_distance = distance_calculation(x_1, y_1)
second_distance = distance_calculation(x_2, y_2)

if first_distance <= second_distance:
    print(f"({floor(x_1)}, {floor(y_1)})")
else:
    print(f"({floor(x_2)}, {floor(y_2)})")
