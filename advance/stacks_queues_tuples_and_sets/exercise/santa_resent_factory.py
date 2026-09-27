from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

items = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafter_presents = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]

    if total_magic in items.keys():
        crafted_item = items[total_magic]
        crafter_presents[crafted_item] = crafter_presents.get(crafted_item, 0) + 1
        materials.pop()
        magic.popleft()

    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())

    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15

    else:
        if materials[-1] == 0:
            materials.pop()

        if magic[0] == 0:
            magic.popleft()

if ('Doll' in crafter_presents.keys() and 'Wooden train' in crafter_presents.keys()) \
        or ('Teddy bear' in crafter_presents.keys() and 'Bicycle' in crafter_presents.keys()):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(map(str, reversed(materials)))}')
if magic:
    print(f'Magic left: {", ".join(map(str, magic))}')

for present, amount in sorted(crafter_presents.items()):
    print(f'{present}: {amount}')