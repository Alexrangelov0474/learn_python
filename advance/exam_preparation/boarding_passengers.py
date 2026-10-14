
def boarding_passengers(capacity: int, *passanger_groups: tuple):
    boarded = {}
    waiting_passangers = False

    for passangers, quality in passanger_groups:
        if passangers <= capacity:
            boarded[quality] = boarded.get(quality, 0) + passangers
            capacity -= passangers
        else:
            waiting_passangers = True
            if capacity <= 0:
                break

    sorted_passangers = sorted(boarded.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    result = ['Boarding details by benefit plan:']
    for quality, passangers in sorted_passangers:
        result.append(f'## {quality}: {passangers} guests')

    if not waiting_passangers:
        result.append('All passengers are successfully boarded!')

    elif capacity <= 0:
        result.append('Boarding unsuccessful. Cruise ship at full capacity.')

    else:
        result.append(f'Partial boarding completed. Available capacity: {capacity}.')

    return '\n'.join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print('==========================')
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print('==========================')
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))