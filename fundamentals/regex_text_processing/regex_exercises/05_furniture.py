import re

total_cost = 0
pattern = r'>>([A-Za-z]+)<<(\d+.?\d+)!(\d+)'
bought_furniture = []

while True:
    line = input()
    if line == 'Purchase':
        break
    match = re.search(pattern, line)
    if match:
        furniture_name, price, quantity = match.groups()
        bought_furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)

print('Bought furniture:')
for furnitures in bought_furniture:
    print(furnitures)
print(f'Total money spend: {total_cost:.2f}')