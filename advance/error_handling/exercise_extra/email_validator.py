class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

EMAIL_MIN_SIM = 4
DOMAINS = {'com', 'bg', 'org', 'net'}

while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if len(email.split('@')[0]) < EMAIL_MIN_SIM:
        raise NameTooShortError('Name must be more than 4 characters')

    domain = email.split('.')[-1]
    if domain not in DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')

