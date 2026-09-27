list_of_crops = list(input().split(' & '))
action = input().split()
while action[0] != 'Collect!':
    if action[0] == 'Plant':
        crop = action[1]
        if crop not in list_of_crops:
            list_of_crops = [crop] + list_of_crops
    if action[0] == 'Transplant':
        crop = action[1]
        if crop in list_of_crops:
            index = list_of_crops.index(crop)
            moved_crop =list_of_crops.pop(index)
            list_of_crops.append(moved_crop)
    if action[0] == 'Replace':
        first_index = int(action[1])
        second_index = int(action[2])
        if 0 <= first_index < len(list_of_crops) and 0 <= second_index < len(list_of_crops):
            list_of_crops[first_index], list_of_crops[second_index] = \
            list_of_crops[second_index], list_of_crops[first_index]
    if action[0] == 'Uproot':
        crop = action[1]
        if crop in list_of_crops:
            list_of_crops.remove(crop)

    action = input().split()

if len(list_of_crops) > 1:
    print(' | '.join(list_of_crops))
else:
    print(''.join(list_of_crops))


