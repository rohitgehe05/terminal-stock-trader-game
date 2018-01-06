import controller
from wrapper import Lookup
from colorama import init, Fore, Style
import os

init(autoreset=True)
os.system("clear")
print(Fore.YELLOW + Style.BRIGHT +
      'Welcome to the Stock Trader Platform!')
print(Fore.YELLOW + Style.BRIGHT + '-' * 30)


def main_menu():
    init(autoreset=True)
    user_input = 0
    while user_input != 3:
        user_input = input(Fore.RED + '''What would you like to do?\n
        1. Login
        2. Create a new account
        3. Quit app\n
        >> ''')
        try:
            user_input = int(user_input)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')
        if user_input == 1:
            username = str(input('\nPlease enter your username: '))
            password = str(input('Please enter your password: '))
            if controller.login(username, password) == 1:
                print(Fore.GREEN +
                      Style.BRIGHT + '\nLogin successful!')
                login_menu(username)
            else:
                print(Fore.RED +
                      Style.BRIGHT + '\nInvalid login!')
        elif user_input == 2:
            username = str(input('\nPlease enter your username: '))
            password = str(input('Please enter your password: '))
            name = str(input('Pleas enter your full name: '))
            if controller.create_account(username, password, name) == 1:
                print(Fore.GREEN + Style.BRIGHT +
                      '\nAccount creation successful!\n')
            else:
                print(Fore.RED + Style.BRIGHT + '\nAccount creation failed\n')
        elif user_input == 3:
            print(Fore.CYAN + Style.BRIGHT +
                  'Thank you for checking this game out! Goodbye :)')
            break
        else:
            print(Fore.RED + Style.BRIGHT + '\nINVALID OPTION, TRY AGAIN!\n')


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
            # go to stock search menu
            pass
        elif user_input == 3:
            buy_stock(username)
        elif user_input == 4:
            sell_stock(username)
        elif user_input == 5:
            break
        else:
            print(Fore.RED + Style.BRIGHT +
                  '\nINVALID OPTION, TRY AGAIN!\n')


def view_portfolio():
    pass


def stock_search():
    pass


def buy_stock(username):
    symbol = str(input("Enter the ticker symbol for the company: ")).upper()
    qty = int(input("Enter the quantity to buy: "))
    last_price, total_price, balance, response = controller.buy_stock(
        symbol, qty, username)
    if response == 400:
        print('You have insufficient funds to proceed with this transaction! Please try again.')
    elif response == 500:
        print('There is a connectivity issue! Please try again.')
    elif response == 200:
        print('-' * 30)
        print('You have successfully purchased {} shares of {} at ${} per share.'.format(
            qty, symbol, last_price))
        print('For a total of ${}'.format(total_price))
        print('Your balance is now ${}.'.format(balance))


def sell_stock(username):
    symbol = str(input("Enter the ticker symbol for the company: ")).upper()
    qty = int(input("Enter the quantity to sell: "))
    last_price, total_price, balance, response = controller.sell_stock(
        symbol, qty, username)
    if response == 400:
        print('The quantity entered exceeds the quantity held in the portfolio! Please try again.')
    elif response == 401:
        print('Your portfolio does not have this stock! Please try again.')
    elif response == 500:
        print("There is a connectivity issue! Please try again.")
    elif response == 200:
        print('-' * 30)
        print('You have successfully sold {} shares of {} at ${} per share.'.format(
            qty, symbol, last_price))
        print('For a total of ${}'.format(total_price))
        print('Your balance is now ${}.'.format(balance))

main_menu()
