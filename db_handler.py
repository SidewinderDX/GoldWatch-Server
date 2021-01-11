import mysql.connector as sql
from mysql.connector import errorcode

user = "GoldWatch"
pw = "GW-Project"
host = "127.0.0.1"
database = "GW"

def getData(coinType):
    db = sql.connect(user=user, password=pw, host=host, database=database)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM `priceHistory{coinType}`")
    ret = cursor.fetchall()
    
    return ret

def saveData(date, buy, sell, coinType):
    db = sql.connect(user=user, password=pw, host=host, database=database)
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO `priceHistory{coinType}` (date, Buy, Sell) VALUES ({date},{buy},{sell}) ON DUPLICATE KEY UPDATE date=date")
    db.commit()
    cursor.close()
    db.close()

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE GW DEFAULT CHARACTER SET 'utf8'")
    except sql.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

# Only runs if db_handler runs on it own
# Trys to create the database if not found
# creates all needed tables
if __name__ == "__main__":
    db = sql.connect(user=user, password=pw, host=host)
    cursor = db.cursor()

    try:
        cursor.execute("USE GW")
    except sql.Error as err:
        print("No GW Database found!")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Succesfully created database!")
        else:
            print(err)
            exit(1)
    
    db.database = "GW"

    tableK = "CREATE TABLE `priceHistoryKrueger` (date INT, Buy FLOAT, Sell FLOAT, PRIMARY KEY (`date`)) ENGINE=InnoDB;"
    tableP = "CREATE TABLE `priceHistoryPhil` (date INT, Buy FLOAT, Sell FLOAT, PRIMARY KEY (`date`)) ENGINE=InnoDB;"
    tableM = "CREATE TABLE `priceHistoryMaple` (date INT, Buy FLOAT, Sell FLOAT, PRIMARY KEY (`date`)) ENGINE=InnoDB;"
    tableKa = "CREATE TABLE `priceHistoryKang` (date INT, Buy FLOAT, Sell FLOAT, PRIMARY KEY (`date`)) ENGINE=InnoDB;"

    querry = tableK + tableP + tableM + tableKa
    cursor.execute(querry, multi=True)

    db.commit()
    cursor.close()
    db.close()
