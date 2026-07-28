import re

library = {}
pattern = r'([!#])([A-Z][A-Za-z]{2,})\1[<]([A-Z][a-z]{2,})[>]'
line_with_books = input()
for match in re.finditer(pattern, line_with_books):
    title = match.group(2)
    author = match.group(3)
    if title not in library:
        library[title] = []
    library[title].append(author)

def add_books(library_dict:dict, book_title:str, book_author: str) -> None:
    if book_title in library_dict.keys() and book_author not in library_dict[book_title]:
        library_dict[book_title].append(book_author)

def remove_books(library_dict:dict, book_title:str, book_author: str) -> None:
    if book_title in library_dict and book_author in library_dict[book_title]:
            library_dict[book_title].remove(book_author)

def change_books(library_dict:dict, book_title:str, book_author: str) -> None:
    if book_title in library_dict and library_dict[book_title]:
        library_dict[book_title][0] = book_author


while True:
    command = input()
    if command == 'Stop':
        break

    action, title, author = command.split(':')

    if action == 'Add':
        add_books(library, title, author)
    elif action == 'Remove':
        remove_books(library, title, author)
    elif action == 'Change':
        change_books(library, title, author)

for title, authors in library.items():
    print(f'{title}:')
    for author in authors:
        print(f'- {author}')



