basket = {}
while True:
    line = input().split()
    if line[0] == 'end':
        break

    fruit = line[0]
    quantity = int(line[1])
    if fruit not in basket:
        basket[fruit] = quantity
    else:
        basket[fruit] += quantity
total_quantity = 0
for fruits, quantities in basket.items():
    total_quantity = sum(basket.values())
    print(f'{fruits}: {quantities}')
total_fruits = len(basket)
print(f'Total Fruits: {total_fruits}')
print(f'Total Quantity: {total_quantity}')


