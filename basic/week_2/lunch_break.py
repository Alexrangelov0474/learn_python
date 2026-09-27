from math import ceil
series_name = str(input())
episode_time = int(input())
break_time = int(input())

lunch_time = break_time * (1/8)
chill_time = break_time * (1/4)

time_left = break_time - lunch_time - chill_time

diff = abs(time_left - episode_time)

if time_left >= episode_time:
    print(f'You have enough time to watch {series_name} and left with {ceil(diff)} minutes free time.')

else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(diff)} more minutes.")