def get_codes_from_db():
    import sqlite3
    #pull all of the raw data from the database
    con =sqlite3.connect("portfolio.db")
    cur = con.cursor()
    ticker =cur.execute("SELECT ticker FROM portfolio")
    ticker= ticker.fetchall()
    exchange = cur.execute("SELECT exchange FROM portfolio")
    exchange = exchange.fetchall()
    
    codes = []
    #Make codes list
    for x in range(len(exchange)):
        codes.append(f"{exchange[x][0].split()[0]}:{ticker[x][0].split()[0]}")
    return codes
