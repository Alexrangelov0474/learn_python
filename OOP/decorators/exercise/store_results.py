class store_results:
    def __init__(self, filename):
        self.filename = filename


    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(self.filename, 'a') as f:
                result = func(*args, **kwargs)
                f.write(f"Function '{func.__name__}' was called. Result: {result}\n")

            return result
        return wrapper


@store_results('results.txt')
def add(a, b):
    return a + b
@store_results('results.txt')
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)