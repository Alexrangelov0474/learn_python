n_groups = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
total_peoples = 0

for _ in range(n_groups):
    group_size = int(input())
    total_peoples += group_size

    if group_size <= 5:
        g1 += group_size
    elif group_size <= 12:
        g2 += group_size
    elif group_size <= 25:
        g3 += group_size
    elif group_size <= 40:
        g4 += group_size
    else:
        g5 += group_size

g = [g1, g2, g3, g4, g5]

for idx in g:
    print(f'{idx / total_peoples * 100:.2f}%')
