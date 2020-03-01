import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import re
import time
import db_handler

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


db_handler.createDB()
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


    oneOunceBuy, oneOunceSell = getOneOunceGold(soup)
    oneMapleLeafBuy, oneMapleLeafSell = getOneCoin('Maple Leaf', soup)
    onePhilharmonikerBuy, onePhilharmonikerSell = getOneCoin('Philharmoniker', soup)
    ounzesAmount = input("Anzahl deiner Goldunzen: ")
    maplesAmount = input("Anzahl deiner Maple Leafs: ")
    philharmonikerAmount = input("Anzahl deiner Philharmoniker: ")

    ounzesValue = int(ounzesAmount) * oneOunceBuy
    mapleValue = int(maplesAmount) * oneMapleLeafBuy
    print("Exchange ", lastUpdate(soup))
    print("Goldunzen")
    print(f"Ankauf: {oneOunceBuy}, Verkauf {oneOunceSell}\n")
    print("Maple Leaf")
    print(f"Ankauf: {oneMapleLeafBuy}, Verkauf {oneMapleLeafSell}\n")
    print("Potentieller Gegenwert Unzen:", ounzesValue)
    print("Potentieller Gegenwert Maple Leafs:", mapleValue)
    print("Potentieller Gegenwert Gesamt:", ounzesValue + mapleValue)

    user_input = input("Auswahl: ")
    while user_input != "quit" or user_input != "exit":
        print(user_input)
        user_input = input("Auswahl: ")

