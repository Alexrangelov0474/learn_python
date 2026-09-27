text = input().split()
filtered_text = [char for char in text if (len(char) % 2 == 0)]
print('\n'.join(filtered_text))