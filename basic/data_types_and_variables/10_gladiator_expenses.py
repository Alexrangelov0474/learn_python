number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_broken_helmets = number_of_lost_fights // 2
total_broken_swords = number_of_lost_fights // 3
total_broken_shields = number_of_lost_fights // (2 * 3)
total_broken_armors = total_broken_shields // 2
total_cost = total_broken_helmets * helmet_price + \
           total_broken_swords * sword_price + \
           total_broken_shields * shield_price + \
           total_broken_armors * armor_price
print(f'Gladiator expenses: {total_cost:.2f} aureus')