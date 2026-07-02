number_of_lines = int(input())
synonyms = {}
for _ in range(number_of_lines):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym_list in synonyms.items():
    synonym_char = ', '.join(synonym_list)
    print(f'{word} - {synonym_char}')
