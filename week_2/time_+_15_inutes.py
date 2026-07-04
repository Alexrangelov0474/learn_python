hours = int(input())
minutes = int(input())

total_minutes = (hours * 60) + minutes + 15

new_hours = total_minutes // 60 % 24
new_minutes = total_minutes % 60

print(f'{new_hours}:{new_minutes:02d}')
