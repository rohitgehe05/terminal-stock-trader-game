import sqlite3
from IPython import embed

conn = sqlite3.connect('stock_trader.sqlite')
cur = conn.cursor()


# User action logic


def add_user(username, password, name, balance):
    cur.execute("INSERT INTO Users(username, password, name, balance) VALUES(?,?,?,?);",
                (username, password, name, balance))
    conn.commit()


def login(username):
    user = cur.execute(
        "SELECT password FROM Users WHERE username = (?);", (username, ))
    pw = cur.fetchone()
    return pw


def get_user_id(username):
    user_id = cur.execute(
        "SELECT id FROM Users WHERE username = (?);", (username,))
    user_id = cur.fetchone()[0]
    return user_id


def check_user(username):
    cur.execute("SELECT id FROM users WHERE username = (?);", (username,))
    account = cur.fetchone()
    return account


def get_balance(user_id):
    balance = cur.execute(
        "SELECT balance FROM Users WHERE id = (?);", (user_id,))
    balance = cur.fetchone()[0]
    return balance


def get_stock_qty(user_id, symbol):
    stock_qty = cur.execute(
        "SELECT quantity FROM Stocks WHERE user_id = (?) and symbol = (?);", (user_id, symbol))
    stock_qty = cur.fetchone()
    if stock_qty is not None:
        return stock_qty[0]
    else:
        return None


def get_portfolio(user_id):
    cur.execute("SELECT * FROM Stocks WHERE user_id = (?);", (user_id,))
    result = cur.fetchall()
    return result


# User trading logic


def buy_stock(user_id, symbol, last_price, total_price, qty):
    txn_type = "BUY"
    cur.execute(
        "SELECT * FROM Stocks WHERE user_id = (?) AND symbol = (?);", (user_id, symbol))
    existing = cur.fetchone()
    if existing is None:
        cur.execute("INSERT INTO Stocks(user_id, symbol, price, quantity) VALUES(?,?,?,?);",
                    (user_id, symbol, last_price, qty))
    else:
        cur.execute(
            "UPDATE Stocks SET quantity = quantity + (?) WHERE user_id = (?) AND symbol = (?);", (qty, user_id, symbol))
        cur.execute(
            "UPDATE Stocks SET price = price + (?) / quantity WHERE user_id = (?) AND symbol = (?);", (last_price, user_id, symbol))
    cur.execute(
        "UPDATE Users SET balance = balance - (?) WHERE id = (?);", (total_price, user_id))
    conn.commit()
    cur.execute(
        "UPDATE Stocks SET total_value = price * quantity WHERE symbol = (?) AND user_id = (?);", (symbol, user_id))
    cur.execute("INSERT INTO History(user_id, symbol, price, order_value, quantity, transaction_type) VALUES(?,?,?,?,?,?);",
                (user_id, symbol, last_price, total_price, qty, txn_type))
    conn.commit()

# buy_stock(1, 'AAPL', 100, 1000, 10)


def sell_stock(user_id, symbol, last_price, total_price, qty):
    txn_type = "SELL"
    cur.execute("UPDATE Stocks SET quantity = quantity - (?) WHERE user_id = (?) AND symbol = (?);",
                (qty, user_id, symbol))
    cur.execute("UPDATE Users SET balance = balance + (?) WHERE id = (?);",
                (total_price, user_id))
    conn.commit()
    cur.execute(
        "UPDATE Stocks SET total_value = price * quantity WHERE symbol = (?) AND user_id = (?);", (symbol, user_id))
    cur.execute("INSERT INTO History(user_id, symbol, price, order_value, quantity, transaction_type) VALUES(?,?,?,?,?,?);",
                (user_id, symbol, last_price, total_price, qty, txn_type))
    conn.commit()


def get_trade_history(user_id):
    cur.execute("SELECT * FROM History WHERE user_id = (?);", (user_id,))
    result = cur.fetchall()
    return result


def view_leaderboard():
    cur.execute("SELECT user_id, name, username, SUM(total_value) FROM Users INNER JOIN Stocks ON Stocks.user_id = Users.id GROUP BY user_id ORDER BY total_value;")
    result = cur.fetchall()
    return result
