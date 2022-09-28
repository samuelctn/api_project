
import requests
import json
import csv
import apikey
import time
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'3',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey.key,
}



def api_pull_coinbase():

    File = open("title.txt", "a+" , encoding='utf8')
    csv_writer = csv.writer(File)
    json = requests.get(url, params= parameters, headers = headers).json()


    coins = json['data']
    for x in coins:
        # if x['symbol'] == 'BTC' or x['symbol'] == 'ETH':
        symbol_coin =[]
        price_usd = []
        percent_change_24h = []
        percent_change_7d = []
        symbol_coin.append(x['symbol']) 
        price_usd.append(x['quote']['USD']['price'])
        # print(x['symbol'],'\n',x['quote']['USD']['price'])

        percent_change_24h.append(x['quote']['USD']['percent_change_24h'])
        # print(x['quote']['USD']['percent_change_24h'], '% IN 24H')

        percent_change_7d.append(x['quote']['USD']['percent_change_7d'])
        # print(x['quote']['USD']['percent_change_7d'], '% IN 7d')
        print(symbol_coin, price_usd,percent_change_24h,percent_change_7d)


    
        csv_writer.writerow([symbol_coin, price_usd, percent_change_24h, percent_change_7d])

def auto_repeat():
    i = 0
    while i < 1:
        api_pull_coinbase()
        print("Api Pull done")
        time.sleep(2)

auto_repeat()


