from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == "__main__":
  app.run() 