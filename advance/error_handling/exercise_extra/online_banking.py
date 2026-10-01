class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = map(int,input().split(', '))
VALID_AGE = 18

while True:
    line = input().split('#')
    if line[0] == 'End':
        break

    if line[0] == 'Send Money':
        money, pin_code = int(line[1]), int(line[2])
        if balance < money:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')

        if pin_code != pin:
            raise PINCodeError('Invalid PIN code')

        if age < VALID_AGE:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')

        balance -= money
        print(f'Successfully sent {money} money to a friend')
        print(f'There is {balance} money left in the bank account')

    elif line[0] == 'Receive Money':
        money = int(line[1])

        if money < 0:
            raise MoneyIsNegativeError('The amount of money cannot be a negative number')

        account_money = money * 0.5
        balance += account_money

        print(f'{account_money} money went straight into the bank account')