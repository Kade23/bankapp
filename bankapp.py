import random
import os

user_input = input("Would you Like to Log In or Close App?: ")
print("Please Log in")

while user_input == "Log in" :
    username = str(input("Enter your Username: "))
    userpassword = str(input("Enter your Password: "))
    file = open("staff.txt", "r")
    for row in file:
        field = row.split(",")
        username1 = (field[0])
        password1 = (field[1])

    if username == username1 and userpassword == password1:
        print ("Log In Successful")
    else:
        print("Wrong details. Please try again")
        file.close()

session= open("session.txt","w+")
print('Please choose an option' '\n1. Create a New Bank Account' '\n2. Check Account Details' '\n3. Logout')
option = int(input('>: '))
if option == 1:
    account_name = str(input('Account Name : ')).lower()
    opening_balance = float(input('Opening Balance: '))
    account_type = str(input('Account Type: ')).lower()
    account_email = input('Account email : ')

    account_number = ''.join(map(str, [random.randint(1, 9) for a in range(0, 10)]))

    customer_details = open('customer.txt', 'w+')
    customer_details.write('Account Name: %s\n' %account_name)
    customer_details.write('Opening Balance: %s\n' %opening_balance)
    customer_details.write('Account Type: %s\n' %account_type)
    customer_details.write('Account Email: %s\n' %account_email)
    customer_details.close()

    print(f'Your Account number is {account_number}')
    print('Please choose an option' '\n1. Create a New Bank Account' '\n2. Check Account Details' '\n3. Logout')


def check_account_deets():
    acc_deets_loop = True
    customer_acc_detail = []
    acc_number = input('Enter Your Account Number: ')
    while acc_deets_loop is True:
        if acc_number == account_number:
            with open('customer.txt', 'r') as customer_details:
                for customer in customer_details:
                    customer = customer.split('\n')
                    print(customer)
            acc_deets_loop = False
        else:
            print('Wrong Account Number, Please input a Valid Account Number')
            check_account_deets()

