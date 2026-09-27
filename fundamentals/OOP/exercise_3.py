class BankAccount:
    def __init__(self, current_owner, current_balance):
        self.owner = current_owner
        self.balance = current_balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawing: {amount}."
        return "Insufficient funds!"

    def show_balance(self):
        return f'Owner: {self.owner}\nBalance: {self.balance} '

    def has_money(self):
        if self.balance <= 0:
            print(f'You doesnt have money!')


owner = input()
balance = int(input())
deposit_amount = int(input())
withdraw_amount = int(input())

account = BankAccount(owner, balance)
account.has_money()
print(account.deposit(deposit_amount))
print(account.withdraw(withdraw_amount))
print(account.show_balance())


