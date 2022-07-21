from bs4 import BeautifulSoup as bs
from requests import get
from settings import HEADERS



class Help:
    def is_sale(item):
        # Returns the html of the page
        def get_soup(URL):

            request = get(URL, headers=HEADERS)
            messy_soup = bs(request.content, 'html.parser')
            soup = bs(messy_soup.prettify(), 'html.parser')
            return soup
        
        # Returns the float of the current price e.g. 39.99
        def get_price(soup):
            price = soup.find(id='apex_offerDisplay_desktop').get_text()
            return float(''.join(price.strip()[1:7].rstrip()))     

        # Compares price and sends email with discount if true
        def compare_price(price, item):
            #item[1] is the price in the item list
            original_price = item[1]
            if price < original_price:
                discount = round(100-((price/original_price)*100))
                return [item[0], price, original_price, discount, URL]

        # item[2] is url in the item list
        URL = item[2]
        soup = get_soup(URL)
        price = get_price(soup)
        return compare_price(price, item)






















