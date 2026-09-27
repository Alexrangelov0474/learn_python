starting_interval = int(input())
end_interval = int(input())

for num in range(starting_interval, end_interval + 1):
    num_str = str(num)
    even_sum = 0
    odd_sum = 0

    for position in range(6):
        dig = int(num_str[position])

        if (position + 1) % 2 == 0:
            even_sum += dig
        else:
            odd_sum += dig

    if even_sum == odd_sum:
        print(num, end=' ')

