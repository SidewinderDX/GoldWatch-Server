import sqlite3 as sql

chest = "treasure_chest.db"

def getData(query):
    db = sql.connect(chest)
    cursor = db.cursor()

    cursor.execute(query)


def saveData(data):
    db = sql.connect(chest)
    cursor = db.cursor()

    #cursor.execute(query)

def createDB():
    db = sql.connect(chest)
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE priceHistory (date, kruegerBuy, kruegerSell, philBuy, philSell, mapleBuy, mapleSell, kangBuy, kangSell)")
    except sql.Error as err:
        print(err)
    try:
        cursor.execute("CREATE TABLE userData (kruegAmount, philAmount, mapleAmount, kangAmount)")
    except sql.Error as err:
        print(err)
    
    db.close()

createDB()