cells = input().split('#')
amount_water = int(input())
total_fire = 0
total_effort = 0
high = range(81, 125+1)
medium = range(51, 80+1)
low = range(1, 50+1)
fire_cells = []
for cell in cells:
    fire_type, fire_value = cell.split(' = ')
    fire_value = int(fire_value)
    cell_is_valid = False
    if fire_type == 'High':
        if fire_value in high:
            cell_is_valid = True
    elif fire_type == 'Medium':
        if fire_value in medium:
            cell_is_valid = True
    elif fire_type == 'Low':
        if fire_value in low:
            cell_is_valid = True
    if cell_is_valid:
        if amount_water >= fire_value:
            amount_water -= fire_value
            fire_cells.append(fire_value)
            total_effort += fire_value * 0.25
            total_fire += fire_value
print('Cells:')
for fire_cell in fire_cells:
    print(f"- {fire_cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")