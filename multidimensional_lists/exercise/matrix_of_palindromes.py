n_rows, n_cols = map(int, input().split())

start = ord('a')

for row in range(n_rows):
    for col in range(n_cols):
        print(f'{chr(start + row)}{chr(start + row + col)}{chr(start + row)}', end=' ')
    print()