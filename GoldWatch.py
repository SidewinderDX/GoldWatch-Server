import time
import base_functions as bf
import db_handler as db

if __name__ == "__main__":
    exchange = 'https://www.exchange-ag.de/aktuelle-goldkurse'

    starttime = time.time()
    starttime = starttime - starttime % 3600.0

    while True:
        soup = bf.getHTML(exchange)
        lastUpdate = int(time.mktime(time.strptime(bf.lastUpdate(soup), "%d.%m.%Y, %H:%M")))
        print(lastUpdate)

        mapleB, mapleS = bf.getOneCoin('Maple Leaf', soup)
        philB, philS = bf.getOneCoin('Philharmoniker', soup)
        kangB, kangS = bf.getOneCoin('Kangaroo', soup)
        kruegB, kruegS = bf.getOneCoin('Krügerrand', soup)

        db.saveData(lastUpdate, mapleB, mapleS, "Maple")
        db.saveData(lastUpdate, philB, philS, "Phil")
        db.saveData(lastUpdate, kangB, kangS, "Kang")
        db.saveData(lastUpdate, kruegB, kruegS, "Krueger")
        #Sleep timer which "restarts" the script every Hour after starting to acquire new data
        time.sleep(3600 - ((time.time() - starttime) % 3600))