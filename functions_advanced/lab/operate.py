from functools import reduce

def sum_nums(*args:tuple) -> tuple:
    return reduce(lambda x, y: x+y, args)

def sub_nums(*args:tuple) -> tuple:
    return reduce(lambda x, y: x-y, args)

def mul_nums(*args:tuple) -> tuple:
    return reduce(lambda x, y: x*y, args)

def div_nums(*args:tuple) -> tuple:
    return reduce(lambda x, y: x/y, args)


mapper = {
    '+': sum_nums,
    '-': sub_nums,
    '*': mul_nums,
    '/': div_nums
}

def operate(operator: str, *args: tuple) -> tuple:
    func = mapper[operator]
    return func(*args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))