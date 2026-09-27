number_of_lines = int(input())
heroes = {}
for line in range(number_of_lines):
    hero, health, mana = input().split('|')
    heroes[hero] = {
        'health':int(health),
        'mana':int(mana)
    }
while True:
    command = input().split(' : ')
    if command[0] == 'End':
        break

    action = command[0]
    if action == 'Cast':
        hero, mana_needed, spell = command[1], int(command[2]), command[3]
        if heroes[hero]['mana'] >= mana_needed:
            heroes[hero]['mana'] -= mana_needed
            mana_left = heroes[hero]['mana']
            print(f'{hero} has successfully cast {spell} and now has {mana_left} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell}!')

    elif action == 'Heal':
        hero, amount = command[1],int(command[2])
        current_health = heroes[hero]['health']
        if current_health + amount >= 100:
            heroes[hero]['health'] = 100
            healed_amount = 100 - current_health
        else:
            healed_amount = amount
            heroes[hero]['health'] += amount
        print(f'{hero} healed for {healed_amount} HP!')

    elif action == 'Recharge':
        hero, amount = command[1], int(command[2])
        current_mana = heroes[hero]['mana']
        if current_mana + amount >= 200:
            heroes[hero]['mana'] = 200
            recharge_amount = 200 - current_mana
        else:
            recharge_amount = amount
            heroes[hero]['mana'] += amount
        print(f'{hero} recharged for {recharge_amount} MP!')

    elif action == 'Damage':
        hero, damage, attacker = command[1], int(command[2]), command[3]
        current_hp = heroes[hero]['health']
        if current_hp - damage <= 0:
            print(f'{hero} has been killed by {attacker}!')
            del heroes[hero]
        else:
            hp_left = current_hp - damage
            heroes[hero]['health'] = hp_left
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!')

for hero, data in heroes.items():
    health, mana = data['health'], data['mana']
    print(f'{hero}\n HP: {health}\n MP: {mana}')
