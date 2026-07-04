library = {}
while True:
    line = input().split()
    if line[0] == 'end':
        break


    author = line[0]
    book = line[1]

    if author not in library:
        library[author] = []

    exists = False
    for current_book in library[author]:
        if current_book.lower() == book.lower():
            exists = True
            break

    if not exists:
        library[author].append(book)

total_authors = len(library)
total_books = sum(len(books) for books in library.values())

print('Library:')
for author, book in library.items():
    books_char = ', '.join(book)
    print(f'{author}: {books_char}')
print(f'Total books: {total_books}')
print(f'Total authors: {total_authors}')