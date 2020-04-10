import sqlite3


conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

stocks = [
    ('WDSS', 10, 34.5),
    ('SERG', 45, 72.12),
    ('ASET', 123, 743.23)
]

for symbol, quantity, price in stocks:
    c.execute("INSERT INTO stocks VALUES ('2010-01-05','BUY', ?, ?, ?)", (symbol, quantity, price))

c.execute('SELECT * FROM stocks')

print(c.fetchall())

conn.commit()
conn.close()
