

n = int(input())
comb_counter = 0

for n1 in range(n + 1):
    for n2 in range(n + 1):
        for n3 in range(n + 1):
            if n1 + n2 + n3 == n:
                comb_counter += 1

print(comb_counter)