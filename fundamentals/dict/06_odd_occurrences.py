words = input().split()
sequence_words = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in sequence_words:
        sequence_words[lower_word] = 0
    sequence_words[lower_word] += 1

for key, value in sequence_words.items():
    if value % 2 != 0:
        print(key, end=" ")
