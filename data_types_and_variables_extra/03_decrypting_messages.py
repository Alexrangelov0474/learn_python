key = int(input())
number_of_lines = int(input())
word = ''
for line in range(number_of_lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    word += new_letter

print(word)