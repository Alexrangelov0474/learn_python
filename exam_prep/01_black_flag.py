days = int(input())
plunder_for_a_day = int(input())
target_plunder = int(input())
total_plunder = 0
for day in range(1, days + 1):
    if day % 3 == 0:
        total_plunder += plunder_for_a_day * 1.5
    else:
        total_plunder += plunder_for_a_day

    if day % 5 == 0:
        total_plunder *= 0.70


if total_plunder >= target_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    percentage = total_plunder / target_plunder * 100
    print(f'Collected only {percentage:.2f}% of the plunder.')
