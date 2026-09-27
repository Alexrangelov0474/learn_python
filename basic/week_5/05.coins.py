
price = int(float(input())* 100)
coin_counter = 0

while price > 0:
    if price >= 200:
        price -= 200
    elif price >= 100:
        price -= 100
    elif price >= 50:
        price -= 50
    elif price >= 20:
        price -= 20
    elif price >= 10:
        price -= 10
    elif price >= 5:
        price -= 5
    elif price >= 2:
        price -= 2
    elif price >= 1:
        price -= 1

    coin_counter += 1

print(coin_counter)