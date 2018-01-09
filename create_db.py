import sqlite3


conn = sqlite3.connect('stock_trader.sqlite')
cur = conn.cursor()


def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS 'Users' (
    'id' INTEGER,
    'username' VARCHAR,
    'password' VARCHAR,
    'name' VARCHAR,
    'balance' REAL,
    -- 'permission_level' INTEGER,
    PRIMARY KEY ('id')
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS 'Stocks' (
    'id' INTEGER,
    'user_id' INTEGER,
    'symbol' VARCHAR,
    'price' REAL,
    'quantity' REAL,
    'total_value' REAL,
    FOREIGN KEY ('user_id') REFERENCES Users(id),
    PRIMARY KEY ('id')
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS 'History' (
    'id' INTEGER,
    'timestamp' VARCHAR,
    'user_id' INTEGER,
    'symbol' VARCHAR,
    'price' REAL,
    'order_value' REAL,
    'quantity' REAL,
    'transaction_type' VARCHAR,
    FOREIGN KEY ('user_id') REFERENCES Users(id),
    PRIMARY KEY ('id')
    )""")

    conn.commit()
