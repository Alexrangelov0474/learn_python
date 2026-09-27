from math import floor

def distance_calculation(x: float, y: float,) -> float:
    return x ** 2 + y ** 2

def line_length(x1:float, y1:float, x2:float, y2:float)-> float:
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

first_line = line_length(x_1,y_1,x_2,y_2)
second_line = line_length(x_3,y_3,x_4,y_4)


if first_line >= second_line:

    first_distance = distance_calculation(x_1, y_1)
    second_distance = distance_calculation(x_2, y_2)

    if first_distance <= second_distance:
        print(f"({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})")
    else:
        print(f"({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})")

else:

    first_distance = distance_calculation(x_3, y_3)
    second_distance = distance_calculation(x_4, y_4)

    if first_distance <= second_distance:
        print(f"({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})")
    else:
        print(f"({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})")