days = int(input())
plunder_per_day = int(input())
target = int(input())

total = 0

for day in range(1, days):
    total += plunder_per_day

    if day % 3 == 0:
        total += plunder_per_day * 1.5

    if day % 5 == 0:
        total *= 0.70

if total >= target:
    print("Success!")
else:
    print("Failed!")