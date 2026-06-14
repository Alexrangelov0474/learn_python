
numbers = list(map(int, input().split(', ')))
group = 10
while numbers:
    lst_of_numbers = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {lst_of_numbers}")
    group += 10
    # numbers = [number for number in numbers if number not in lst_of_numbers]
    for num in lst_of_numbers:
        numbers.remove(num)