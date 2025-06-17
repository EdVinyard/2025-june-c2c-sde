print('Welcome to the Cafe Curtis app!')

account_balance = 32    # integer
correct_pin = '123456'  # string
entered_pin = ''        # string

while entered_pin != correct_pin:
    entered_pin = input('PIN? ')

    if entered_pin != correct_pin:
        print('Incorrect PIN.  Try again.')

print('Hi, Ashley!')
print('Your current balance is $' + str(account_balance))

transfer_amount = input('How much will you transfer? ') # string
account_balance += int(transfer_amount)
print('Your new balance is $' + str(account_balance))
