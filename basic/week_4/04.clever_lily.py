lily_age = int(input())
washing_machine = float(input())
toy_price = int(input())

money_saved = 0
money_gift = 10
toys_count = 0

for age in range(1, lily_age + 1):
    if age % 2 == 0:
        money_saved += money_gift
        money_gift += 10
        money_saved -= 1
    else:
        toys_count += 1

money_saved += toys_count * toy_price
diff = abs(money_saved - washing_machine)

if money_saved >= washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
