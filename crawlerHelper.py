from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


def getStock(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    error = None
    if web.status_code == 404:
        error = url + "/Error"
        return error
    company = soup.select('h1')[1].get_text()
    quote = soup.find('span', {'class': 'Fz(32px)'}).get_text()
    difference = soup.find('span', {'class': 'Fz(20px)'}).get_text()
    isUpOrDown = ''
    try:
        if quote.select('.C($c-trend-down)')[0]:
            isUpOrDown = '-'
    except:
        try:
            if quote.select('.C($c-trend-up)')[0]:
                isUpOrDown = '+'
        except:
            isUpOrDown = '-'

        return (f'{ company } : { quote } ( { isUpOrDown }{ difference } )')


def get_error(url):
    error = ""
    if "Error" in url:
        return url.split('/')[4]
    


def map_together(func, lst):
    data = []
    executor = ThreadPoolExecutor()
    with ThreadPoolExecutor() as executor:
        data = list(executor.map(func, lst))
        # data = list(filter(None, list(executor.map(func, lst))))
        # data = executor.map(func, lst)
    #data = [i for i in data if i != None]
    return data


def get_url(codes):
    url = 'https://tw.stock.yahoo.com/quote/'
    return f'{url}{codes}'


def get_value_from_request(request):
    lst = []
    for idx in request:
        stock_code = request.getlist(idx)[0]
        if stock_code != "":
            lst.append(f'{stock_code}')
    return lst
