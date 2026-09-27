total_orders = 0
total_profit = 0

french_fries = 0
burgers = 0
pizza = 0
sushi = 0

flag = False

while True:
    order = input()

    if order == 'Finish':
        break

    while True:
        product_type = input()

        if product_type == 'Enough':
            total_orders += 1
            break

        if product_type == 'french_fries':
            french_fries += 1
            total_profit += 4.00
        elif product_type == 'burgers':
            burgers += 1
            total_profit += 10.00
        elif product_type == 'pizza':
            pizza += 1
            total_profit += 7.00
        elif product_type == 'sushi':
            sushi += 1
            total_profit += 15.00


        if total_profit >= 60:
            flag = True

    if flag:
        break

if flag:
    print("Target acquired.")
else:
    print("Target not reached.")

print(f"{total_orders} orders completed.")
print(f"Profit: {total_profit:.2f} lv.")

if total_orders > 0:
    avg_price = total_profit / total_orders
    print(f"Average order value: {avg_price:.2f} lv.")

print(f"We sold {burgers} burgers.\n{pizza} pizza\n{french_fries} french fries\n{sushi} sushi")



    













