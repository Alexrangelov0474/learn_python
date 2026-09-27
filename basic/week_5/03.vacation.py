money_needed = float(input())
available_money = float(input())
action_count = 0
days_count = 0

while True:

    action = input()
    new_money = float(input())
    days_count += 1
    if action == 'spend':
        action_count += 1
        available_money -= new_money
        if action_count == 5:
            print(f"You can't save the money.\n{days_count}")
            break
    else:
        action_count = 0
        available_money += new_money

    if available_money < 0:
        available_money = 0

    elif available_money >= money_needed:
        print(f"You saved the money for {days_count} days.")
        break








