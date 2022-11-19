from flask import Flask, render_template
from concurrent.futures import ThreadPoolExecutor
from scraper import getStock

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/stock")
def stock():
  stock_urls = [
      'https://tw.stock.yahoo.com/quote/2330',
      'https://tw.stock.yahoo.com/quote/2330',
      'https://tw.stock.yahoo.com/quote/2317',
      'https://tw.stock.yahoo.com/quote/6547'
  ]
  executor = ThreadPoolExecutor()
  with ThreadPoolExecutor() as executor:
    data = list(executor.map(getStock, stock_urls))
  
  
  return render_template('home.html', data = data)

if __name__ == "__main__":
  app.run(debug=True)
