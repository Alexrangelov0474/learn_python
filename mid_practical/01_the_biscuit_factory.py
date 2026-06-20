days_of_the_month = 30
total_production = 0
biscuit_per_day = 0
biscuits_per_worker = int(input())
workers = int(input())
competing_factory_production = int(input())

for day in range(1, days_of_the_month +1):
    biscuit_per_day = 0

    if day % 3 == 0:
        biscuit_per_day = int((biscuits_per_worker * workers) * 0.75)
        total_production += biscuit_per_day
    else:
        total_production += biscuits_per_worker * workers

print(f'You have produced {total_production} biscuits for the past month.')
diff = total_production - competing_factory_production
percentage = diff / competing_factory_production * 100
if total_production > competing_factory_production:
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {abs(percentage):.2f} percent less biscuits.')