while True:
    location = input()
    if location == 'End':
        break

    budget = float(input())
    money = 0.0

    while money < budget:
        money_saved = float(input())
        money += money_saved

    print(f'Going to {location}!')


