money_string = input().split(', ')
number_of_beggars = int(input())
money_as_integer = []

for money in money_string:
    money_as_integer.append(int(money))
beggars_sum = []
starting_index = 0

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(starting_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[index]
    beggars_sum.append(current_beggar_sum)
    starting_index += 1
print(beggars_sum)