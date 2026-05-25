n = int(input())

counter = 1
rows = 1

while counter <= n:
    for _ in range(rows):
        if counter > n:
            break

        print(counter, end=" ")
        counter += 1

    print()
    rows += 1
