import decimal

deposit_amount = float(input(f'Enter your deposit amount: '))
period_deposit_amount = float(input(f'Enter your period deposit amount: '))
yearly_interest_rate = float(input(f'Enter your yearly interest rate: '))

montly_interest_rate = (deposit_amount * yearly_interest_rate) / 100 / 12

final_amount = deposit_amount + (period_deposit_amount * montly_interest_rate)

print(final_amount)