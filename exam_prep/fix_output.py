total = 0
command = input()
while command not in ["special", "regular"]:
    price = float(command)

    if price > 0:
        total += price

    command = input()

total_with_tax = total * 1.20

if command == "special":
    total_with_tax *= 0.90

print(f"{total_with_tax:.2f}")
