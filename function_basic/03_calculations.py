
def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide  (a, b):
    return a / b


def calculation ():
    operator = input()
    a = int(input())
    b = int(input())
    result = 0
    if operator == 'add':
        result = add(a,b)
    elif operator == 'subtract':
        result = subtract(a,b)
    elif operator == 'multiply':
        result = multiply(a,b)
    elif operator == 'divide':
        result = divide(a,b)

    print(result)

calculation()