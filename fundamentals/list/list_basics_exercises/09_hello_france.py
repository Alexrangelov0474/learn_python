collection_of_items = input().split('|')
starting_budget = float(input())
max_price_clothe = 50.00
max_price_shoes = 35.00
max_price_accessories = 20.50
bought_items = []
profit = 0

for item in collection_of_items:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    item_bought = False

    if item_type == 'Clothes':
        if item_price <= max_price_clothe and item_price <= starting_budget:
            starting_budget -= item_price
            item_bought = True
    elif item_type == 'Shoes':
        if item_price <= max_price_shoes and item_price <= starting_budget:
            starting_budget -= item_price
            item_bought = True
    elif item_type == 'Accessories':
        if item_price <= max_price_accessories and item_price <= starting_budget:
            starting_budget -= item_price
            item_bought = True

    if item_bought:
        new_price = item_price * 1.40
        bought_items.append(new_price)
        profit += new_price - item_price

for price in bought_items:
    print(f'{price:.2f}',end=' ')

print()
print(f"Profit: {profit:.2f}")
sum_after_selling = starting_budget + sum(bought_items)

if sum_after_selling >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")