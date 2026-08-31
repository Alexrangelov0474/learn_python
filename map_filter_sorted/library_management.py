libraries = {}

def check_library_exists(libraries_dict: dict, library_name: str) -> bool:
    return library_name in libraries_dict

def check_book_exists(libraries_dict: dict, library_name: str, book_name: str,) -> bool:
    return book_name in libraries_dict[library_name]


while True:
    line = input().split(' => ')
    if line[0] == 'Build':
        break

    library, book, author, rating, copies = line[0], line[1], line[2], float(line[3]), int(line[4])

    if not check_library_exists(libraries, library):
        libraries[library] = {}

    if not check_book_exists(libraries, library, book):
        libraries[library][book] = {}

    libraries[library][book]['author'] = author
    libraries[library][book]['rating'] = rating
    libraries[library][book]['copies'] = copies

def validate_book(libraries_dict: dict, library_name: str, book_name: str) -> bool:
    return library_name in libraries_dict and book_name in libraries_dict[library_name]

def add_or_update_book(libraries_dict: dict, library_name: str, book_name: str,
                       author_name: str, current_rating: float, current_copies: int):
    if not check_library_exists(libraries_dict, library_name):
        libraries_dict[library_name] = {}
    if not check_book_exists(libraries_dict, library_name, book_name):
        libraries_dict[library_name][book_name] = {}

    libraries_dict[library_name][book_name]['author'] = author_name
    libraries_dict[library_name][book_name]['rating'] = current_rating
    libraries_dict[library_name][book_name]['copies'] = current_copies

def borrow_the_copies(libraries_dict: dict, library_name: str, book_name: str, copies_to_remove: int):
    if not validate_book(libraries_dict, library_name, book_name):
        print('Invalid!')
        return

    if copies_to_remove <= libraries_dict[library_name][book_name]['copies']:
        libraries_dict[library_name][book_name]['copies'] -= copies_to_remove

    else:
        print('Not enought copies to remove!')

def increase_the_copies(libraries_dict: dict, library_name: str, book_name: str, copies_to_return: int):
    if not validate_book(libraries_dict, library_name, book_name):
        print('Invalid!')
        return

    libraries_dict[library_name][book_name]['copies'] += copies_to_return

def rating_replace(libraries_dict: dict, library_name: str, book_name: str, rating_to_replace: float):
    if not validate_book(libraries_dict, library_name, book_name):
        print('Invalid!')
        return

    libraries_dict[library_name][book_name]['rating'] = rating_to_replace


while True:
    command = input().split(' => ')
    if command[0] == 'End':
        break

    action, library, book = command[0], command[1], command[2]

    if action == 'Add':
        author, rating, copies = command[3], float(command[4]), int(command[5])
        add_or_update_book(libraries, library, book, author, rating, copies)

    elif action == 'Borrow':
        borrow_copies = int(command[3])
        borrow_the_copies(libraries, library, book, borrow_copies)

    elif action == 'Return':
        return_copies = int(command[3])
        increase_the_copies(libraries, library, book, return_copies)

    elif action == 'Rate':
        rating = float(command[3])
        rating_replace(libraries, library, book, rating)



