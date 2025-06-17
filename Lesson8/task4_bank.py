balance = 0

def input_amount(deposit_or_withdraw):
    amount = 0
    while amount <= 0:
        amount = int(input('How much will you ' + deposit_or_withdraw + '? '))
        if amount <= 0:
            print('Invalid ' + deposit_or_withdraw + ' amount.')

    return amount

option = ''
while option != 'q':
    option = input('(D)eposit, (W)ithdraw, (B)alance, or (Q)uit? ').lower()

    if option == 'd':
        balance += input_amount('deposit')
    elif option == 'w':
        balance -= input_amount('withdraw')

    if option != 'q':
        print('Your current balance is $' + str(balance) + '.')

print('Goodbye!')
