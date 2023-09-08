import sqlite3

def init_db():
    #setup connection and cursor
    con =sqlite3.connect("portfolio.db")
    cur = con.cursor()
    #make tables
    cur.execute("CREATE TABLE IF NOT EXISTS portfolio(ticker, exchange, shares)")
    #Commit Them Changes
    con.commit()
    print("DB HAS BEEN CREATED")