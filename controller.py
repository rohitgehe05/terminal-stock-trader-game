import model
from wrapper import Lookup
from IPython import embed


def login(username):
    validator = model.login(username)
    if validator == None:
        return 0
    elif validator is not None:
        return validator[0]


def create_account(username, password, name):
    if model.check_user(username) == None:
        model.add_user(username, password, name, 100000)
        return 1
    else:
        return 0


def get_portfolio(username):
    user_id = model.get_user_id(username)
    portfolio = model.get_portfolio(user_id)
    if portfolio == None:
        return 0
    else:
        return portfolio


def company_search(company):
    search = Lookup()
    data = search.company_search(company)
    if data is not None:
        return data
    else:
        return 0


def get_quote(symbol):
    quote = Lookup()
    data = quote.get_quote(symbol)
    if data is not None:
        return data
    else:
        return False


def get_details(symbol):
    details = Lookup()
    data = details.get_details(symbol)
    if data is not None:
        return data
    else:
        return False


def buy_stock(symbol, qty, username):
    user_id = model.get_user_id(username)
    last_price = get_quote(symbol)
    if last_price == False:
        response = 500
        return (0, 0, 0, response)
    else:
        total_price = qty * last_price
    if model.get_balance(user_id) < total_price:
        response = 400
        return (0, 0, 0, response)
    else:
        response = 200
        model.buy_stock(user_id, symbol, last_price, total_price, qty)
        return last_price, total_price, model.get_balance(user_id), response


def sell_stock(symbol, qty, username):
    user_id = model.get_user_id(username)
    last_price = get_quote(symbol)
    if last_price == False:
        response = 500
        return (0, 0, 0, response)
    else:
        total_price = qty * last_price
    if model.get_stock_qty(user_id, symbol) == None:
        response = 401
        return (0, 0, 0, response)
    elif model.get_stock_qty(user_id, symbol) < qty:
        response = 400
        return (0, 0, 0, response)
    else:
        response = 200
        model.sell_stock(user_id, symbol, last_price, total_price, qty)
        return last_price, total_price, model.get_balance(user_id), response


def get_trade_history(username):
    user_id = model.get_user_id(username)
    history = model.get_trade_history(user_id)
    if history == None:
        return 0
    else:
        return history
