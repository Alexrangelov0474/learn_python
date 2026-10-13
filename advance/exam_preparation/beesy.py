n_rows = int(input())
BEE_ENERGY = 15

matrix = []
bee_r, bee_c = 0, 0

for row in range(n_rows):
    line = list(input())
    if 'B' in line:
        bee_r, bee_c = row, line.index('B')



