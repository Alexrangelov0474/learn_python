
record = float(input())
distance_in_metres = float(input())
seconds_for_meter = float(input())

total_seconds = distance_in_metres * seconds_for_meter
water_resistance = (distance_in_metres // 15 * 12.5)

total_time = (total_seconds + water_resistance)

if total_time >= record:
    time_needed = total_time - record

    print(f'No, he failed! He was {time_needed:.2f} seconds slower.')

else:
    new_record = total_seconds +water_resistance
    print(f'Yes, he succeeded! The new world record is  {new_record:.2f} seconds faster.')