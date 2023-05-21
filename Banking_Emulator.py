import random
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
    card_number = [random.randint(0,9) for i in range(16)]
    sort_code = [random.randint(0,9) for i in range(6)]
    account_number = [random.randint(0,9) for i in range(8)]
    print(f'Here is your new {card_type}')
    print(f'''
-------------------------------------------------
                    {bank_name}
{card_number}
{validation_date} {expiry_date}
{user_name}
{sort_code} {account_number}
{card_type}
-------------------------------------------------''')
    
print('Welcome to UKBank')
create_account()