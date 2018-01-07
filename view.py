import controller
from wrapper import Lookup
from colorama import init, Fore, Style
from prettytable import PrettyTable
from IPython import embed
import os
import getpass


init(autoreset=True)
os.system("clear")
print(Fore.YELLOW + Style.BRIGHT +
      'Welcome to the Stock Trader Platform!')
print(Fore.YELLOW + Style.BRIGHT + '-' * 30)


def main_menu():
    init(autoreset=True)
    user_input = 0
    while user_input != 3:
        user_input = input(Fore.RED + '''\nWhat would you like to do?\n
        1. Login
        2. Create a new account
        3. Quit app\n
        >> ''')
        try:
            user_input = int(user_input)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')
        if isinstance(user_input, int) == True:
            if user_input == 1:
                username = str(input('\nPlease enter your username: '))
                password = str(getpass.getpass('Please enter your password: '))
                if controller.login(username, password) == 1:
                    print(Fore.GREEN +
                          Style.BRIGHT + '\nLogin successful!')
                    login_menu(username)
                else:
                    print(Fore.RED +
                          Style.BRIGHT + '\nINVALID LOGIN!')
            elif user_input == 2:
                username = str(input('\nPlease enter your username: '))
                password = str(input('Please enter your password: '))
                name = str(input('Pleas enter your full name: '))
                if controller.create_account(username, password, name) == 1:
                    print(Fore.GREEN + Style.BRIGHT +
                          '\nAccount creation successful!\n')
                else:
                    print(Fore.RED + Style.BRIGHT +
                          '\nAccount creation failed\n')
            elif user_input == 3:
                print(Fore.CYAN + Style.BRIGHT +
                      'Thank you for checking this game out! Goodbye :)')
                break
            elif user_input > 3:
                print(Fore.RED + Style.BRIGHT +
                      '\nINVALID OPTION, TRY AGAIN!\n')


def login_menu(username):
    init(autoreset=True)
    user_input = 0
    while user_input != 5:
        user_input = input(Fore.BLUE + '''\nChoose an option:\n
        1. See my portfolio
        2. Stock search
        3. Buy stocks
        4. Sell stocks
        5. Logout\n
        >> ''')
        try:
            user_input = int(user_input)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')
        if user_input == 1:
            # check portfolio
            pass
        elif user_input == 2:
            company = str(
                input("\nEnter the name of the company you want to search for: "))
            stock_search(company)
            pass
        elif user_input == 3:
            buy_stock(username)
        elif user_input == 4:
            sell_stock(username)
        elif user_input == 5:
            break
        else:
            print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')


def view_portfolio():
    pass


def stock_search(company):
    # var initiation
    t = PrettyTable()
    # print table
    if controller.company_search(company) != 0:
        t.field_names = controller.company_search(company).keys()
        t.add_row(controller.company_search(company).values())
        print('\n', t)
    else:
        print(Fore.RED + Style.BRIGHT +
              '\nWhoops! We could not find the company named "' + company + '"')


def buy_stock(username):
    # var initiation
    t = PrettyTable()
    print()
    symbol = str(input("Enter the ticker symbol for the company: ")).upper()
    qty = int(input("Enter the quantity to buy: "))
    # print table
    t.field_names = controller.get_details(symbol).keys()
    t.add_row(controller.get_details(symbol).values())
    print('\n' + t.get_string(fields=["Name", "Symbol", "LastPrice", "Change",
                                      "ChangePercent", "ChangeYTD", "ChangePercentYTD", "Volume"]) + '\n')
    print('Your total purchase value is ${0:.2f}'.format(
        controller.get_quote(symbol) * qty))
    confirmation = str(input(
        'Are you sure you want to go ahead with this transaction? (Y/N) '))
    # validate confirmation and do actual buying of stock
    if confirmation != 'Y' and confirmation != 'y':
        print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')
    else:
        last_price, total_price, balance, response = controller.buy_stock(
            symbol, qty, username)
        if response == 400:
            print(
                'You have insufficient funds to proceed with this transaction! Please try again.')
        elif response == 500:
            print('There is a connectivity issue! Please try again.')
        elif response == 200:
            print('-' * 30)
            print('You have successfully purchased {} shares of {} at ${} per share.'.format(
                qty, symbol, last_price))
            print('For a total of ${0:.2f}'.format(total_price))
            print('Your balance is now ${0:.2f}.'.format(balance))


def sell_stock(username):
    # var initiation
    t = PrettyTable()
    symbol = str(input("Enter the ticker symbol for the company: ")).upper()
    qty = int(input("Enter the quantity to sell: "))
    # print table
    t.field_names = controller.get_details(symbol).keys()
    t.add_row(controller.get_details(symbol).values())
    print('\n' + t.get_string(fields=["Name", "Symbol", "LastPrice", "Change",
                                      "ChangePercent", "ChangeYTD", "ChangePercentYTD", "Volume"]) + '\n')
    print('Your total purchase value is ${0:.2f}'.format(
        controller.get_quote(symbol) * qty))
    confirmation = str(input(
        'Are you sure you want to go ahead with this transaction? (Y/N) '))
    # validate confirmation and do actual buying of stock
    if confirmation != 'Y' and confirmation != 'y':
        print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')
    else:
        last_price, total_price, balance, response = controller.sell_stock(
            symbol, qty, username)
        if response == 400:
            print(
                'The quantity entered exceeds the quantity held in the portfolio! Please try again.')
        elif response == 401:
            print('Your portfolio does not have this stock! Please try again.')
        elif response == 500:
            print("There is a connectivity issue! Please try again.")
        elif response == 200:
            print('-' * 30)
            print('You have successfully sold {} shares of {} at ${} per share.'.format(
                qty, symbol, last_price))
            print('For a total of ${0:.2f}'.format(total_price))
            print('Your balance is now ${0:.2f}.'.format(balance))
