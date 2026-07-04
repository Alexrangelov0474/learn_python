from math import pi

shape = input()
shape_area = 0.0

if shape == "square":
    square_side_length = float(input())
    shape_area = square_side_length * square_side_length
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    shape_area = side_a * side_b
elif shape == "circle":
    radius = float(input())
    shape_area = pi * radius * radius
elif shape == "triangle":
    length = float(input())
    height = float(input())
    shape_area = (length * height) / 2

print(f'{shape_area:.3f}')