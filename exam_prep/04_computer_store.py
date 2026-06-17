total_price_without_tax = 0
total_price_with_tax = 0
taxes = 0
order = input()
while order != 'special' and order != 'regular':
    order_as_integer = float(order)
    if order_as_integer < 0 :
        print('Invalid price!')
    else:
        total_price_without_tax += order_as_integer
    order = input()

total_price_with_tax = total_price_without_tax * 1.20
taxes = total_price_with_tax - total_price_without_tax

if total_price_with_tax == 0:
    print('Invalid order!')
else:
    if order == 'special':
        total_price_with_tax *= 0.90

    print("Congratulations you've just bought a new computer!\n"
        f"Price without taxes: {total_price_without_tax:.2f}$\n"
        f"Taxes: {taxes:.2f}$\n"
        f"-----------\n"
        f"Total price: {total_price_with_tax:.2f}$")

