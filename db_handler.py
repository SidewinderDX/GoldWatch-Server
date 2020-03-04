import sqlite3 as sql

chest = 'treasure_chest.db'

def getData(query):
    db = sql.connect(chest)
    cursor = db.cursor()

    cursor.execute(query)
    ret = cursor.fetchall()
    db.close()
    return ret

def saveData(data):
    try:
        db = sql.connect(chest)
    except Exception as err:
        print(err)
    else:
        cursor = db.cursor()
        # print("saving")
        cursor.execute(data)
        db.commit()
        # cursor.
        db.close()

def createDB():
    db = sql.connect(chest)
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE priceHistory (date, kruegerBuy, kruegerSell, philBuy, philSell, mapleBuy, mapleSell, kangBuy, kangSell)")
    except sql.Error as err:
        pass
    try:
        cursor.execute("CREATE TABLE userData (entryID INTEGER PRIMARY KEY, kruegAmount INTEGER, philAmount INTEGER, mapleAmount INTEGER, kangAmount INTEGER)")
    except sql.Error as err:
        pass
    
    db.close()

# createDB()