import sqlite3 as sql

def getData(query):
    db = sql.connect('data_safe.db')
    cursor = db.cursor()

    cursor.execute(query)


def saveData(data):
    db = sql.connect('data_safe.db')
    cursor = db.cursor()

    #cursor.execute(query)

def createDB():
    db = sql.connect('data_safe.db')
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