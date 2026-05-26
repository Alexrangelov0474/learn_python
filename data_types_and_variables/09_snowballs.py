number_of_balls = int(input())
total_weight = 0
total_time = 0
total_quality = 0
total_value = 0
for current_ball in range(number_of_balls):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight // current_time) \
                    ** current_quality
    if current_value > total_value:
        total_weight = current_weight
        total_time = current_time
        total_quality = current_quality
        total_value = current_value

print(f'{total_weight} : {total_time} = {total_value} ({total_quality})')
