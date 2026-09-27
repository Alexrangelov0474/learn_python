number_of_lines = int(input())

positive_list = []
negative_list = []

for _ in range(number_of_lines):
    number = int(input())
    if number < 0:
        negative_list.append(number)
    else:
        positive_list.append(number)
print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}\n'
      f'Sum of negatives: {sum(negative_list)}')
