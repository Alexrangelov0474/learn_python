
def calculation(operation, a , b):
    if operation == 'add':
        return  a + b
    elif operation == 'subtract':
        return  a - b
    elif operation == 'multiply':
        return  a * b
    elif operation == 'divide':
        return  int(a / b)


operation_ = input()
a_ = int(input())
b_ = int(input())

result = calculation(operation_,a_,b_)
print(result)