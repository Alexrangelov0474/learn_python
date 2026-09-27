def password_length(some_password: str) -> str or bool:
    if 6 <= len(some_password) <= 10:
        return True
    return "Password must be between 6 and 10 characters"

def only_letter_or_digits(some_password: str) -> str or bool:
    if some_password.isalnum():
        return True
    return "Password must consist only of letters and digits"


def least_two_digits(some_password: str) -> str or bool:
    number_of_digits = 0
    for digit in some_password:
        if digit.isdigit():
            number_of_digits += 1
    if number_of_digits >= 2:
        return True
    return "Password must have at least 2 digits"


def validation_password(some_password:str) -> list:
    is_valid = []
    is_valid.append(password_length(some_password))
    is_valid.append(only_letter_or_digits(some_password))
    is_valid.append(least_two_digits(some_password))
    for idx in range(len(is_valid)-1,-1,-1):
        if isinstance(is_valid[idx], bool):
            is_valid.pop(idx)

    return is_valid

password = input()
password_is_not_valid = validation_password(password)
if password_is_not_valid:
    print('\n'.join(password_is_not_valid))
else:
    print("Password is valid")