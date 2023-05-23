import random
import sys
# Global variables
balance = 0
new_pin = random.randint(1000, 9999)
account_data = 'account_data.txt'

# Load account data from file
def load_data():
    account_record = []
    with open (account_data, 'r') as f:
        for line in f:
            account_record.append(line.strip().split(','))
    return account_record
    
# Account creator function
def create_account():
    print('Account Creator')
    user_name = input('Enter your Full Name > ')
    card_type = input('''Select the type of card you would like using the number keys:
                    [1] Debit Card
                    [2] Credit Card
                    > ''')
    if card_type == '1':
        card_type = ('Debit Card')
    if card_type == '2':
        card_type = ('Credit Card')
    validation_date = ('05/23')
    expiry_date = ('05/28')
    bank_name = ('UKBank')
    # Creating random numbers for account numbers
    card_number = [random.randint(0,9) for i in range(16)]
    sort_code = [random.randint(0,9) for i in range(6)]
    account_number = [random.randint(0,9) for i in range(8)]
    print(f'Here is your new {card_type}')
    # Draw card
    print(f'''
-------------------------------------------------
                    {bank_name}
{card_number}
{validation_date} {expiry_date}
{user_name}
{sort_code} {account_number}
{card_type}
-------------------------------------------------''')
    print(f'Your current balance is £{balance}, use the ATM to withdraw or deposit money')
    print(f'Your PIN is {new_pin}, use this to access your account')
        # Save user information to file
    with open(account_data, 'a') as f:
         f.write(f'{user_name},{card_type},{validation_date},{expiry_date},{bank_name},{"".join(map(str, card_number))},{"".join(map(str, sort_code))},{"".join(map(str, account_number))},{balance},{new_pin}\n')

# ATM function
def ATM():
    global balance
    global new_pin
    pincheck = True
    account_record = load_data()
    # Verifying correct PIN is inputted
    while pincheck:
        found = False
        record_number = 0
        pin_input = int(input('Enter PIN > '))
        for user in account_record: # Iterating through the account record array
            if str(pin_input) == user[-1]: # Checking pin inputted against every pin in file
                found = True
                balance = int(user[-2]) # Updating balance with value from file
            if found:
                break
            record_number +=1 # Taking down the record of the account accessed so the balance can be correctly overwritten
        if not found:
            print('Incorrect PIN try again')
        else:
            pincheck = False
            atm = True
            # ATM menu interface
            while atm:
                opt2 = input('''
    UKBank ATM
    ----------
    [1] Check Balance
    [2] Withdraw Cash
    [3] Deposit Cash
    [4] Exit
    > ''')
                # Balance output
                if opt2 == '1':
                    print(f'Current balance: £{balance}')
                # Withdraw cash
                if opt2 == '2':
                    withdraw = int(input('Enter the amounnt you would like to withdraw > £'))
                    while withdraw > balance:
                        withdraw = int(input(f'Insufficient funds, you only have £{balance}, try again > £'))
                    else:
                        balance -= withdraw
                        print(f'Your new balance is £{balance}, thank you for using UKBank')
                        # Update balance in account record array
                        account_record[record_number][-2] = str(balance)
                        # Update balance in account data file
                        with open(account_data, 'w') as f:
                            for account in account_record:
                                f.write(','.join(account) + '\n')
                # Deposit cash
                if opt2 == '3':
                    deposit = int(input('Enter an amount to deposit > £'))
                    balance += deposit
                    print(f'Your new balance is £{balance}, thank you for using UKBank')
                    # Update balance in account record array
                    account_record[record_number][-2] = str(balance)
                    # Update balance in account data file
                    with open(account_data, 'w') as f:
                        for account in account_record:
                            f.write(','.join(account) + '\n')
                # Exit
                if opt2 == '4':
                    atm = False
                    menu()

# Main menu 
def menu():
    menu = True
    while menu:
        opt = input('''
Welcome to UKBank:
------------------
[1] Create an account
[2] Use ATM
[3] Exit
> ''')
        if opt == '1':
            create_account()
        if opt == '2':
            ATM()
        if opt == '3':
            print('Thank you for using UKBank!')
            menu = False
            sys.exit()

menu()