mapper = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a / b,
    '^': lambda a,b: a ** b,
}

def calculator(num1:float, num2:float, sign:str):
    function = mapper[sign]
    return function(num1, num2)
