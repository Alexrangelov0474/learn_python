n = int(input())
for power in range(n + 1): #<---- така върти до + 1 за да включа и числото n
    if power % 2 == 0:
        result = 2 ** power #<--- Така се изписва число на степен (**)
        print(result)