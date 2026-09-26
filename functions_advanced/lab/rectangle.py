def rectangle(lenght: int, width: int):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return 'Enter valid values!'

    def area():
        return lenght * width

    def perimeter():
        return 2 * lenght + 2 * width

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
print(rectangle(2, 10))
print(rectangle('2', 10))