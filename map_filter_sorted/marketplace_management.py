stores = {}

def check_store_exists(stores_dict: dict, current_store: str) -> bool:
    return current_store in stores_dict


def product_exists_in_store(stores_dict: dict, current_store: str, current_product: str) -> bool:
    return current_product in stores_dict[current_store]


while True:
    line = input()
    if line == 'Build':
        break

    store_type, product_type, price, quantity = line.split(' => ')
    price = int(price)
    quantity = int(quantity)

    if not check_store_exists(stores, store_type):
        stores[store_type] = {}
    if not product_exists_in_store(stores, store_type, product_type):
        stores[store_type][product_type] = {}

    stores[store_type][product_type]['price'] = price
    stores[store_type][product_type]['quantity'] = quantity


def add_product(store_dict: dict, current_store: str, current_product:str, current_price: int, current_quantity: int):
    if not check_store_exists(store_dict, current_store):
        store_dict[current_store] = {}

    if not product_exists_in_store(store_dict, current_store, current_product):
        store_dict[current_store][current_product] = {}

    store_dict[current_store][current_product]['price'] = current_price
    store_dict[current_store][current_product]['quantity'] = current_quantity

def restock_the_store(store_dict: dict, current_store: str, current_product: str, current_quantity:int):
    if not check_store_exists(store_dict, current_store):
        print('The store did not exists!')
        return
    if not product_exists_in_store(store_dict, current_store, current_product):
        print('The product did not exists!')
        return
    store_dict[current_store][current_product]['quantity'] += current_quantity

def discount_the_price(store_dict: dict, current_store: str, current_product: str, current_discount:int):
    if not check_store_exists(store_dict, current_store):
        print('The store did not exists!')
        return
    if not product_exists_in_store(store_dict, current_store, current_product):
        print('The product did not exists!')
        return

    old_price = store_dict[current_store][current_product]['price']
    store_dict[current_store][current_product]['price'] = old_price * (1 - current_discount / 100)

def sell_product(store_dict: dict, current_store: str, current_product: str, current_sell_quantity:int):
    if not check_store_exists(store_dict, current_store):
        print('The store did not exists!')
        return
    if not product_exists_in_store(store_dict, current_store, current_product):
        print('The product did not exists!')
        return
    if store_dict[current_store][current_product]['quantity'] >= current_sell_quantity:
        store_dict[current_store][current_product]['quantity'] -= current_sell_quantity
    else:
        print('Not enought quantity to sell!')


while True:
    command = input().split(' => ')
    if command[0] == 'End':
        break

    action, store, product = command[0], command[1], command[2]

    if action == 'Add':
        price, quantity = int(command[3]), int(command[4])
        add_product(stores, store, product, price, quantity)

    elif action == 'Restock':
        quantity = int(command[3])
        restock_the_store(stores, store, product, quantity)

    elif action == 'Discount':
        percent_to_decrease = int(command[3])
        discount_the_price(stores, store, product, percent_to_decrease)

    elif action == 'Sell':
        sell_quantity = int(command[3])
        sell_product(stores, store, product, sell_quantity)


