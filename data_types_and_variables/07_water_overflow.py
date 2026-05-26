number_of_lines = int(input())
water_capacity = 255

for current_line in range(number_of_lines):
    water_added = int(input())

    if water_capacity < water_added:
        print('Insufficient capacity!')
        continue
    water_capacity -= water_added

print(255 - water_capacity)

