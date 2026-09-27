class Library:

    def __init__(self):
        self.list_of_books = []

    def add_book(self ,current_title):
        self.list_of_books.append(current_title)


    def remove_book(self, current_title):
        self.list_of_books.remove(current_title)


    def show_books(self):
        books = "\n".join(self.list_of_books)
        return f"Books:\n{books}"

    def books_count(self):
        counter = len(self.list_of_books)
        return counter

library = Library()

while True:

    action = input().split()
    command = action[0]

    if command == 'show':
        print(library.show_books())
    elif command == 'add':
        title = action[1]
        library.add_book(title)
    elif command == 'remove':
        title = action[1]
        library.remove_book(title)
    elif command == 'count':
        count = library.books_count()
        print(f'Number of books: {count}')
    elif command == 'end':
        break



