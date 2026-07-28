import re
text = input()
pattern = r'([#@]+)([A-Z][a-z]{2,})([#@]+)'
valid_hashtag_counter = 0
valid_hashtags = []
for match in re.finditer(pattern,text):
    left = match.group(1)
    word = match.group(2)
    right = match.group(3)
    if left == right:
        valid_hashtag_counter += 1
        valid_hashtags.append(left + word + right)


print(f'Valid hashtags: {valid_hashtag_counter}')
print('\n'.join(valid_hashtags))