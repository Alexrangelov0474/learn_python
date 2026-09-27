target = 100
money_saved = 0
command = input()
flag = False
money = 0

while command != 'End':
    command = int(command)
    if command == 0:
        print(f'Invalid')
    elif command < 0:
        print(f'you take: {command}')

    money_saved += command

    if money_saved >= target:
        flag = True
        break

    command = input()

diff = abs(target - money_saved)
print(f'Congratulation you saved: {money_saved:.2f}')
if not flag:
    print(f'You need: {diff:.2f} euro')
flag = False

money = money_saved
products = ''

while True:
    if money <= 0:
        print('No money left')
        break

    choice = input('choose product: ')

    if choice == 'End':
        break

    if choice == 'burger':
        price = 25

    elif choice =='pizza':
       price = 37

    elif choice == 'sushi':
        price = 50

    else:
        print('Invalid')
        continue


    if money >= price:
        money -= price
        products += choice + ' '
        print(f'You take: {choice}')
    else:
        diff = abs(money - price)
        print(f'Not enough money\nYou need: {diff:.2f} euro')
        flag = True
        break

print(f'Products: {products}')

if not flag:
    print(f'Money left: {money:.2f}')
