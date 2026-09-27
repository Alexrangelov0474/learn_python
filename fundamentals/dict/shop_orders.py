basket = {}
while True:
    order = input().split()
    if order[0] == 'finish':
        break

    customer = order[0]
    product = order[1].capitalize()
    if customer not in basket.keys():
        basket[customer] = []

    exist = False
    for current_product in basket[customer]:
        if current_product == product:
            exist = True
            break

    if not exist:
        basket[customer].append(product)

total_customers = 0
total_products = 0
print('Orders:')
for customers, products in basket.items():

    print(f'{customers} -> {", ".join(products)}')
total_products = sum(len(products) for products in basket.values())
total_customers = len(basket)
print(f'Total customers: {total_customers}')
print(f'Total products: {total_products}')
