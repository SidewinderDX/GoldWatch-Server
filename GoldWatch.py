import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import re
import time
from storage import Storage

def getOneOunceGold(soup):
    oneGgoldPrice = soup.find(string='Gold 1 Unze')
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    buy = oneGgoldPrice.next_element        # Ankauf
    oneGgoldPrice = buy.next_element   
    oneGgoldPrice = oneGgoldPrice.next_element
    sell = oneGgoldPrice.next_element            
    oneGgoldPrice = buy.next_element        # Verkauf
    return float(buy.text[0:len(buy.text)-3])*1e3, float(sell.text[0:len(buy.text)-3])*1e3

def getOneCoin(coin, soup):
    oneGgoldPrice = soup.find(string=coin)
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element
    oneGgoldPrice = oneGgoldPrice.next_element  
    buy = oneGgoldPrice.next_element            # Ankauf
    oneGgoldPrice = buy.next_element            
    oneGgoldPrice = oneGgoldPrice.next_element  
    sell = oneGgoldPrice.next_element           # Verkauf     

    return float(buy.text[0:len(buy.text)-3])*1e3, float(sell.text[0:len(buy.text)-3])*1e3

def lastUpdate(soup):
    update = soup.find("div", class_="exchange-rates-table--change-date")
    update = update.next_element
    return update

def evaluateInput(user_input, treasure):
    if user_input == 0:
        treasure.saveStorage()
        pass
    elif user_input == 1:
        user_input = int(input("|Anzahl der neuen Muenzen: "))
        treasure.mapleLeafAmount += user_input

    elif user_input == 2:
        user_input = int(input("|Anzahl der neuen Muenzen: "))
        treasure.philharmonikerAmount += user_input

    elif user_input == 3:
        user_input = int(input("|Wie viele Muenzen entnehmen: "))
        while treasure.mapleLeafAmount - user_input < 0:
            print("|Arr, leider besitzt du nicht so viele Muenzen du Sueßwassermatrose!")
            user_input = int(input("|Wie viele Muenzen entnehmen: "))
        treasure.mapleLeafAmount -= user_input
        
    elif user_input == 4:
        user_input = int(input("|Wie viele Muenzen entnehmen: "))
        while treasure.philharmonikerAmount - user_input < 0:
            print("|Arr, leider besitzt du nicht so viele Muenzen du Sueßwassermatrose!")
            user_input = int(input("|Wie viele Muenzen entnehmen: "))
        treasure.philharmonikerAmount-= user_input 
    elif user_input == 5:
        treasure.saveStorage()


# db_handler.createDB()
exchange = 'https://www.exchange-ag.de/aktuelle-goldkurse'
session = requests.Session()

try:
    response = session.get(exchange)

except HTTPError as http_err:
    print('')
    print(f'HTTP error occured: {http_err}')
except Exception as err:
    print('')
    print(f'Other error occured: {err}')
else:
    print('')
    

    soup = BeautifulSoup(response.text, features="html.parser")

    user_input = -1
    treasure = Storage()
    while user_input != 0:
        # Interface
        borderline_row = "+--------------------------------------------------------------------------------------------------+"
                        
        updateLine = ' ' * (98 - len(lastUpdate(soup)))
        oneMapleLeafBuy, oneMapleLeafSell = getOneCoin('Maple Leaf', soup)
        onePhilharmonikerBuy, onePhilharmonikerSell = getOneCoin('Philharmoniker', soup)
        
        mapleLen = str(treasure.mapleLeafAmount)
        mapleAmountLine = ' ' * (48 - len(mapleLen) - 13)
        mapleLen = str(oneMapleLeafBuy)
        mapleBuyLine = ' ' * (22 - len(mapleLen))
        mapleLen = str(oneMapleLeafSell)
        mapleSellLine = ' ' * (22 - len(mapleLen))

        philLen = str(treasure.philharmonikerAmount)
        philAmountLine = ' ' * (48 - len(philLen) - 16)
        philLen = str(onePhilharmonikerBuy)
        philBuyLine = ' ' * (22 - len(philLen))
        philLen = str(onePhilharmonikerSell)
        philSellLine = ' ' * (22 - len(philLen))

        mapleLen = str(treasure.mapleLeafAmount)
        mapleLenMoney = str(float(treasure.mapleLeafAmount) * oneMapleLeafBuy)
        mapleMoneyLine = ' ' * (98 - len(mapleLen) - len(mapleLenMoney) - 14) 

        philLen = str(treasure.philharmonikerAmount)
        philLenMoney = str(float(treasure.philharmonikerAmount) * onePhilharmonikerBuy)
        philMoneyLine = ' ' * (98 - len(philLen) - len(philLenMoney) - 17) 

        print(borderline_row)
        print(f"|{lastUpdate(soup)}{updateLine}|")
        print(borderline_row)
        print("|Besitz                                          ||Ankauf x 1             ||Verkauf x 1            |")
        print("+------------------------------------------------||-----------------------||-----------------------+")
        print(f"|Maple Leafs: {treasure.mapleLeafAmount}{mapleAmountLine}||{oneMapleLeafBuy}€{mapleBuyLine}||{oneMapleLeafSell}€{mapleSellLine}|") 
        print(f"|Philharmoniker: {treasure.philharmonikerAmount}{philAmountLine}||{onePhilharmonikerBuy}€{philBuyLine}||{onePhilharmonikerSell}€{philSellLine}|") 
        print(borderline_row)
        print(f"|Aktueller Wert                                                                                    |")
        print(borderline_row)
        print(f"|{treasure.mapleLeafAmount} Maple Leafs: {treasure.mapleLeafAmount * oneMapleLeafBuy}{mapleMoneyLine}|")
        print(f"|{treasure.philharmonikerAmount} Philharmoniker: {treasure.philharmonikerAmount * onePhilharmonikerBuy}{philMoneyLine}|")
        print(borderline_row)
        print("|Menue                                                                                             |")
        print(borderline_row)
        print("| 1. Maple Leaf in die Truhe werfen                                                                |")
        print("| 2. Philharmoniker in die Truhe werfen                                                            |")
        print("| 3. Maple Leaf aus der Truhe entfernen                                                            |")
        print("| 4. Philharmoniker aus der Truhe entfernen                                                        |")
        print("| 5. Matrosen abstellen um die Truhe zu bewachen (speichern)                                       |")
        print("| 0. Truhe schließen und vergraben                                                                 |")
        print(borderline_row)
        print("|Gib die Zahl der gewuenschten Option ein und bestaetige mit Enter                                 |")
        user_input = int(input("|Auswahl: "))

        evaluateInput(user_input, treasure)
