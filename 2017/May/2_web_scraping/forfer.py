"""
Scrap data from website and export to csv
Not trully automated, it would be necessary to manually run it, or automate it,
but I do not have a machine capable of running a script 24/7, and as this
challege is purely based on webscrapping, I didn't see the need to deepen more
into making the script 24/7

by ForFer
"""

from bs4 import BeautifulSoup
import csv 
import requests
import requests_cache # For debugging, not necessary
from time import time

# Uncomment if you want to debug or try things. it's nice to cache the website 
# for some time in order to not get "too many calls" error. 
#requests_cache.install_cache('bitcoins', expire_after=3600)
page = requests.get("https://bitcoinwisdom.com/")
soup = BeautifulSoup(page.content, 'html.parser')

btc = list(soup.find(id="o_btceur").find(class_="r").children)[0]
ltc = list(soup.find(id="o_ltceur").find(class_="r").children)[0]

res = [btc, ltc, time()]

with open("bitcoin_rates.csv", 'a+') as f:
    wr = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    wr.writerow(res)
