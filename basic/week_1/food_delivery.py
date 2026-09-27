from math import ceil

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_cost = 2.50
#Dessert = 20 % from total, without delivery

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

chicken_menu_cost = number_chicken_menu * chicken_menu_price
fish_menu_cost = number_fish_menu * fish_menu_price
vegetarian_menu_cost = number_vegetarian_menu * vegetarian_menu_price

total_cost_menus = chicken_menu_cost + fish_menu_cost + vegetarian_menu_cost
dessert_price = total_cost_menus * 0.20

final_price = total_cost_menus + dessert_price + delivery_cost

print(f'Order price: {final_price:.2f}')

