new_money = input()
total_money = 0.0

while new_money != 'NoMoreMoney':
    amount = float(new_money)
    if amount < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    total_money += amount
    new_money = input()

print(f'Total: {total_money:.2f}')