time1 = int(input())
time2 = int(input())
time3 = int(input())

total_seconds = time1 + time2 + time3

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f'{minutes}:{seconds:02d}')
