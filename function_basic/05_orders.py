total_price = 0

def calculation_recip(price, amount):
    return price * amount

item = input()
amount = int(input())

if item == "coffee":
    price = 1.50
elif item == "water":
    price = 1.00
elif item == "coke":
    price = 1.40
elif item == "snacks":
    price = 2.00

total_price = calculation_recip(price, amount)
print(f"{total_price:.2f}")
