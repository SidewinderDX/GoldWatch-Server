from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError

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
    return update[7:len(update)-4]  
    
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

def getHTML(url):
    session = requests.Session()

    try:
        response = session.get(url)

    except HTTPError as http_err:
        print('')
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print('')
        print(f'Other error occured: {err}')
    else:
        soup = BeautifulSoup(response.text, features="html.parser")
    
    return soup