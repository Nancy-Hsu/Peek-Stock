from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import requests
stock_urls = [
    'https://tw.stock.yahoo.com/quote/2330',
    'https://tw.stock.yahoo.com/quote/0050',
    'https://tw.stock.yahoo.com/quote/2317',
    'https://tw.stock.yahoo.com/quote/6547'
]
def getStock(url):
  web = requests.get(url)
  soup = BeautifulSoup(web.text, 'html.parser')
  company = soup.select('h1')[1].get_text()
  quote = soup.find('span', {'class': 'Fz(32px)'}).get_text()
  difference = soup.find('span', {'class': 'Fz(20px)'}).get_text()
  isUpOrDown = ''
  try:
    if quote.select('.C($c-trend-down)')[0]:
        s = '-'
  except:
    try:
        if quote.select('.C($c-trend-up)')[0]:
            s = '+'
    except:
        s = '-'

    return (f'{ company } : { quote } ( { isUpOrDown }{ difference } )')
  






