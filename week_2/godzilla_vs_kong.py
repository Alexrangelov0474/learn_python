from math import floor

budget = float(input())
extras = int(input())
price_single_dress = float(input())

decor = budget * 0.10
dress_price = extras * price_single_dress

if extras > 150:
    dress_price = dress_price - (dress_price * 0.10)

total_movie_price = decor + dress_price

money_left = budget - total_movie_price

if budget < total_movie_price:
    money_needed = abs(budget - total_movie_price)
    print(f'not enough money!')
    print(f'Wingard needs {money_needed:.2f} euro more!')
else:
    print(f'ACTION!')
    print(f'Wingard starts filming with {money_left:.2f} euro left!')