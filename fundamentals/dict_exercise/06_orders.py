products = {}
total_price = 0

while True:
    product = input().split()
    if product[0] == 'buy':
        break

    name = product[0]
    price =float(product[1])
    quantity = int(product[2])


    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity


for name,price_quantity_list in products.items():
    price = price_quantity_list[0]
    quantity = price_quantity_list[1]
    total_price = price * quantity
    print(f'{name} -> {total_price:.2f}')