from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Optional

def validate_user(**user: dict) -> Optional[str]:
    if user['username'] == '' or \
            user['password'] == '' or \
            user['first_name'] == '' or \
            user['last_name'] == '':
        return 'All fields are required!'

    if len(user['username']) < 4:

        return 'Username must be at least 4 chars!'

    if len(user['password']) < 3:

        return 'Password must be at least 3 chars!'

    pass_validation_map = {'upper': False, 'lower': False, 'digit': False, 'special': False}

    for char in user['password']:
        if char in ascii_uppercase:
            pass_validation_map['upper'] = True

        elif char in ascii_lowercase:
            pass_validation_map['lower'] = True

        elif char in digits:
            pass_validation_map['digit'] = True

        elif char in punctuation:
            pass_validation_map['special'] = True

    if not all(pass_validation_map.values()):

        return 'Password must contain at least 1 lower, upper, digit and special character!'

    if len(user['first_name']) < 2:

        return 'First name must be at least 2 chars!'

    if len(user['last_name']) < 2:
        return 'Last name must be at least 2 chars!'
    return None