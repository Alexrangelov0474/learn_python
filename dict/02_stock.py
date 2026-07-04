elements = input().split()
stock = {}

for element in range(0,len(elements), 2):
    products = elements[element]
    quantities = elements[element + 1]
    stock[products] = quantities

product_to_search = input().split()

for product in product_to_search:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")