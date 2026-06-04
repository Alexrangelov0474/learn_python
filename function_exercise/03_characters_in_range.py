def char_in_range(num_1, num_2):
    lst = []

    for char in range(num_1 +1, num_2):
        lst.append(chr(char))

    return ' '.join(lst)

num_1 = ord(input())
num_2 = ord(input())

print(char_in_range(num_1,num_2))