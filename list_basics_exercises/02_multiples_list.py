factor = int(input())
count = int(input())
lst = []

for number in range(1, count + 1):
    factored_number = number * factor
    lst.append(factored_number)
print(lst)