from math import floor

from advance.modules.mathematical_operations.mathematical_operations_core import calculator

expression = input().split()

num1, num2, sign = float(expression[0]), float(expression[2]), expression[1]

print(f'{calculator(num1, num2, sign):.2f}')
