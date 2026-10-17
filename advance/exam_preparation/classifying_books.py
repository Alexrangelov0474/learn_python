def classify_books(*args, **kwargs):
    genres = {}
    for genre, title in args:
        genres[title] = genre

    fiction_books = []
    non_fiction_books = []

    for isbn, title in kwargs.items():
        genre = genres[title]

        if genre == 'fiction':
            fiction_books.append((isbn, title))
        else:
            non_fiction_books.append((isbn, title))

    sorted_fiction = sorted(fiction_books,key=lambda book: book[0])
    sorted_non_fiction = sorted(non_fiction_books,key=lambda book: book[0],reverse=True)

    result = []
    if sorted_fiction:
        result.append('Fiction Books:')
        for pair in sorted_fiction:
            result.append('~~~' + '#'.join(pair))

    if sorted_non_fiction:
        result.append('Non-Fiction Books:')
        for pair in sorted_non_fiction:
            result.append('***' + '#'.join(pair))

    return '\n'.join(result)



print(classify_books( ("fiction", "Brave New World"), ("non_fiction", "The Art of War"), NF3421NN="The Art of War", FF1234UU="Brave New World" ))
print('==================')
print(classify_books(    ("fiction", "Brave New World"),    ("fiction", "The Catcher in the Rye"),    ("fiction", "1984"),    FICCITRZZ="The Catcher in the Rye",    FIC1984XX="1984",    FICBNWYYY="Brave New World" ))
print('==================')
print(classify_books(    ("non_fiction", "Sapiens"),    ("non_fiction", "Homo Deus"),    ("non_fiction", "The Selfish Gene"),    NF123ABC="Sapiens",    NF987XYZ="Homo Deus",    NF456DEF="The Selfish Gene" ))