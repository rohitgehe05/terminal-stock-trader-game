import sqlite3

conn = sqlite3.connect('stock_trader.sqlite')
cur = conn.cursor()

# User action logic


def add_user(username, password, name, balance):
    cur.execute("INSERT INTO Users(username, password, name, balance) VALUES(?,?,?,?);",
                (username, password, name, balance))
    conn.commit()


def login(username, password):
    user = cur.execute(
        "SELECT id FROM Users WHERE username=(?) and password=(?);", (username, password))
    user = cur.fetchone()
    return user


def get_user_id(username):
    user_id = cur.execute(
        "SELECT id FROM Users WHERE username=(?);", (username,))
    user_id = cur.fetchone()[0]
    return user_id


def check_user(username):
    cur.execute("SELECT id FROM users WHERE username=(?);", (username,))
    account = cur.fetchone()
    return account


def get_balance(user_id):
    balance = cur.execute(
        "SELECT balance FROM Users WHERE id=(?);", (user_id,))
    balance = cur.fetchone()[0]
    return balance


def get_stock_qty(user_id, symbol):
    stock_qty = cur.execute(
        "SELECT quantity FROM Stocks WHERE user_id=(?) and symbol=(?);", (user_id, symbol))
    stock_qty = cur.fetchone()[0]
    return stock_qty


# User trading logic


def buy_stock(user_id, symbol, last_price, total_price, qty):
    cur.execute(
        "SELECT * FROM Stocks WHERE user_id=(?) AND symbol=(?);", (user_id, symbol))
    existing = cur.fetchone()
    if existing is None:
        cur.execute("INSERT INTO Stocks(user_id, symbol, price, quantity) VALUES(?,?,?,?);",
                    (user_id, symbol, last_price, qty))
    else:
        cur.execute(
            "UPDATE Stocks SET quantity=quantity+(?) WHERE user_id=(?) AND symbol=(?);", (qty, user_id, symbol))
    cur.execute(
        "UPDATE Users SET balance=balance-(?) WHERE id=(?);", (total_price, user_id))
    conn.commit()


def sell_stock(user_id, symbol, last_price, total_price, qty):
    cur.execute("UPDATE Stocks SET quantity=quantity-(?) WHERE user_id=(?) AND symbol=(?);", (qty, user_id, symbol))
    cur.execute("UPDATE Users SET balance=balance+(?) WHERE id=(?);", (total_price, user_id))
    conn.commit()
