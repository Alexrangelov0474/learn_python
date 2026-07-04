speed = float(input())
if speed <= 10:
    print(f'slow')
elif 10 < speed <= 50:
    print(f'average')
elif 50 < speed <= 150:
    print(f'fast')
elif 150 < speed <= 1000:
    print(f'ultra fast')
else:
    print(f'extremely fast')
